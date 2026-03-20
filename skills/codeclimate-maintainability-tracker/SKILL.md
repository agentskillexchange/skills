---
name: CodeClimate Maintainability Tracker
description: Tracks CodeClimate maintainability scores over time using the CodeClimate v1 API. Generates trend reports for technical debt, duplication, and complexity metrics.
category: Code Quality & Review
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 9
source: https://agentskillexchange.com/skill/codeclimate-maintainability-tracker/
---

# CodeClimate Maintainability Tracker

Tracks CodeClimate maintainability scores over time using the CodeClimate v1 API. Generates trend reports for technical debt, duplication, and complexity metrics.

## Overview

The CodeClimate Maintainability Tracker agent provides continuous monitoring and trend analysis of code quality metrics from CodeClimate. Using the CodeClimate v1 API, it tracks maintainability grades, technical debt ratios, and issue counts across your repositories over time.
The agent fetches repository snapshots via the CodeClimate Repos API, collecting metrics including maintainability GPA, test coverage percentage, technical debt hours, and issue counts by category (complexity, duplication, style, bug risk). It builds time-series datasets from snapshot history, generating trend reports that highlight improving or degrading quality areas.
For each analysis, the tracker identifies the top contributors to technical debt using the CodeClimate Issues API, ranking files by remediation time and churn frequency. It correlates code quality trends with development activity from the CodeClimate Test Reporter API, showing how coverage changes relate to deployment frequency. Weekly digest reports include maintainability score changes, new critical issues, and recommended refactoring targets prioritized by impact-to-effort ratio.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-tracker
```

### OpenClaw

```bash
openclaw install codeclimate-maintainability-tracker
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Code Quality & Review |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (9 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/codeclimate-maintainability-tracker/)*
