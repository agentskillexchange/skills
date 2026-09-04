---
name: "Proofed Completion Gate"
slug: "proofed-completion-gate"
description: "Uses the Proofed CLI and current-subject completion receipts to reject unsupported coding-agent completion claims, rerun repository-configured tests, and detect stale PASS evidence after code changes."
github_stars: 0
verification: "listed"
source: "https://github.com/liangfeng-hu/proofed"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "liangfeng-hu/proofed"
  github_stars: 0
---

# Proofed Completion Gate

Proofed is a deterministic completion gate for coding agents. Use this skill when an
agent is about to claim that a repository task is complete and the claim should be
checked against evidence from the current checkout rather than accepted from the
model's narration. The `proofed` CLI records a run, executes repository-configured
tests when authorized, binds the result to a digest of the current code, and emits a
portable completion receipt. If code changes afterward, independent receipt checking
returns `STALE_SUBJECT` instead of accepting the old PASS. This is useful across
Claude Code, Codex, Cursor, OpenClaw, and other agents because the gate is local and
does not require a model API key or private Proofed service.

## When to use

- Before stating that a coding task is complete.
- When a prior test result may belong to an older code state.
- When CI or another tool needs a portable, independently readable completion receipt.
- After an interrupted session, to recover the current intent, missing evidence, and
  next legal action with `proofed status`.

## Operating procedure

1. Check whether the `proofed` command and repository opt-in file `.proofed.yml` exist.
   If either is absent, report that the gate has not run. Ask before installing the
   package or initializing the repository.
2. Run `proofed status` before choosing the next action. Do not repeat a failed path
   listed there without new distinguishing evidence.
3. Run `proofed verify` before accepting a completion claim.
4. If the result is `REJECT: missing tests_passed`, and the detected test command is
   appropriate for this repository, run `proofed verify --run-tests`.
5. Accept completion only when Proofed emits `PASSED` for the current subject. Any
   later code change requires fresh evidence.
6. When consuming an existing receipt, run
   `proofed check-receipt RECEIPT --current .` so subject binding is checked as well as
   receipt structure.

Do not treat passing tests as proof that software is correct. Do not describe a host
hook as unbypassable, and do not silently opt a repository into enforcement. CI that
re-verifies the current checkout is the stronger shared gate.

## Install the runtime

Proofed requires Python 3.10 or later. The public package has no third-party runtime
dependencies:

```bash
python -m pip install --pre "proofed-agent>=0.1.0a3,<0.2"
proofed --version
```

Repository opt-in and a first evidence-gated run:

```bash
proofed init
proofed run . --intent "finish the current repository task"
proofed status
proofed verify --run-tests
```

## Install this skill

After this skill is published in Agent Skill Exchange:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill proofed-completion-gate
```

For a manual installation, clone the catalog and copy the skill directory into the
location used by the target agent:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/proofed-completion-gate ~/.agent-skills/proofed-completion-gate
```

The upstream Proofed repository also exposes its canonical skill directly:

```bash
npx skills add liangfeng-hu/proofed --skill proofed-verify
```

## GitHub Actions gate

Use the tagged public Action to re-verify the checked-out pull request rather than
trusting a committed PASS file:

```yaml
- uses: liangfeng-hu/proofed@v0.1.0-alpha.3
  with:
    target: .
```

See the upstream red/green demonstration, receipt specification, and independent
Python and JavaScript verifiers at https://github.com/liangfeng-hu/proofed.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/liangfeng-hu/proofed

