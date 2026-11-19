---
name: "Turn IDE security scan findings into prioritized backlog tasks with DevoxxGenie"
slug: "turn-ide-security-scan-findings-into-backlog-tasks-with-devoxxgenie"
description: "Use DevoxxGenie Agent Mode to scan current project files and dependencies, interpret findings, and create prioritized Backlog.md tasks for review."
github_stars: 691
verification: "security_reviewed"
source: "https://github.com/devoxx/DevoxxGenieIDEAPlugin"
author: "DevoxxGenie contributors"
publisher_type: "Open Source Project"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "devoxx/DevoxxGenieIDEAPlugin"
  github_stars: 691
---

# Turn IDE security scan findings into prioritized backlog tasks with DevoxxGenie

Use DevoxxGenie Agent Mode to scan current project files and dependencies, interpret findings, and create prioritized Backlog.md tasks for review.

## Prerequisites

IntelliJ IDEA, DevoxxGenie plugin, configured model provider, Gitleaks, OpenGrep (opengrep-cli and pyopengrep), Trivy, Backlog.md workspace

## Installation

Install or set up from the source-backed instructions:

Install DevoxxGenie from https://plugins.jetbrains.com/plugin/24169-devoxxgenie and configure a supported model provider. Install the three scanners using their upstream distribution instructions; Homebrew users can install gitleaks, opengrep and trivy. Enable Security Scanning, test binary paths, and enable Create Spec Tasks from findings for a valid Backlog.md workspace.

- Source: https://github.com/devoxx/DevoxxGenieIDEAPlugin

## Documentation

- https://genie.devoxx.com/docs/features/security-scanning

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-ide-security-scan-findings-into-backlog-tasks-with-devoxxgenie/)
