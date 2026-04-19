---
title: "Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall"
description: "Use gh-aw-firewall when the job is specifically to harden GitHub Agentic Workflows with network policy before those agents are allowed to operate in CI or automation lanes. It wraps the command in a Docker sandbox, pushes HTTP and HTTPS through an allowlisted proxy, and can keep LLM API keys in a sidecar so they never enter the agent process. The scope boundary is narrow and publishable: this is a GitHub Agentic Workflows firewall workflow, not a generic container platform or broad GitHub product listing."
source: "https://github.com/github/gh-aw-firewall"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "github/gh-aw-firewall"
  github_stars: 55
---

# Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall

Use gh-aw-firewall when the job is specifically to harden GitHub Agentic Workflows with network policy before those agents are allowed to operate in CI or automation lanes. It wraps the command in a Docker sandbox, pushes HTTP and HTTPS through an allowlisted proxy, and can keep LLM API keys in a sidecar so they never enter the agent process. The scope boundary is narrow and publishable: this is a GitHub Agentic Workflows firewall workflow, not a generic container platform or broad GitHub product listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall/)
