# Writing style guide — safjan.com

Use this guide whenever you write, rewrite or edit an article, note or page on
this blog. The goal is text that reads like Krystian wrote it himself: a
practitioner explaining what he did, what he found and what he'd do next.

It is based on the posts written before AI-assisted drafting (2018–2019,
the zsh rankings, the 2022 Copilot and OCR posts), the recent hand-edited ones
(Shape Up, model migration, the About page) and how Krystian communicates in
general. Some 2020–2021 tutorials ("X is a crucial step… In this article we
will explore…") were generated and are **not** a style reference.

## Who is writing, for whom

- **Author:** AI practitioner and team lead (EU research projects, ML team lead
  at Nokia, now taking generative AI from demo to production). Writes from
  hands-on experience, not from a vendor or analyst position.
- **Reader:** people who have already seen the demo and now have to live with
  the system: AI technical leaders, enterprise practitioners, forward-deployed
  engineers, senior+ ML/LLM engineers. Assume they're smart and busy. Don't
  explain what an LLM is; do explain the trade-off nobody mentions.
- **Stance:** opinions with the reasoning behind them, the methodology, the
  occasional mistake, very few predictions.

## Core traits (observed)

1. **First person, from experience.** "I had a few problems like that.",
   "From my experience, I have benefited most from…", "I've been through this a
   few times now.", "I'm a happy user of both." Claims are anchored in
   something the author did, saw or tried. When it's a hypothetical, say so
   ("Imagine a team that…").
2. **Start with the situation, not with a definition.** Good openings name a
   concrete trigger or frustration:
   - "So OpenAI deprecated `gpt-4o-mini`. … The email lands and your first
     thought is: *how hard can a model swap be?*"
   - "I keep coming back to the same frustration with how we build software."
   - "During my Christmas break, I found a blog post from…"
   Never open with "In today's fast-paced world…", "X is a crucial…", or a
   dictionary definition.
3. **Plain, direct sentences.** Mostly medium length, one idea each. Simple
   vocabulary. Short sentences are used for a beat ("Easy. Twenty minutes,
   tops."), not as a recurring rhetorical device.
4. **Practical and concrete.** Real tool names, commands, file names, numbers,
   versions, dates ("as of November 2021", "800+ → 1800+ plugins",
   "around 100 hours"). Code and commands in backticks. Examples over
   abstractions.
5. **Honest about limits.** "This post is the recording of an almost naive
   attempt…", "I don't have good answers to these questions yet - I'm still
   working through them myself.", "Perhaps there is a way to pass this
   parameter… but I have not found it yet." Admitting uncertainty is fine;
   faking certainty is not.
6. **Dry, light humour, used sparingly.** "So be nice to yourselves and
   organize…", "Predicting AI is a great way to look silly six months later."
   At most one or two per article. No jokes in headings.
7. **Reader-friendly structure.**
   - TLDR or "go straight to `[Summary and recommendations](#summary-and-recommendations)`" for long posts.
   - Numbered rules or steps with a bold lead: "**Rule #1: Keep your projects'
     directory clean**".
   - Lists and tables for comparisons (tools, metrics, GitHub stars).
   - Headings that say what the section is about ("Where the responsibility
     goes", "The typical approach for deskewing"), not clever teasers.
8. **Keeps content honest over time.** Dated notes at the top when a post ages
   ("> **NOTE:** This article was written in 2018, for a more recent version
   see…", "> **EDIT 2021:** This post is partially deprecated…"), an **Edits:**
   list at the bottom, and `Modified:` updated (see AGENTS.md).
9. **Gives credit.** Links to the original source, a "Credits" line for images,
   "Further reading" with one-line descriptions of each link
   ("- [GEPA: …](url) - paper behind the GEPA optimizer").
10. **Ends practically.** A short opinion, a next step, open questions or
    further reading. Older posts close with
    `*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*`
    No "In conclusion…" recap of everything above.

## Traits inferred from how Krystian communicates

- **Brevity and getting to the point.** He asks short, direct questions and
  expects short, direct answers. Articles should feel the same: no warm-up
  paragraphs, no restating the question.
- **Pragmatism over theory.** Cares whether something works, how to verify it
  and what it costs. Prefer "here's how to check" over "here's why it matters".
- **Verification mindset.** Reproducible steps, before/after comparisons,
  numbers with how they were measured. If a claim can't be backed up, soften it
  or drop it.
- **Strong dislike of AI-sounding text.** He will notice and reject it. When in
  doubt, write less and plainer.
- **Non-native English, clear rather than idiomatic.** Polish-born author
  writing for an international audience. Keep the English simple and correct;
  fix grammar and typos, but don't "upgrade" the prose with native-speaker
  idioms, flourishes or rare words he wouldn't use. Mild, natural phrasing such
  as "I won't deny that" or "at some point things drifted" is in character.
- **Modest, not self-promotional.** Experience is mentioned to give context,
  not to impress. No "as a thought leader…".

## Language mechanics

- Use a spaced hyphen ` - ` for asides, as in the existing posts. Avoid em
  dashes (`—`) in body text.
- Contractions are fine (I'm, don't, it's) in essays; tutorials can be a bit
  more neutral.
- "We" for a team he was part of, "you" for the reader. Avoid the royal "we"
  in tutorials ("we will now explore").
- British/American spelling: be consistent within an article; American is the
  default.
- Italics for a key term on first use or for an inner question
  (*is a human still reviewing the output?*). Bold for rule names and lead-ins,
  not for random emphasis mid-sentence.
- Headings: sentence case, `##` for sections (H1 is the title).
- Keep paragraphs to 2–5 sentences.

## Avoid (AI tells)

Rewrite any of these on sight:

- Openers: "In today's…", "In the ever-evolving landscape of…", "X is a
  crucial/critical/essential…", "Let's dive in", "In this article, we will
  explore…".
- Vocabulary: delve, leverage (as a verb for "use"), robust, seamless,
  empower, unlock, harness, landscape, realm, tapestry, pivotal, game-changer,
  cutting-edge, "plays a vital role", "it's worth noting that".
- Staccato triplets used for drama: "Dashboards are green. Reviews complete
  on time. Audits pass."
- Negative parallelism and slogan endings: "It's not X, it's Y.", "They're not
  managing risk. They're performing risk management.", "The code passes tests.
  The understanding doesn't."
- Rule-of-three lists everywhere, especially of adjectives.
- Rhetorical questions answered immediately ("The result? Chaos.").
- "Here's what surprised me:", "And that's the point.", "That's what made it
  disturbing." as transitions.
- Summary paragraphs starting with "In conclusion", "Ultimately", "Overall".
- Vague attributions ("experts say", "studies show") without a link.
- Emoji, exclamation marks in prose, marketing superlatives.

## Before / after

### Opening

> ✗ Dashboards are green. Reviews complete on time. Audits pass. And the
> organization is slowly losing track of what its own systems actually do.
>
> ✓ Every pull request gets reviewed, the architecture board signs off, the
> audit passes. On paper the team is fully in control. In practice, fewer and
> fewer people can explain why the system works the way it does.

### Transition

> ✗ The review wasn't sloppy. That's what made it disturbing.
>
> ✓ I don't think the review was sloppy, and that is what bothers me.

### Tutorial intro (illustrative - never invent experience the author didn't have)

> ✗ Data plays a critical role in the field of data science, and the accuracy
> and quality of data directly impacts the success of data-driven projects.
>
> ✓ Most of the data pipeline bugs I've chased came from the data itself.
> Here are the checks I now run first.

## Checklist before you finish

- [ ] Opening names a concrete situation, problem or trigger.
- [ ] Every claim is backed by experience, a number, a link or is clearly
      marked as opinion/hypothetical.
- [ ] No phrases from the "Avoid" list; no em dashes in body text.
- [ ] Headings describe content; long posts have a TLDR or a jump link.
- [ ] Ending is practical (opinion, next step, questions, further reading).
- [ ] English is simple and correct, not polished into someone else's voice.
- [ ] Frontmatter rules from AGENTS.md followed (`Summary`, `Status`,
      `Modified`).
