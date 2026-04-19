---
title: "Download every archived snapshot of a URL before site migrations, takedowns, or investigations"
description: "Tool: waybackpack by Jeremy Bowers and contributors. This skill is for agents that need to capture historical copies of a web page or file from the Internet Archive&#8217;s Wayback Machine in a repeatable, scriptable way. The upstream tool can list snapshots for a URL, download the full archive into timestamped folders, limit the time range, collapse results, skip duplicates, retry around intermittent errors, and preserve raw archived content. That turns the browsing-oriented Wayback interface into something an agent can actually operate at scale. Invoke this when the task is historical recovery or evidence preservation. Examples include collecting a domain&#8217;s archived homepages before a redesign, preserving a disappearing documentation page before a vendor removes it, building a timeline for a policy or pricing page, or gathering older versions of a resource for migration analysis. In those situations, normal product use is too manual. An agent often needs all snapshots, date filters, deduplication, and a local folder structure that other tools can inspect after the fetch completes. The scope boundary keeps this skill from collapsing into a generic archive.org listing. It is not a broad web crawler, not a website testing framework, and not a content analysis platform. Its job is specific: retrieve the historical Wayback record for a chosen URL or path so a downstream agent can inspect, diff, summarize, or preserve it. Integration points are clear. The downloaded archive can feed diff tools, OCR or text extraction pipelines, legal or policy review workflows, or migration audits. Agents can also use the --list mode first to decide whether the historical coverage is rich enough before downloading the full set."
source: "https://github.com/jsvine/waybackpack"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jsvine/waybackpack"
  github_stars: 3173
---

# Download every archived snapshot of a URL before site migrations, takedowns, or investigations

Tool: waybackpack by Jeremy Bowers and contributors. This skill is for agents that need to capture historical copies of a web page or file from the Internet Archive&#8217;s Wayback Machine in a repeatable, scriptable way. The upstream tool can list snapshots for a URL, download the full archive into timestamped folders, limit the time range, collapse results, skip duplicates, retry around intermittent errors, and preserve raw archived content. That turns the browsing-oriented Wayback interface into something an agent can actually operate at scale. Invoke this when the task is historical recovery or evidence preservation. Examples include collecting a domain&#8217;s archived homepages before a redesign, preserving a disappearing documentation page before a vendor removes it, building a timeline for a policy or pricing page, or gathering older versions of a resource for migration analysis. In those situations, normal product use is too manual. An agent often needs all snapshots, date filters, deduplication, and a local folder structure that other tools can inspect after the fetch completes. The scope boundary keeps this skill from collapsing into a generic archive.org listing. It is not a broad web crawler, not a website testing framework, and not a content analysis platform. Its job is specific: retrieve the historical Wayback record for a chosen URL or path so a downstream agent can inspect, diff, summarize, or preserve it. Integration points are clear. The downloaded archive can feed diff tools, OCR or text extraction pipelines, legal or policy review workflows, or migration audits. Agents can also use the --list mode first to decide whether the historical coverage is rich enough before downloading the full set.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations/)
