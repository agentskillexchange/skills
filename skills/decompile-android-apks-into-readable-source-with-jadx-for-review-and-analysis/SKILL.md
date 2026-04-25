---
title: "Decompile Android APKs into readable source with jadx for review and analysis"
description: "Turn an APK into readable Java or decompiled source artifacts so an agent can inspect behavior before deeper reverse-engineering or triage."
verification: "listed"
source: "https://github.com/skylot/jadx"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "skylot/jadx"
  github_stars: 46142
---

# Decompile Android APKs into readable source with jadx for review and analysis

Use jadx when the task is to convert an Android APK into readable source for inspection, not when a user is simply using Android tooling normally. The agent workflow is specific: load the APK, decompile Dalvik bytecode into readable source, and inspect code paths, resources, or app behavior clues. That scope boundary, APK-to-readable-source analysis, keeps this narrower than a generic Android tooling or product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/decompile-android-apks-into-readable-source-with-jadx-for-review-and-analysis/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/decompile-android-apks-into-readable-source-with-jadx-for-review-and-analysis
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/decompile-android-apks-into-readable-source-with-jadx-for-review-and-analysis`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decompile-android-apks-into-readable-source-with-jadx-for-review-and-analysis/)
