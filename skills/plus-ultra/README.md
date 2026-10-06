# Plus Ultra

Plus Ultra separates choosing a change, making it, and checking that it worked. Two independent
read-only agents propose plans; an arbiter chooses one; the main agent applies it; a fresh
verifier checks the resulting state without seeing the plan.

The point is to interrupt a familiar failure: an agent forms a plausible plan, executes commands,
then treats its own success messages as proof. Independent proposals challenge the approach
before changes happen. A plan-blind check challenges the outcome afterward.

This repository contains an **Agent Skill plus an optional, dependency-free Python hook adapter
for Claude Code**. The skill describes the method. The adapter can block recognized mutations
and turn completion until the required verdicts are recorded. Neither component supplies the
agents, guarantees their independence, or proves a recorded verdict is true.

## When to use it

Use this loop for a bounded consequential change where a mistaken plan or an unverified outcome
would be expensive: changing a deployment configuration, repairing a data-processing step, or
modifying a shared interface. It adds several agent calls, so check the budget first. Ordinary
conversation and deterministic low-risk reads usually do not need the full loop.

For example, suppose you are changing a service's configuration. One proposer checks the actual
current settings and the exact intended delta; another considers an alternative and explains why
it rejects it. Both specify verification, rollback, and uncertainty. The arbiter resolves any
conflict before the main agent changes anything.

Afterward, the verifier is told what should now be true and inspects the relevant configuration
or running service. It is not given “we ran this command successfully” as its conclusion. If it
cannot observe the result, it reports that limitation rather than converting it into a pass.

## The loop

```text
task -> blind read-only proposer A --\
                                     -> arbiter -> one plan -> main applies
task -> blind read-only proposer B --/                            |
                                                                 v
                                                   fresh plan-blind verifier
```

1. Give both proposers the same task specification, without each other's outputs.
2. Have the arbiter select or explicitly reconcile their proposals. Fundamental disagreement
   goes to the human rather than being averaged into a vague compromise.
3. Apply the authoritative plan once in the main thread. Proposers do not mutate live state.
4. Give a fresh verifier the expected observable outcome, not the plan or its rationale.
5. Record what it checked, what it found, and what remains uncertain. A failed or unobservable
   check is an outcome to report, not success.

The outputs are two candidate plans, an arbitration decision, the applied change, and an
independent reality verdict. The optional adapter also stores per-session turn state under
`~/.plus-ultra/state/` and best-effort local audit events in `~/.plus-ultra/audit.jsonl`.

## Instructions versus enforcement

| Host | What this repository provides |
|---|---|
| Claude Code | A hook adapter that can enforce recorded-plan and recorded-reality prerequisites when correctly installed and functioning |
| Codex | The skill's method by convention; no verified Codex hook adapter is shipped |
| Other agent hosts | The method by convention unless an equivalent integration is separately implemented and tested |

Installing a skill does not install hooks. Reading the instructions in Codex does not make tool
calls gated. On Claude Code, verify both configuration and actual hook behavior before relying
on enforcement.

## Install the skill

```sh
npx skills add AntreasAntoniou/plus-ultra
```

Or copy/symlink the repository into your agent host's skills directory. The entry point is
[SKILL.md](SKILL.md). Ask the host to use Plus Ultra for a specific change, with its scope,
success criteria, permissions, and budget.

### Optional Claude Code hook setup

1. Put [scripts/plusultra.py](scripts/plusultra.py) on your `PATH` as `plusultra`.
2. Merge the three entries from [examples/claude-settings.json](examples/claude-settings.json)
   into your Claude Code settings. Preserve existing hooks; do not replace the settings file.
3. Run `plusultra doctor` and confirm all three events report `ok` and the mode is enabled.
4. In a disposable test session, verify that an unplanned recognized mutation is blocked and
   that a changed turn requests a fresh reality verdict before completion.

The doctor checks for hook entries in `~/.claude/settings.json`; it does not prove the executable
is reachable, hooks are delivered, or enforcement works end to end.

### Record the actual verdicts

Once the arbiter has ruled, record its verdict for the exact session:

```sh
plusultra plan --session "$CLAUDE_SESSION_ID" --arbiter Athena --verdict -
```

After the verifier has inspected the outcome:

```sh
plusultra confirm --session "$CLAUDE_SESSION_ID" --verifier Argus --verdict -
```

Both commands read verdict text from standard input. Use the actual session ID; if the environment
does not supply it, pass it explicitly. The CLI does not guess from whichever session was most
recently active. `plusultra status --session "$CLAUDE_SESSION_ID"` shows that session's recorded state.

These commands record decisions; they do not spawn the arbiter or verifier. “Athena” and “Argus”
are role labels, not proof that separate agents were used. Record `unobservable` when nothing
can be checked, and report the task as unverified rather than successful.

## What the adapter checks—and what it cannot

`UserPromptSubmit` opens a turn. `PreToolUse` denies recognized mutating calls until a plan
entry exists. A recognized mutation invalidates an earlier reality verdict. `Stop` can block
completion until a verdict has been recorded after the latest recognized mutation.

That is a workflow prerequisite check, not an assessment of the verdict's substance. A nonempty
record does not prove that two proposers ran, that the arbiter was independent, that the change
matched the plan, or that the verifier found success.

The command classifier recognizes common filesystem, Git, package-manager, container, and HTTP
mutation shapes. It is heuristic, not a shell parser or sandbox. Unknown tools and arbitrary
interpreter code are not comprehensively covered. Subagents are exempt to prevent recursive
gating, so their read-only scope must be maintained separately. Hook-handler errors fail open;
the adapter is not a fail-closed authorization boundary.

The mode is intentionally bypassable through `PLUS_ULTRA=off` or `plusultra off`, with
`plusultra on` to re-enable the CLI-controlled mode. CLI on/off changes are recorded in the
local audit log; do not assume every environment-variable bypass has a durable receipt.

Two independent contexts can still share a false assumption, and a verifier can inspect the
wrong observable. Use real permissions, credential boundaries, and appropriate isolation for
safety. See [SECURITY.md](SECURITY.md).

## Where it fits

[Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra) helps choose or compose a
collaboration graph. Plus Ultra deliberately chooses one small graph and gives it an optional
host gate. [Grade-A Pipeline](https://github.com/AntreasAntoniou/grade-a-pipeline) is a broader
software-delivery composition with competing implementations, Git checkpoints, and tests.
[Agent Collaboration Control](https://github.com/AntreasAntoniou/agent-collaboration-control)
governs authority, evidence, and ongoing operations; recording a Plus Ultra plan does not grant
any of those permissions.

## Test

From a local checkout with Python 3:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/plusultra.py
```

The tests exercise command classification and session/verdict behavior in isolation. The second
command prints CLI help. Neither installs hooks or establishes that they work in your live host.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contributions. Licensed under the [MIT License](LICENSE).
