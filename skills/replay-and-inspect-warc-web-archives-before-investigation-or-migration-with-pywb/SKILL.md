---
title: "Replay And Inspect WARC Web Archives Before Investigation Or Migration With Pywb"
description: "Replay WARC-backed web archives locally so an agent can inspect historical pages, validate captures, and review preserved site behavior before migration or investigation work."
verification: "security_reviewed"
source: "https://github.com/webrecorder/pywb"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "webrecorder/pywb"
  github_stars: 1646
---

# Replay And Inspect WARC Web Archives Before Investigation Or Migration With Pywb

pywb is a skill for replaying and inspecting WARC web archives with high-fidelity historical playback. An agent should invoke it when the user needs to review captured pages, query archived states, or verify historical evidence before migration checks, takedown response, incident reconstruction, or archive QA. Use this instead of browsing the live site or using a generic archiving platform when the actual job is local replay and inspection of archived captures. The boundary is narrow: load archived collections, replay them, inspect what was preserved, and hand findings to the next step. It is not a generic CMS, crawler, or broad web platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb/)
