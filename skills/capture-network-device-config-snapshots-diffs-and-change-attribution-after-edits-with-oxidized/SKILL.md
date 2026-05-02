---
title: "Capture network device config snapshots diffs and change attribution after edits with Oxidized"
description: "Pull running configs from routers and switches on a schedule or after change events so you can diff drift, audit edits, and recover known-good state."
verification: "listed"
source: "https://github.com/ytti/oxidized"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ytti/oxidized"
  github_stars: 3350
---

# Capture network device config snapshots diffs and change attribution after edits with Oxidized

Use Oxidized when an agent or operator needs to collect, diff, and retain network device configurations across fleets instead of treating it as a generic network management platform. The workflow is specific: fetch configs from supported devices, trigger refreshes after change events, store version history, and inspect diffs or blame when something changed. That scope boundary—configuration backup and drift visibility for network devices—keeps this publishable as a skill instead of a plain product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized/)
