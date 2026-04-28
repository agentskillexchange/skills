---
title: Deepgram Podcast Chapter Generator
description: Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize
  features, then clusters returned timestamps into logical chapters using a sliding-window
  topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready
  podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.
verification: security_reviewed
source: https://developers.deepgram.com/
category:
- Media & Transcription
framework:
- ChatGPT Agents
---

# Deepgram Podcast Chapter Generator

Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/deepgram-podcast-chapter-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/deepgram-podcast-chapter-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/)
