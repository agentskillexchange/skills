---
title: "Gitea Repository & Pull Request Automation"
description: "Automates repository administration, pull request workflows, issue triage, and release operations against Gitea using its REST API and webhook system. Useful for self-hosted software teams that want GitHub-like automation without leaving their own infrastructure."
verification: security_reviewed
source: "https://github.com/go-gitea/gitea"
category:
  - "Integrations &amp; Connectors"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitea-repository-pull-request-automation/)
