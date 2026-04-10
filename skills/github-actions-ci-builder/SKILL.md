---
name: GitHub Actions CI Builder
description: Generate and manage GitHub Actions workflow YAML files using the GitHub
  Actions REST API and workflow_dispatch events. Supports matrix builds, reusable
  workflows, and composite actions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-ci-builder/
category:
- CI/CD Integrations
framework:
- Codex
---
# GitHub Actions CI Builder

The GitHub Actions CI Builder skill creates, validates, and manages CI/CD pipelines through GitHub Actions workflow files and the GitHub REST API. It generates proper workflow YAML syntax with on triggers (push, pull_request, workflow_dispatch, schedule), job definitions with runs-on labels for GitHub-hosted and self-hosted runners, and step configurations using official actions (actions/checkout@v4, actions/setup-node@v4, actions/cache@v4). The skill supports matrix strategy configurations for multi-version testing, reusable workflow definitions with workflow_call triggers and input/output/secret definitions, and composite action authoring in action.yml files. It leverages the Actions REST API (repos/{owner}/{repo}/actions/workflows, actions/runs) for triggering workflow_dispatch events, monitoring run status, downloading artifacts via actions/artifacts, and managing repository secrets through the API with libsodium encryption. Environment protection rules and deployment gates are configurable through the environments API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-ci-builder/)
