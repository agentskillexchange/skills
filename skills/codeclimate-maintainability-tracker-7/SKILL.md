---
title: "CodeClimate Maintainability Tracker"
description: "Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid."
slug: "codeclimate-maintainability-tracker-7"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/"
listed: true
---

# CodeClimate Maintainability Tracker

Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install codeclimate-maintainability-tracker-7
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CodeClimate Maintainability Tracker skill provides continuous technical debt monitoring by interfacing with the Code Climate v1 API. It fetches repository-level maintainability ratings, file-level complexity scores, and duplication metrics on a scheduled basis. The skill implements churn-complexity analysis by correlating Code Climate issue data with git log frequency, identifying files that are both highly complex and frequently modified — the true maintenance burden. It tracks maintainability grade changes across releases, flagging regressions before they compound. Generates formatted weekly digests with sparkline charts showing metric trends and sends them via SendGrid transactional email API. Supports badge generation for README files showing current maintainability grade. Can create GitHub Issues automatically for files that cross configured complexity thresholds. Integrates with Linear and Jira for technical debt backlog management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/)
