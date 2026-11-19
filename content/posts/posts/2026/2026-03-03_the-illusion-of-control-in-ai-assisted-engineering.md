---
Title: The illusion of control in AI-assisted engineering
Slug: the-illusion-of-control-in-ai-assisted-engineering
Date: 2026-03-03
Modified: 
Start: 
Tags: 
Category: Machine Learning
Image: /images/head/abstract_1.jpg
banner: "/images/head/abstract_1.jpg"
Summary: AI-assisted engineering keeps operational control (approve, reject, sign off) but erodes epistemic control (understanding what was built and why). How review ceremonies turn into governance theater, how responsibility diffuses, and the slower risks of architectural drift and unexplainable systems.
Status: published
---

## The illusion of control in AI-assisted engineering

Every pull request gets reviewed, the architecture board signs off, the audit passes. On paper the team is fully in control. In practice, fewer and fewer people can explain why the system works the way it does.

I've seen this a few times now in teams that lean heavily on AI-assisted engineering. Nobody skipped a step - the reviews, sign-offs and checklists are all still there. What quietly changed is what they check: whether the output looks right, not whether anyone understands it.

### Two kinds of control

When a team adopts AI-assisted development, the first question management usually asks is: *is a human still reviewing the output?* The answer is yes. Code review gates are in place, architecture sign-offs happen, compliance checklists get filled in.

The problem is that "oversight" covers two different things. The first one is *operational control* - can you approve, reject or modify the output? The second one is *epistemic control* - do you understand what was built, why it works this way and what it assumes?

AI-assisted workflows keep the first one and slowly erode the second. The governance frameworks I know were designed at a time when the two went together. The engineer who wrote a module also defended it in review and signed off on it, and they understood it because they built it. With AI in the loop this coupling is gone, and most organizations haven't noticed yet.

### What it looks like in practice

An example from a project I was involved in last year. The team was building an integration layer between an enterprise platform and a third-party data provider. AI tooling generated the service contracts, the transformation logic and the error-handling paths. Engineers reviewed all of it, and the review was actually good - line-by-line, lots of comments on the PR, long discussions about edge cases. Better than most reviews I've seen. The architecture board signed off.

Six months later we had a cascading failure. The root cause was a silent retry pattern in the error-handling logic that misbehaved under load. In the postmortem someone asked who understood the design intent behind that module, and there was no good answer. The AI generated it. The engineer reviewed it carefully, caught formatting issues and a missing null check, but never asked *why the retry logic was structured this way*. The review was focused on "is this correct", not on "what does this assume".

I don't think the review was sloppy, and that is what bothers me. The process did what it was designed to do. It just wasn't designed for code that nobody had thought through before it showed up in a PR.

In compliance the same gap gets more expensive. Imagine a software company under financial regulation that is asked during an external audit to explain the reasoning behind an algorithm that classifies customer data. The honest answer would be: it was AI-generated and the team validated the outputs without tracing the reasoning. No compliance framework accepts that. You either reconstruct a rationale after the fact or admit a gap the auditors weren't even looking for.

### Where the responsibility goes

In a typical engineering workflow you can point at a person and say: you designed this, you understood it, you signed off. Architecture review boards exist partly to create that paper trail. When something breaks, you know who to ask.

With AI-assisted workflows there is something in the authorship chain that can't be asked, can't explain itself and can't take responsibility when a regulator shows up. The responsibility doesn't move to the AI - it gets spread across everyone who touched the output. Everyone reviewed it, nobody wrote it. So when an incident review or an auditor asks "who understood this design", nobody can really answer.

You won't notice this in a single sprint. After a year, though, you can end up with a pile of production systems where the design intent and the assumptions were never written down, and the engineers maintaining the code can't tell you why a service boundary is where it is or why the retry logic works the way it does. Tests pass and the architecture diagrams exist, but the understanding is missing.

### The slower risks

When leadership talks about AI in engineering, the focus is usually on the obvious risks: hallucinated code, security vulnerabilities, IP leakage. Those are real. The ones I worry about more take longer to show up.

The first is architectural drift. When many teams in an organization generate code with AI without a shared context, each team's output carries slightly different assumptions about data models, error handling and service contracts. Service A assumes retries are idempotent, service B doesn't. Both pass their own tests. The inconsistency shows up only when they run together under load, and then it spreads quickly.

The second is that AI-generated systems are hard to change later. Regular technical debt is annoying but manageable, because at some point someone on the team understood the code. When a system was generated and reviewed, but not really authored, the next team inherits a black box. They can't refactor with confidence because nobody can tell them what the original constraints were. So they wrap it, route around it or leave it alone, and the codebase gets more rigid over time - in a different way than with normal code decay.

Regulators are catching up as well. Especially in financial services and telecom, the questions about AI-assisted code generation are getting quite specific. The organizations I would worry about are not the ones using AI the most, but the ones that adopted it without adjusting their traceability and governance.

### A better question to ask

Whether humans are in the loop is not a useful question anymore - they are. More useful is to ask whether the person clicking "approve" on a PR could explain the design to an auditor, rebuild the module if the original was lost, or predict how it fails in conditions the tests don't cover.

Reviewing code for correctness and understanding the architecture of a system are two different activities. Review processes were designed when they were one activity. AI-assisted workflows split them, and the process wasn't updated to compensate.

Part of this can be fixed. Not every AI-generated module needs deep human understanding - boilerplate, scaffolding and config are fine. But integration contracts, error-handling strategies and anything that encodes assumptions about how other systems behave need someone who understands them, and "reviewed the PR" is not the same thing. A few changes I would consider:

- architecture reviews that ask "why is it designed this way", not only "does this look right",
- traceability for AI-generated code that records the assumptions, not only the output.

If the review ceremonies keep running while the understanding behind them thins out, that's risk management on paper only. It works until someone tests it, and in regulated industries that usually happens during an incident or an audit, when the consequences are already serious.

### Questions I keep asking myself

Can your organization tell the difference between systems your teams approved and systems they actually understand? Does anyone track that? I haven't seen it tracked anywhere.

If a regulator or a potential acquirer asked your team to walk through the design intent of a critical integration, who would take that call? Would they explain what they know, or reverse-engineer it on the spot?

Have your sign-off processes changed since you started using AI? Each code review approval and architecture sign-off carries an implicit statement: "I understood this". If in practice it has become "I checked this", the paperwork still looks the same, but the assurance behind it is gone.

I don't have good answers to these questions yet - I'm still working through them myself.
