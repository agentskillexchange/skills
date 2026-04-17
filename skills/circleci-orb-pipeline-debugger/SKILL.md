---
title: "CircleCI Orb Pipeline Debugger"
description: "The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Debugger

The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-pipeline-debugger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-pipeline-debugger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/)
