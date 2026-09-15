# Propagate

An agent skill by [Antreas Antoniou](https://github.com/AntreasAntoniou). Version 1.0.0; MIT licensed.

## Problem

Reusable work gets stranded in its birth repository, or spreads as unowned copies that drift.

## Mechanism

Propose one canonical home, evidence-backed consumers and integration forms, project benefits, and a runtime home only if needed. Execute only exact approved targets/actions and verify their actual state.

## Why useful

Distribution becomes an explicit ownership and maintenance decision instead of an automatic copy/deploy reflex. A no-host or no-additional-consumer outcome is valid.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/propagate --skill propagate
```

Use a compatible agent's skill installer with `AntreasAntoniou/propagate`, or clone this repository into that host's configured skills directory under the folder name `propagate`:

```sh
git clone https://github.com/AntreasAntoniou/propagate.git <your-skills-directory>/propagate
```

Replace the destination placeholder first. The repository root is the single discoverable skill, with [SKILL.md](SKILL.md) as its entry point. Installation location and reload/discovery steps vary by host. Installing the skill grants no extra permissions. The host must support Markdown skills; only packages with helpers require Python.

## Example

> Use $propagate to propose where this reusable validation helper should live. Use only the two repositories I supplied. Identify a canonical home and a consumer strategy, with maintenance cost; make no changes.

This release is instruction-only and contains no deployment or synchronization runtime. Verify ownership, license, target state, and disclosure constraints before applying an approved proposal.

## Trust boundary

Proposal first. The skill does not authorize private inventory crawling, cross-repository changes, commits, publication, deployment, credential moves, or client commitments. Approval for one operation does not imply approval for every proposed operation.

## Validation

There is no executable runtime in this package. Review its behavior against a scoped hypothetical request: distinguish evidence from inference, preserve authorization boundaries, and state what remains unverified. If the official skill-creator validator is installed in your environment, run its `quick_validate.py` against this directory. That checks skill packaging, not the truth of a review or the effectiveness of the workflow.

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [CHANGELOG.md](CHANGELOG.md).
