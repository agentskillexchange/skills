---
title: "Gitea Repository & Pull Request Automation"
description: "Automates repository administration, pull request workflows, issue triage, and release operations against Gitea using its REST API and webhook system. Useful for self-hosted software teams that want GitHub-like automation without leaving their own infrastructure."
verification: "security_reviewed"
source: "https://github.com/go-gitea/gitea"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "go-gitea/gitea"
  github_stars: 54880
  license: "MIT"
---

# Gitea Repository & Pull Request Automation

Gitea Repository & Pull Request Automation is a tool-anchored skill built around Gitea, the self-hosted Git service maintained by the go-gitea organization. It is designed for agents that need to work against a private forge instead of GitHub: creating repositories, opening or reviewing pull requests, syncing labels and milestones, managing releases, and responding to webhooks from internal development systems. Because Gitea exposes a documented REST API for repositories, issues, pull requests, branches, tags, packages, users, and organizations, it gives agents a concrete surface area for repeatable automation rather than vague UI scripting.

In practice, this skill fits jobs like triaging incoming issues, creating pull requests from generated branches, checking CI status before merge, updating release notes, or mirroring repository metadata across internal tooling. It also works well in environments where developers already run Gitea with Actions-compatible CI or package registries and want one automation layer to interact with the whole stack. The upstream project ships Docker installation guidance, API documentation, and an actively maintained release stream, so it passes the intake bar for a real, documented source. Integration points include the Gitea REST API, webhooks, repository settings, token-based authentication, and optional Docker-based deployments for local or remote instances.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitea-repository-pull-request-automation/)
