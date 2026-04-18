---
title: "Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall"
description: "Run GitHub Agentic Workflow jobs behind a domain allowlist and optional API-key sidecar instead of giving repository agents broad outbound access."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall/)
