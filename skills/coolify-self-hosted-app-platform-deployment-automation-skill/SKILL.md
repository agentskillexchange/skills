---
name: Coolify Self-Hosted App Platform and Deployment Automation Skill
description: Coolify is an open source self-hosted deployment platform for applications,
  databases, and services. This skill covers installing Coolify, connecting infrastructure
  over SSH, and using it as an operational control plane for repeatable app delivery
  workflows.
verification: security_reviewed
source: https://github.com/coollabsio/coolify
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: coollabsio/coolify
  github_stars: 52773
---
# Coolify Self-Hosted App Platform and Deployment Automation Skill

Coolify is a large, actively maintained open source platform from CoolLabs for self-hosted application deployment. It provides a control plane for deploying apps, databases, static sites, and supporting services onto your own servers through a web interface and automation-friendly operational model. The upstream project has substantial adoption, detailed documentation, and a quick-install path that makes it relevant for real deployment workflows rather than hypothetical experiments.
The practical job to be done is clear: install Coolify on a supported Linux host, connect target infrastructure over SSH, and use it to standardize deployments, environment management, and service lifecycle operations. That makes it useful for teams that want a Heroku-style or PaaS-like experience on their own infrastructure. In an agent context, Coolify can be used as the documented platform behind runbooks for shipping apps, rotating services, or managing supporting databases and containers with less manual shell work.
Technically, the important integration points are SSH-based server access, Docker-backed runtime management, and the installation script published in the official docs. This skill belongs in developer tools because it gives operators a repeatable deployment interface for application delivery, infra hygiene, and service orchestration on self-managed systems.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coolify-self-hosted-app-platform-deployment-automation-skill/)
