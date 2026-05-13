---
title: "Turn Windows event logs into Sigma-backed threat-hunting timelines with Hayabusa"
slug: "turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa"
description: "Parse Windows event logs into fast timelines and detection-rich outputs so agents can triage suspicious host activity, search for known patterns, and hand investigators reviewable artifacts."
github_stars: 3116
verification: "security_reviewed"
source: "https://github.com/Yamato-Security/hayabusa"
author: "Yamato Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Yamato-Security/hayabusa"
  github_stars: 3116
---

# Turn Windows event logs into Sigma-backed threat-hunting timelines with Hayabusa

Parse Windows event logs into fast timelines and detection-rich outputs so agents can triage suspicious host activity, search for known patterns, and hand investigators reviewable artifacts.

## Prerequisites

Hayabusa plus Windows event logs from a live system, offline collection, or enterprise collection pipeline.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a Hayabusa release or build from source, then run its timeline and analysis commands against Windows EVTX files or collected event log directories.
```

## Documentation

- https://github.com/Yamato-Security/hayabusa

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa/)
