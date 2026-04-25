---
title: "Run repeatable Google Ads and SEO audits inside Claude Code with Toprank"
description: "Use Toprank when an agent needs a repeatable Claude Code workflow for Google Ads and SEO audits, with concrete slash commands, account-backed analysis, and optional repo edits instead of one-off marketing prompting."
verification: "security_reviewed"
source: "https://github.com/nowork-studio/toprank"
category:
  - "Content Writing & SEO"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "nowork-studio/toprank"
  github_stars: 466
---

# Run repeatable Google Ads and SEO audits inside Claude Code with Toprank

Tool name: Toprank from nowork-studio/toprank. The upstream README is explicit about the operator workflow: install the Claude Code plugin, invoke commands like /toprank:ads-audit and /toprank:seo-analysis, connect Google Ads and Search Console data, review ranked findings, and optionally apply site fixes when the repository is available. That makes this a bounded agent workflow rather than a generic marketing product card. What the agent does: run account-backed Google Ads and SEO audits, surface wasted spend and ranking problems, prioritize recommended actions, preserve business context between related commands, and in repo-connected cases help ship fixes such as metadata, heading, or structured-data updates. The value is not just access to a dashboard; it is the repeatable audit-and-action loop exposed as Claude Code commands. When to use it: invoke this when the user wants Claude Code to inspect Google Ads efficiency, Search Console performance, and on-site SEO issues through a repeatable command surface instead of ad-hoc chat prompting or manual dashboard hopping. It fits recurring marketing review, campaign triage, and SEO remediation workflows. Scope boundary: this is not a general SEO platform listing, not a generic Google Ads connector, and not a broad Claude Code customization pack. Its boundary is the installable Toprank command workflow for Google Ads and SEO analysis inside Claude Code, with concrete audit commands and bounded remediation behavior.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-repeatable-google-ads-and-seo-audits-inside-claude-code-with-toprank/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-repeatable-google-ads-and-seo-audits-inside-claude-code-with-toprank
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-repeatable-google-ads-and-seo-audits-inside-claude-code-with-toprank`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-repeatable-google-ads-and-seo-audits-inside-claude-code-with-toprank/)
