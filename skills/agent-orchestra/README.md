# Agent Orchestra

Agent Orchestra teaches an AI agent how to design a team for a task: who works independently,
who sees whose findings, who settles disagreements, and who tries to prove the result wrong.
The useful unit is not “five agents.” It is the information flow between them.

This is an installable **Agent Skill: instructions, a pattern catalog, and a worked workflow
example**. It is not an agent runtime, a hosted service, or a library that spawns agents by itself.
Your host supplies the agents, tools, models, and isolation.

## The problem it addresses

Adding reviewers can produce more agreement without producing better evidence. If every reviewer
reads the first answer, they can inherit its mistake. If competing implementers edit the same
files, parallel work becomes an integration problem. If a synthesizer smooths over disagreement,
the most important finding can disappear from the final answer.

Orchestra makes those choices explicit. Independent first passes stay blind. An arbiter must
resolve a disagreement or preserve it for escalation. An adversary looks for reasons the chosen
answer fails. For code-producing work, each writer has a defined file scope and an isolated
working area, and integration is a separate responsibility.

Use it when the hard part is deciding **how several agents should cooperate**: an uncertain design,
a correctness-critical change, a research synthesis, or a document whose claims and rendered
figures both need scrutiny. A deterministic lookup or small, low-risk edit usually needs one agent.

## A concrete example

Suppose a report reads convincingly, but you need to know whether its charts actually support
its conclusions. A useful graph might be:

```text
report -> independent claim and evidence reviews -> textual verdict
rendered pages + textual verdict -> visual contradiction checks
both sets of findings -> adversary -> arbiter -> findings, dissent, next checks
```

The visual stage deliberately sees the textual verdict: it needs to challenge statements such as
“the chart supports this claim.” The initial reviewers do not see one another's findings: their
job is to notice things independently. Knowing where to share context, and where not to, is the
point of the skill.

The included [saturating review example](examples/saturating-review-engine.workflow.js) develops
this further. Each reviewer contains its own smaller review graph; text reviews feed visual
checks; an optional rewrite stage produces a revised copy and sends it back through review.
It supports a review-only mode, a round ceiling, and a “no findings left” stopping condition.
The default mode is `fix`, so choose `mode: "review"` explicitly when edits are not authorized.

## How it works

Start with the failure you need to catch, then compose the smallest graph that can catch it:

| Need | Useful structure |
|---|---|
| Challenge one consequential decision | Two blind proposals, then an arbiter |
| Cover different failure modes | Independent review lenses, then adjudication and refutation |
| Investigate an evolving disagreement | A committee whose arbiter can ask targeted follow-up questions |
| Check words against visible evidence | A visual stage conditioned on the textual claims |
| Improve an artifact over several passes | Review and rewrite stages in a bounded feedback loop |

A node can itself be a smaller graph. Dependency edges determine what must run in sequence;
unrelated work can run concurrently. Machine-consumed results need schemas. Fundamental
disagreement needs an escalation path, not a forced consensus.

For code-producing waves, the skill calls for a recoverable backup, a disposable source copy,
single-owner file scopes, returned patches, and verification after integration. Preserve useful
outputs durably; a temporary source copy is not an archive. These are operating instructions,
not filesystem enforcement, and they do not authorize a remote push.

## What you get

Applying the skill should leave a graph suited to your task, role-specific briefs, explicit
context boundaries, and an integration decision with supporting evidence, gaps, and dissent.
Those outputs are produced by your agent host; the skill does not maintain a central job database.

The example adapter returns a review panel and round history. In fix mode it also returns the
final artifact manifest and whether its stopping condition was reached. “Saturated” means that
this review process stopped finding outstanding issues, not that the artifact is correct.

## Install and use

```sh
npx skills add AntreasAntoniou/agent-orchestra
```

The repository root is the skill directory. You can also copy or symlink it into your host's
skills directory. From this repository, for example:

```sh
ln -s "$(pwd)" ~/.agents/skills/agent-orchestra
```

Ask your host to use Agent Orchestra to design the collaboration graph, naming the deliverable,
risks, available tools, budget, and permitted changes. Host discovery and invocation syntax vary.

The JavaScript example requires a compatible workflow host that injects `agent`, `parallel`,
`phase`, `log`, and `args`; the broader catalog also uses `pipeline`. It is **not a standalone
Node program**. A port must preserve context isolation, structured outputs, dependency edges,
and filesystem boundaries. Rendering and inspecting images require tools and models supplied
by the host.

## How it differs from related skills

| Skill | Primary question |
|---|---|
| Agent Orchestra | What collaboration graph fits this task? |
| [Plus Ultra](https://github.com/AntreasAntoniou/plus-ultra) | How do we follow one fixed propose → arbitrate → apply → independently verify loop? |
| [Agent Collaboration Control](https://github.com/AntreasAntoniou/agent-collaboration-control) | Who may act, what evidence permits the next transition, and how do we supervise ongoing work? |
| [Grade-A Pipeline](https://github.com/AntreasAntoniou/grade-a-pipeline) | How do we apply these patterns to a staged software build with Git checkpoints and tests? |

They can be combined; they are not interchangeable runtimes.

## Limits and validation

Independent contexts do not guarantee independent reasoning. Several calls to the same model
can share a blind spot; different models can too. An arbiter can choose the wrong plan, and a
schema can validate a false claim. The named “Byzantine” patterns are review arrangements, not
a formally proven Byzantine fault-tolerant consensus protocol. Orthogonality and emergence
scores in the catalog are design heuristics, not validated measures of correctness.

Nested graphs can become expensive quickly. Set the budget and stopping rules before launching;
do not treat the largest example as the default for every task.

From a local checkout:

```sh
python3 tests/validate_repo.py
node --check examples/saturating-review-engine.workflow.js
```

These check package structure and example syntax. They do not execute a multi-agent workflow
or establish its effectiveness on your task.

Read [SKILL.md](SKILL.md) for the full grammar, [PLAYBOOK.md](PLAYBOOK.md) for the compact
reference, and the [token-efficient overlay](variants/token-efficient/SKILL.md) for model-tier
allocation guidance. Contributions and security reports are covered in
[CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

Licensed under the [MIT License](LICENSE).
