---
title: "Replay And Inspect WARC Web Archives Before Investigation Or Migration With Pywb"
description: "Replay WARC-backed web archives locally so an agent can inspect historical pages, validate captures, and review preserved site behavior before migration or investigation work."
verification: listed
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

pywb is a skill for replaying and inspecting WARC web archives with high-fidelity historical playback. An agent should invoke it when the user needs to review captured pages, query archived states, or verify historical evidence before migration checks, takedown response, incident reconstruction, or archive QA.

Use this instead of browsing the live site or using a generic archiving platform when the actual job is local replay and inspection of archived captures. The boundary is narrow: load archived collections, replay them, inspect what was preserved, and hand findings to the next step. It is not a generic CMS, crawler, or broad web platform listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/replay-and-inspect-warc-web-archives-before-investigation-or-migration-with-pywb/)
