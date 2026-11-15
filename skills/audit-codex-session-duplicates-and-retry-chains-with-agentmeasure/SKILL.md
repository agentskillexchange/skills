---
name: "Audit Codex session duplicates and retry chains with AgentMeasure"
slug: "audit-codex-session-duplicates-and-retry-chains-with-agentmeasure"
description: "Inspect supported Codex rollout logs locally for duplicate records, retry amplification, and repeated tool failures, preserving unknown evidence and comparing before-and-after snapshots."
github_stars: 218
verification: "security_reviewed"
source: "https://github.com/roy-tong/AgentMeasure"
author: "roy-tong / AgentMeasure contributors"
publisher_type: "community"
category: "Runbooks & Diagnostics"
framework: "Codex"
tool_ecosystem:
  github_repo: "roy-tong/AgentMeasure"
  github_stars: 218
  npm_package: "@agentmeasure/mcp"
  npm_weekly_downloads: 0
---

# Audit Codex session duplicates and retry chains with AgentMeasure

Inspect supported Codex rollout logs locally for duplicate records, retry amplification, and repeated tool failures, preserving unknown evidence and comparing before-and-after snapshots.

## Prerequisites

Python 3.9+; AgentMeasure Healthcheck CLI; supported local Codex rollout JSONL; user-selected local report directory

## Installation

Install or set up from the source-backed instructions:

Create a Python virtual environment and run python -m pip install agentmeasure==0.7.2. Run agentmeasure demo --no-history, then agentmeasure check --dir /path/to/codex/sessions --json report.json --no-history using the actual chosen directory. Inspect findings and coverage rather than treating exit 0 as clean. Optional before/after snapshots use --save-snapshot before.json and --save-snapshot after.json, followed by agentmeasure compare before.json after.json. Keep reports local; agentmeasure share report.json previews the reduced summary. Supported scope follows the detailed upstream Codex rollout support table, not the broader marketing headline.

- Source: https://github.com/roy-tong/AgentMeasure

## Documentation

- https://github.com/roy-tong/AgentMeasure/blob/main/healthcheck/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-codex-session-duplicates-and-retry-chains-with-agentmeasure/)
