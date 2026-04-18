---
title: "Capture Linux runtime security events and suspicious behavior for live triage with Tracee"
description: "Watch live Linux and container activity through eBPF so you can triage suspicious runtime behavior before it disappears into guesswork."
verification: listed
source: "https://github.com/aquasecurity/tracee"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/tracee"
  github_stars: 4468
---

# Capture Linux runtime security events and suspicious behavior for live triage with Tracee

Use Tracee when an agent needs a live runtime forensics pass on a Linux host or container environment instead of a generic security platform or static scanner. The workflow is bounded: attach Tracee, collect runtime events or detections, filter on suspicious behavior, and inspect what processes, syscalls, or containers are actually doing. That scope boundary, runtime event capture and triage through Tracee, keeps this from being just a product card for a broader security offering.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/capture-linux-runtime-security-events-and-suspicious-behavior-for-live-triage-with-tracee
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/capture-linux-runtime-security-events-and-suspicious-behavior-for-live-triage-with-tracee` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-linux-runtime-security-events-and-suspicious-behavior-for-live-triage-with-tracee/)
