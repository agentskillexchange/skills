---
title: "GitHub Actions CI Builder"
description: "Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-ci-builder/"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
---

# GitHub Actions CI Builder

The GitHub Actions CI Builder skill creates, validates, and manages CI/CD pipelines through GitHub Actions workflow files and the GitHub REST API. It generates proper workflow YAML syntax with on triggers (push, pull_request, workflow_dispatch, schedule), job definitions with runs-on labels for GitHub-hosted and self-hosted runners, and step configurations using official actions (actions/checkout@v4, actions/setup-node@v4, actions/cache@v4). The skill supports matrix strategy configurations for multi-version testing, reusable workflow definitions with workflow_call triggers and input/output/secret definitions, and composite action authoring in action.yml files. It leverages the Actions REST API (repos/{owner}/{repo}/actions/workflows, actions/runs) for triggering workflow_dispatch events, monitoring run status, downloading artifacts via actions/artifacts, and managing repository secrets through the API with libsodium encryption. Environment protection rules and deployment gates are configurable through the environments API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-ci-builder/)
