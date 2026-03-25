---
name: "Deepgram Podcast Chapter Generator"
description: "Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry."
category: "Media & Transcription"
framework: "ChatGPT Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "notion"  # from ase_tool_match
  github_stars: 5562  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1084242  # from ase_npm_downloads
  github_repo: "makenotion/notion-sdk-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Deepgram Podcast Chapter Generator

Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.

## Overview

Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a codex
```

### OpenClaw

```bash
clawhub install deepgram-podcast-chapter-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/
