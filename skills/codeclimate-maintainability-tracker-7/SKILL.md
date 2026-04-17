---
title: "CodeClimate Maintainability Tracker"
description: "Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/"
category:
  - "Code Quality & Review"
framework:
  - "ChatGPT Agents"
---

# CodeClimate Maintainability Tracker

The CodeClimate Maintainability Tracker skill provides continuous technical debt monitoring by interfacing with the Code Climate v1 API. It fetches repository-level maintainability ratings, file-level complexity scores, and duplication metrics on a scheduled basis. The skill implements churn-complexity analysis by correlating Code Climate issue data with git log frequency, identifying files that are both highly complex and frequently modified — the true maintenance burden. It tracks maintainability grade changes across releases, flagging regressions before they compound. Generates formatted weekly digests with sparkline charts showing metric trends and sends them via SendGrid transactional email API. Supports badge generation for README files showing current maintainability grade. Can create GitHub Issues automatically for files that cross configured complexity thresholds. Integrates with Linear and Jira for technical debt backlog management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codeclimate-maintainability-tracker-7
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/codeclimate-maintainability-tracker-7` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/)
