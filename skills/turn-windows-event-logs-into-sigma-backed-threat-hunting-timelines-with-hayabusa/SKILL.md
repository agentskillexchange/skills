---
title: "Turn Windows event logs into Sigma-backed threat-hunting timelines with Hayabusa"
description: "Parse Windows event logs into fast timelines and detection-rich outputs so agents can triage suspicious host activity, search for known patterns, and hand investigators reviewable artifacts."
verification: "listed"
source: "https://github.com/Yamato-Security/hayabusa"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Yamato-Security/hayabusa"
  github_stars: 3116
---

# Turn Windows event logs into Sigma-backed threat-hunting timelines with Hayabusa

Use Hayabusa when an agent needs to ingest EVTX data, apply Sigma-aligned detections, and produce a timeline for Windows host triage or enterprise threat hunting. The scope boundary is concrete: it is about turning Windows event logs into investigation-ready timelines and detections, whether from live systems or collected logs. That is a bounded DFIR workflow with a clear input and output, not a generic security platform or endpoint product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa/)
