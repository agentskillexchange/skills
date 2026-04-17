---
title: "Gitea Repository & Pull Request Automation"
description: "Gitea Repository & Pull Request Automation is a tool-anchored skill built around Gitea, the self-hosted Git service maintained by the go-gitea organization. It is designed for agents that need to work against a private forge instead of GitHub: creating repositories, opening or reviewing pull requests, syncing labels and milestones, managing releases, and responding to webhooks from internal development systems. Because Gitea exposes a documented REST API for repositories, issues, pull requests, branches, tags, packages, users, and organizations, it gives agents a concrete surface area for repeatable automation rather than vague UI scripting.\nIn practice, this skill fits jobs like triaging incoming issues, creating pull requests from generated branches, checking CI status before merge, updating release notes, or mirroring repository metadata across internal tooling. It also works well in environments where developers already run Gitea with Actions-compatible CI or package registries and want one automation layer to interact with the whole stack. The upstream project ships Docker installation guidance, API documentation, and an actively maintained release stream, so it passes the intake bar for a real, documented source. Integration points include the Gitea REST API, webhooks, repository settings, token-based authentication, and optional Docker-based deployments for local or remote instances."
verification: security_reviewed
source: "https://github.com/go-gitea/gitea"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "go-gitea/gitea"
  github_stars: 54880
---

# Gitea Repository & Pull Request Automation

Gitea Repository & Pull Request Automation is a tool-anchored skill built around Gitea, the self-hosted Git service maintained by the go-gitea organization. It is designed for agents that need to work against a private forge instead of GitHub: creating repositories, opening or reviewing pull requests, syncing labels and milestones, managing releases, and responding to webhooks from internal development systems. Because Gitea exposes a documented REST API for repositories, issues, pull requests, branches, tags, packages, users, and organizations, it gives agents a concrete surface area for repeatable automation rather than vague UI scripting.
In practice, this skill fits jobs like triaging incoming issues, creating pull requests from generated branches, checking CI status before merge, updating release notes, or mirroring repository metadata across internal tooling. It also works well in environments where developers already run Gitea with Actions-compatible CI or package registries and want one automation layer to interact with the whole stack. The upstream project ships Docker installation guidance, API documentation, and an actively maintained release stream, so it passes the intake bar for a real, documented source. Integration points include the Gitea REST API, webhooks, repository settings, token-based authentication, and optional Docker-based deployments for local or remote instances.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitea-repository-pull-request-automation
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitea-repository-pull-request-automation` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitea-repository-pull-request-automation/)
