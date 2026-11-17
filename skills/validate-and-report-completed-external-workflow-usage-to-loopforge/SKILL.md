---
name: "Validate and report completed external workflow usage to LoopForge"
slug: "validate-and-report-completed-external-workflow-usage-to-loopforge"
description: "Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for safe retries."
github_stars: 2771
verification: "security_reviewed"
source: "https://github.com/Tencent/LoopForge"
author: "Tencent"
publisher_type: "open_source_project"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Tencent/LoopForge"
  github_stars: 2771
  npm_package: "loopforge-cli"
  npm_weekly_downloads: 482
---

# Validate and report completed external workflow usage to LoopForge

Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for safe retries.

## Prerequisites

Python 3, official report-workflow-usage skill directory, complete host-produced usage JSON, configured LoopForge instance and project-scoped ingestion credential

## Installation

Install or set up from the source-backed instructions:

Obtain Tencent/LoopForge from https://github.com/Tencent/LoopForge and load skills/report-workflow-usage with its scripts and references. No Python package dependencies are required. Configure the existing target and host-supplied AGENTFLOW_USAGE_FILE, AGENTFLOW_URL and AGENTFLOW_INSIGHT_TOKEN, then run scripts/report_usage.py --check from the skill directory before the configured reporting step.

- Source: https://github.com/Tencent/LoopForge

## Documentation

- https://github.com/Tencent/LoopForge/blob/main/skills/report-workflow-usage/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-and-report-completed-external-workflow-usage-to-loopforge/)
