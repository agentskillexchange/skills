---
name: "Operate a multi-container agent fleet on a shared task bus"
slug: "operate-agent-fleet-shared-task-bus"
description: "Run N Hermes agent containers claiming work from a shared filesystem task bus, and tell a healthy fleet from a working one. Covers the four-layer health check, dispatcher invariants, per-container model pinning, cron delivery target resolution, and the failure modes that report success while producing nothing."

category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/nusabyte-my/agent-skills"
author: "nusabyte-my"
publisher_type: "individual"
---

# Operate a multi-container agent fleet on a shared task bus

Running a fleet of agent containers is the easy part. Knowing whether they are actually
doing work is not. This skill is the four-layer check that separates the two, plus the
dispatcher invariants and the failure modes that report success while producing nothing.

## The four layers

Containers running and counted from the runtime rather than hardcoded. A periodic health
timer reporting the same count. The bus consumer's systemd timer active rather than merely
installed. And the inbox trending to zero. Each layer can pass while the next is broken,
which is why the order matters.

If the first three pass and the inbox keeps growing, the bus is write-only: nothing claims
work. That is the state worth diagnosing, because from the outside every dashboard is
green.

## Dispatcher invariants

The timer-driven dispatcher claims one task per queue under a lock, runs the agent
non-interactively with a timeout, then moves the agent's output document to outbox and
archives the task. Three prompt invariants have to be baked in, because the agent otherwise
interprets the task file literally: never send email, post, or submit to a portal (drafting
is the job); always write the deliverable to the outbox path regardless of the path the
task file names; and treat a `status: blocked` answer containing a specific question as
success, otherwise an agent that correctly cannot proceed retries forever or fabricates.

## Failure modes that look like success

A write-safe root that excludes the bus mount makes every task-file write instruction fail
and the run still reports success with an empty outbox. An outbox directory owned by root
fails the atomic temp-file rename after the agent has done all the work. A shared provider
key means one quota cap stalls the whole fleet at once. A model swap requires three writes
— provider pin, provider block, API key in the container environment — and missing either
of the last two produces the identical "no LLM provider configured" error. And the
non-interactive agent exits zero on a rate-limit failure, so the presence of the output
file is the only reliable success signal.

## Operational details

Read each container's model pin with a single grep across the fleet and `sort | uniq -c` on
the provider column rather than N individual smoke tests. After any bulk config pass, smoke
several containers rather than one, because their configs are separate files and loops skip
some. Do not diagnose a stalled bus from `journalctl` alone: the timer reports `activating`
mid-run, which reads as hung but is normal — the per-task run log distinguishes a working
run from a zero-byte one.

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/nusabyte-my/agent-skills.git
cp -R agent-skills/skills/agent-fleet-task-bus ~/.agent-skills/agent-fleet-task-bus
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add nusabyte-my/agent-skills --skill agent-fleet-task-bus
```

## Cron delivery

`deliver: telegram` alone fails with "no delivery target resolved" even with a valid bot
token. The allowed-users list must be non-empty and the channel directory must be populated,
which only happens once a DM actually arrives. Verify with a direct send to an explicit
`platform:<chat_id>` target, then bind the cron job to that same target.
