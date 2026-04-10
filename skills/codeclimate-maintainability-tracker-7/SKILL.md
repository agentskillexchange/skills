---
name: "CodeClimate Maintainability Tracker"
description: "Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
---

# CodeClimate Maintainability Tracker

The CodeClimate Maintainability Tracker skill provides continuous technical debt monitoring by interfacing with the Code Climate v1 API. It fetches repository-level maintainability ratings, file-level complexity scores, and duplication metrics on a scheduled basis. The skill implements churn-complexity analysis by correlating Code Climate issue data with git log frequency, identifying files that are both highly complex and frequently modified — the true maintenance burden. It tracks maintainability grade changes across releases, flagging regressions before they compound. Generates formatted weekly digests with sparkline charts showing metric trends and sends them via SendGrid transactional email API. Supports badge generation for README files showing current maintainability grade. Can create GitHub Issues automatically for files that cross configured complexity thresholds. Integrates with Linear and Jira for technical debt backlog management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/)
