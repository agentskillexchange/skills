---
title: "Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review"
description: "This skill is for repositories that want a dedicated security-focused AI review pass inside GitHub Actions. It covers the workflow of triggering on trusted pull requests, scanning only the changed code, tuning false-positive filtering, and posting findings back to the pull request for human review. Invoke this instead of using Claude Code manually when you need a repeatable, CI-native security checkpoint rather than an informal one-off review. It fits best when maintainers want security findings attached to the PR discussion and governed by normal merge policy. The scope boundary is tight: this is not a general Claude Code listing and not a generic SAST product card. It is specifically the GitHub Action workflow for AI-assisted security review of pull request diffs."
source: "https://github.com/anthropics/claude-code-security-review"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-security-review"
  github_stars: 4304
---

# Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review

This skill is for repositories that want a dedicated security-focused AI review pass inside GitHub Actions. It covers the workflow of triggering on trusted pull requests, scanning only the changed code, tuning false-positive filtering, and posting findings back to the pull request for human review. Invoke this instead of using Claude Code manually when you need a repeatable, CI-native security checkpoint rather than an informal one-off review. It fits best when maintainers want security findings attached to the PR discussion and governed by normal merge policy. The scope boundary is tight: this is not a general Claude Code listing and not a generic SAST product card. It is specifically the GitHub Action workflow for AI-assisted security review of pull request diffs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review/)
