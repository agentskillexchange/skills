---
title: "GitHub Actions CI Builder"
description: "Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-ci-builder/"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
---

# GitHub Actions CI Builder

The GitHub Actions CI Builder skill creates, validates, and manages CI/CD pipelines through GitHub Actions workflow files and the GitHub REST API. It generates proper workflow YAML syntax with on triggers (push, pull_request, workflow_dispatch, schedule), job definitions with runs-on labels for GitHub-hosted and self-hosted runners, and step configurations using official actions (actions/checkout@v4, actions/setup-node@v4, actions/cache@v4). The skill supports matrix strategy configurations for multi-version testing, reusable workflow definitions with workflow_call triggers and input/output/secret definitions, and composite action authoring in action.yml files. It leverages the Actions REST API (repos/{owner}/{repo}/actions/workflows, actions/runs) for triggering workflow_dispatch events, monitoring run status, downloading artifacts via actions/artifacts, and managing repository secrets through the API with libsodium encryption. Environment protection rules and deployment gates are configurable through the environments API.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-ci-builder/)
