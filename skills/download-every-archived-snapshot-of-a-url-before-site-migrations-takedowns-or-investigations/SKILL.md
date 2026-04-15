---
title: "Download every archived snapshot of a URL before site migrations, takedowns, or investigations"
description: "Use waybackpack when an agent needs the full historical record for a URL, not a few clicks through the Wayback Machine UI. The agent can list or download snapshots, constrain by date, deduplicate archives, and preserve evidence locally before a site changes or disappears."
verification: security_reviewed
source: "https://github.com/jsvine/waybackpack"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jsvine/waybackpack"
  github_stars: 3173
---

# Download every archived snapshot of a URL before site migrations, takedowns, or investigations

Tool: waybackpack by Jeremy Bowers and contributors.

This skill is for agents that need to capture historical copies of a web page or file from the Internet Archive’s Wayback Machine in a repeatable, scriptable way. The upstream tool can list snapshots for a URL, download the full archive into timestamped folders, limit the time range, collapse results, skip duplicates, retry around intermittent errors, and preserve raw archived content. That turns the browsing-oriented Wayback interface into something an agent can actually operate at scale.

Invoke this when the task is historical recovery or evidence preservation. Examples include collecting a domain’s archived homepages before a redesign, preserving a disappearing documentation page before a vendor removes it, building a timeline for a policy or pricing page, or gathering older versions of a resource for migration analysis. In those situations, normal product use is too manual. An agent often needs all snapshots, date filters, deduplication, and a local folder structure that other tools can inspect after the fetch completes.

The scope boundary keeps this skill from collapsing into a generic archive.org listing. It is not a broad web crawler, not a website testing framework, and not a content analysis platform. Its job is specific: retrieve the historical Wayback record for a chosen URL or path so a downstream agent can inspect, diff, summarize, or preserve it.

Integration points are clear. The downloaded archive can feed diff tools, OCR or text extraction pipelines, legal or policy review workflows, or migration audits. Agents can also use the --list mode first to decide whether the historical coverage is rich enough before downloading the full set.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations/)
