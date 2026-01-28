---
Title: The limiting factor at work isn't writing code anymore
Slug: the-limiting-factor-at-work-isnt-writing-code-anymore
Date: 2026-01-28
Modified: 2026-01-28
Status: published
Tags: agentic-coding, vibe-coding, software-development, software-project
Category: note
---

In a Hacker News [discussion](https://news.ycombinator.com/item?id=46782811)! on the article [Management as AI Superpower](https://www.oneusefulthing.org/p/management-as-ai-superpower) by Ethan Mollick, I came across a comment that resonated strongly with a realization I’ve had recently while coding with a factory.ai droid:

> The limiting factor at work isn’t writing code anymore. It’s deciding what to build and catching when things go sideways.

([link](https://news.ycombinator.com/item?id=46783415) by [augusteo](https://news.ycombinator.com/user?id=augusteo))

This observation forces a shift in priorities.

## Deciding what to build

Creative minds tend to have no shortage of ideas. With agentic coding, it’s incredibly tempting to start immediately: the goal feels only “a few hours of AI agent work” away, something you can even run in the background.

Starting to build something immediately, however, incurs real costs:
- mental engagement
Once you commit, you have to keep making decisions: should you continue, pivot, or drop the project? Dropping it comes with a psychological cost—unfinished work, a sense of abandonment, or the feeling of being unable to finish. These are easy mental traps to fall into. You end up with one more thing occupying your cognitive space.

The unfinished projects creating cognitive and emotional debt - “psychological technical debt”.  AI accelerates its accumulation by lowering the barrier to starting but not to finishing.

- expected returns on investment
You still need to ask “why” you are building something—ideally several times, as in the [Five Whys](https://en.wikipedia.org/wiki/Five_whys) method. Even in the era of AI agents, resources remain limited. Your time is certainly finite. I’ll set aside, for now, considerations about token costs—both in dollars and in the broader sense of shared planetary resources.

Decision latency can be a competitive advantage. This could be expanded into a framework for “pre-coding decision filters” in an agentic world: how to deliberately slow down before starting, when everything pushes you to start immediately.


## Catching when things go sideways

In many of my projects, there hasn’t been enough time to add strong guardrails for quickly detecting when things start to go wrong. Test suites need to be designed with clear principles and intent.

Today, it’s easy to get close to 100% test coverage with AI agents. The problem lies deeper, in how models are trained: they are optimized to produce an answer rather than to challenge assumptions. I’ve experienced that when a test suite is AI-generated from existing code, it can be fundamentally flawed. The tests often mirror the current implementation of the business logic—even if that logic is incorrect.

Without solid specifications or clearly stated expectations, generated tests tend to confirm what already exists rather than falsify it. They won’t catch flaws unless there is a reliable external reference, such as a well-defined specification. “AI tests can be bad,” is known  but more: they systematically reflect existing assumptions unless anchored to external specifications. This confirmatory nature of AI-generated tests is a blind spot for teams that want to quickly close testing gaps and reduce technical debt.

From a Python-specific perspective, extensive usage of typing mechanisms available in Python can help catching bugs and inconsistencies in implementation. 

## Other thoughts from the discussion

> The skills that matter are the same ones that make someone a good manager of people.

([link](https://news.ycombinator.com/item?id=46783415) by [augusteo](https://news.ycombinator.com/user?id=augusteo))

The current situation creates pressure for a fast track into managerial competence. Developers supervising and mentoring AI agents get many hours of practice in planning, delegating, and communicating work in a clear, actionable, and precise way. This becomes a kind of manager’s dojo: a training ground entered almost automatically when stepping into AI-assisted coding. Agent supervision exercises the same muscles as people management: planning, delegation, expectation-setting, and review. This reframes career progression and challenges the idea that management skills only come from managing people. I expect in a near future an abundance of technically inclined people with strong managerial skills, even if they have never formally led a human team.

Another comment adds an important nuance:

> The apparent speedup only holds if we ignore the cost of comprehension and review; once those are included, the comparison becomes less about raw code throughput and more about where and how understanding is generated in the process.

([link](https://news.ycombinator.com/item?id=46792118) by [ithkuil](https://news.ycombinator.com/user?id=ithkuil))

This reframes productivity not as code output, but as the efficiency of understanding.

