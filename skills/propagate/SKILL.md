---
name: "Propagate"
slug: "propagate"
description: "Propose a canonical home, concrete consumers, and any justified runtime home for a reusable tool, library, skill, document, or workflow. Use after building a reusable capability or when asked where it should live; execution requires approval of exact targets and actions."
category: "Templates & Workflows"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/propagate"
---

# Propagate

Useful work often stays stranded in its birth repository. Surface the distribution decision: one canonical home, justified consumers, and a runtime home only when needed. Skip one-off throwaway edits and avoid a distribution exercise for every small change.

This skill produces a proposal by default. It does not confer authority to copy private code, modify another repository, commit, push, publish, deploy, install, message people, or create commitments.

## Establish the authorized landscape

Identify the reusable capability and its current evidence state (idea, implementation, locally tested, integrated, or deployed). Inspect only repositories, records, and hosts already in scope. Use provided/current inventories; do not crawl a user's machine, accounts, client work, or private memory to find consumers without authorization. Mark unknown inventories as unknown and ask only when they materially affect the proposal.

Confirm ownership/license, disclosure boundary, dependencies, interfaces, compatibility, maintenance owner, and whether extraction would expose private data, embedded endpoints, host assumptions, or credentials. A plausible use case is not evidence a project needs or accepts the dependency.

## Answer three questions

### 1. Repositories: where should the artifact live?

- **Canonical home:** choose one source of truth based on ownership, generality, release cadence, and maintenance. Keeping the current home may be best. Avoid competing canonical copies.
- **Consumers:** name each authorized target, concrete benefit, and integration form: copy (simple but drifts), import/package dependency (version and release contract), or submodule (explicit checkout/update burden). Include compatibility and update ownership.
- **Skill-shaped?** Consider a reusable skill only if the artifact encodes a repeatable agent workflow. Do not turn every code module into instructions or publish a skill merely because it can be packaged.

### 2. Projects: who benefits now?

Match verified active projects to a specific problem this capability solves. Separate immediate consumers from speculative future ones, with evidence and adoption cost. Do not invent client engagements or treat stale project names as current priorities. “No additional consumer established” is a valid result.

### 3. Machines: does anything need to run?

A library, document, or skill usually needs no host. For a service, match uptime, reachability, resource use, session/secrets, data locality, backup, observability, and operator ownership to an authorized host. A sleeping development machine is not an always-on service plan. Client-facing production needs an approved account/ownership boundary. Do not provision infrastructure merely to give every proposal a machine.

## Decision-grade proposal

Keep it short: capability and evidence state; recommended canonical home; consumers with benefit/integration/cost; runtime home or “none”; risks and unresolved facts; exact proposed actions needing approval. Offer a clear default and ask which targets/actions the user approves. If several operations were listed, an ambiguous “yes” does not authorize all copies, commits, publications, and deployments.

## Apply only approved scope

If execution is requested, resolve exact source/target paths and versions, inspect target worktree state and instructions, and preserve unrelated changes. Plan update ownership and rollback before copying or deploying. Do not bundle public release, history rewrites, credential moves, provider configuration, or new infrastructure into a local integration approval.

Verify the actual change at each approved target: dependency/import resolves, tests or an appropriate check passes, and deployment readback if deployment was approved. Record original and destination versions and distinguish proposed, copied, committed, published, integrated, and deployed. Report skipped targets and failures without silently widening the plan or retrying destructive operations. Stop when approved targets are handled or a new decision/authority is required.

## Installation and upstream provenance

The upstream skill identifier is `propagate`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/propagate --skill propagate --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/propagate#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`0dfc7c8041fa`](https://github.com/AntreasAntoniou/propagate/tree/0dfc7c8041faa38561be35b3636632910c55f290). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
