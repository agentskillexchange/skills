---
title: "CircleCI Orb Pipeline Debugger"
description: "Diagnoses CircleCI orb configuration errors and pipeline failures using the CircleCI v2 API. Parses orb YAML schemas, detects version pinning issues, and suggests fixes for executor and job dependency problems."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Debugger

The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/)
