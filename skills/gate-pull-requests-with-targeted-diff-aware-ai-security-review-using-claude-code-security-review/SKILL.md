---
name: "Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review"
slug: "gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review"
description: "Run a Claude Code powered security review pass on trusted pull requests so suspicious auth, secret, injection, and unsafe logic changes surface before merge."
github_stars: 4304
verification: "listed"
source: "https://github.com/anthropics/claude-code-security-review"
author: "Anthropic"
publisher_type: "organization"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-security-review"
  github_stars: 4304
---

# Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review

Run a Claude Code powered security review pass on trusted pull requests so suspicious auth, secret, injection, and unsafe logic changes surface before merge.

## Prerequisites

GitHub Actions, Claude API access, pull request workflows on trusted repositories

## Installation

Requirements and caveats from upstream:
- ├── requirements.txt # Python dependencies

Basic usage or getting-started notes:
- Add this to your repository's .github/workflows/security.yml:
- yaml
- name: Security Review

- Source: https://github.com/anthropics/claude-code-security-review
- Extracted from upstream docs: https://raw.githubusercontent.com/anthropics/claude-code-security-review/HEAD/README.md

## Documentation

- https://github.com/anthropics/claude-code-security-review

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review/)
