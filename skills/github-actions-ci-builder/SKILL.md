---
title: "GitHub Actions CI Builder"
description: "Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions."
slug: "github-actions-ci-builder"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-ci-builder/"
---

# GitHub Actions CI Builder

Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions.

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
clawhub install github-actions-ci-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitHub Actions CI Builder skill creates, validates, and manages CI/CD pipelines through GitHub Actions workflow files and the GitHub REST API. It generates proper workflow YAML syntax with on triggers (push, pull_request, workflow_dispatch, schedule), job definitions with runs-on labels for GitHub-hosted and self-hosted runners, and step configurations using official actions (actions/checkout@v4, actions/setup-node@v4, actions/cache@v4). The skill supports matrix strategy configurations for multi-version testing, reusable workflow definitions with workflow_call triggers and input/output/secret definitions, and composite action authoring in action.yml files. It leverages the Actions REST API (repos/{owner}/{repo}/actions/workflows, actions/runs) for triggering workflow_dispatch events, monitoring run status, downloading artifacts via actions/artifacts, and managing repository secrets through the API with libsodium encryption. Environment protection rules and deployment gates are configurable through the environments API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-ci-builder/)
