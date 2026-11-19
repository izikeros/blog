#!/bin/sh
# Pull-based GitHub -> Forgejo sync (runs on the NAS from cron).
#
# Forgejo -> GitHub is handled by a Forgejo push mirror. This script brings
# commits made on GitHub (merged PRs, web edits) into Forgejo:
#   - branch missing on Forgejo          -> push
#   - Forgejo behind GitHub (ancestor)   -> fast-forward push
#   - Forgejo ahead of GitHub            -> skip (push mirror updates GitHub)
#   - diverged                           -> log DIVERGED, exit 1 (fix manually)
#   - tag missing on Forgejo             -> push; differing tag -> log, exit 1
# Pushes are never forced. Pushing back the mirror's echo is a no-op.
#
# Usage: github-to-forgejo-sync.sh /path/to/repo.env
# Config (env file): GITHUB_URL, FORGEJO_URL, FORGEJO_USER, FORGEJO_TOKEN,
#   optional: GITHUB_TOKEN, WORKDIR, LOG, GIT, SYNC_LOW_SPEED_TIME (s),
#   SYNC_LOW_SPEED_LIMIT (bytes/s), SYNC_LOCK_MAX_AGE (s), SYNC_LOG_MAX_BYTES

set -u
PATH="/opt/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

CONF="${1:?usage: $0 /path/to/repo.env}"
# shellcheck disable=SC1090
. "$CONF"
: "${GITHUB_URL:?}" "${FORGEJO_URL:?}" "${FORGEJO_USER:?}" "${FORGEJO_TOKEN:?}"

BASE="$(dirname "$CONF")/$(basename "$CONF" .env)"
WORKDIR="${WORKDIR:-$BASE.git}"
LOG="${LOG:-$BASE.log}"
GIT="${GIT:-git}"
LOW_SPEED_TIME="${SYNC_LOW_SPEED_TIME:-60}"
LOW_SPEED_LIMIT="${SYNC_LOW_SPEED_LIMIT:-1000}"
LOCK_MAX_AGE="${SYNC_LOCK_MAX_AGE:-3600}"
LOG_MAX_BYTES="${SYNC_LOG_MAX_BYTES:-1048576}"
LOCK="$WORKDIR.lock"

log() { echo "$(date '+%Y-%m-%dT%H:%M:%S%z') $*" >>"$LOG"; }

if [ -f "$LOG" ] && [ "$(wc -c <"$LOG")" -gt "$LOG_MAX_BYTES" ]; then
    mv "$LOG" "$LOG.1"
fi

if ! mkdir "$LOCK" 2>/dev/null; then
    age=$(($(date +%s) - $(stat -c %Y "$LOCK" 2>/dev/null || date +%s)))
    if [ "$age" -lt "$LOCK_MAX_AGE" ]; then
        exit 0
    fi
    log "WARN removing stale lock ($age s)"
    rmdir "$LOCK" 2>/dev/null
    mkdir "$LOCK" || exit 1
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT INT TERM

basic() { printf '%s:%s' "$1" "$2" | base64 | tr -d '\n'; }

# Credentials go through GIT_CONFIG_* env (not argv/URL), so they stay out of
# `ps` output and logs.
export GIT_CONFIG_COUNT=2
export GIT_CONFIG_KEY_0=http.lowSpeedTime GIT_CONFIG_VALUE_0="$LOW_SPEED_TIME"
export GIT_CONFIG_KEY_1=http.lowSpeedLimit GIT_CONFIG_VALUE_1="$LOW_SPEED_LIMIT"
FJ_AUTH="http.extraHeader=Authorization: Basic $(basic "$FORGEJO_USER" "$FORGEJO_TOKEN")"
GH_AUTH=""
if [ -n "${GITHUB_TOKEN:-}" ]; then
    GH_AUTH="http.extraHeader=Authorization: Basic $(basic x-access-token "$GITHUB_TOKEN")"
fi

g() { "$GIT" --git-dir="$WORKDIR" "$@"; }
with_auth() {
    auth="$1"; shift
    if [ -n "$auth" ]; then
        GIT_CONFIG_COUNT=3 GIT_CONFIG_KEY_2="${auth%%=*}" \
            GIT_CONFIG_VALUE_2="${auth#*=}" g "$@"
    else
        g "$@"
    fi
}

[ -d "$WORKDIR" ] || "$GIT" init -q --bare "$WORKDIR" || exit 1

if ! out=$(with_auth "$GH_AUTH" fetch -q --prune --no-tags "$GITHUB_URL" \
    "+refs/heads/*:refs/gh/heads/*" "+refs/tags/*:refs/gh/tags/*" 2>&1); then
    log "ERROR fetch github: $out"; exit 1
fi
if ! out=$(with_auth "$FJ_AUTH" fetch -q --prune --no-tags "$FORGEJO_URL" \
    "+refs/heads/*:refs/fj/heads/*" "+refs/tags/*:refs/fj/tags/*" 2>&1); then
    log "ERROR fetch forgejo: $out"; exit 1
fi

rc=0
push() {
    if out=$(with_auth "$FJ_AUTH" push -q "$FORGEJO_URL" "$1:$2" 2>&1); then
        log "OK $3 $2 -> $(echo "$1" | cut -c1-9)"
    else
        log "ERROR push $2: $out"; rc=1
    fi
}

for ref in $(g for-each-ref --format='%(refname)' refs/gh/heads/); do
    name="${ref#refs/gh/heads/}"
    gh=$(g rev-parse "$ref")
    fj=$(g rev-parse -q --verify "refs/fj/heads/$name" 2>/dev/null || true)
    if [ "$gh" = "$fj" ]; then
        continue
    elif [ -z "$fj" ]; then
        push "$gh" "refs/heads/$name" new
    elif g merge-base --is-ancestor "$fj" "$gh"; then
        push "$gh" "refs/heads/$name" fast-forward
    elif g merge-base --is-ancestor "$gh" "$fj"; then
        :  # Forgejo ahead; push mirror will update GitHub
    else
        log "DIVERGED refs/heads/$name github=$(echo "$gh" | cut -c1-9) forgejo=$(echo "$fj" | cut -c1-9)"
        rc=1
    fi
done

for ref in $(g for-each-ref --format='%(refname)' refs/gh/tags/); do
    name="${ref#refs/gh/tags/}"
    gh=$(g rev-parse "$ref")
    fj=$(g rev-parse -q --verify "refs/fj/tags/$name" 2>/dev/null || true)
    if [ -z "$fj" ]; then
        push "$gh" "refs/tags/$name" new-tag
    elif [ "$gh" != "$fj" ]; then
        log "TAG-CONFLICT refs/tags/$name"; rc=1
    fi
done

exit "$rc"
