---
title: "Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall"
description: "Run GitHub Agentic Workflow jobs behind a domain allowlist and optional API-key sidecar instead of giving repository agents broad outbound access."
verification: "listed"
source: "https://github.com/github/gh-aw-firewall"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "github/gh-aw-firewall"
  github_stars: 55
---

# Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall

Use gh-aw-firewall when the job is specifically to harden GitHub Agentic Workflows with network policy before those agents are allowed to operate in CI or automation lanes. It wraps the command in a Docker sandbox, pushes HTTP and HTTPS through an allowlisted proxy, and can keep LLM API keys in a sidecar so they never enter the agent process. The scope boundary is narrow and publishable: this is a GitHub Agentic Workflows firewall workflow, not a generic container platform or broad GitHub product listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall/)
