---
title: "Dokploy Self-Hosted Application Deployment Platform"
description: "Dokploy is an open source deployment platform for running applications, databases, and Docker Compose stacks on your own servers. The upstream project is maintained at github.com/Dokploy/dokploy, with official documentation at docs.dokploy.com. It is designed for teams that want a Heroku, Vercel, or Netlify style workflow without giving up control of their VPS, Docker host, or swarm environment.\nThis skill is a good fit when an agent needs to help with self-hosted deployment work that has a concrete operational target. That includes installing Dokploy on a fresh VPS, setting up the control plane, deploying a Git-based application, configuring environment variables and domains, attaching persistent volumes, and working with Dokploy’s built-in support for Docker Compose, databases, backups, and Traefik-based routing. It also applies when an agent needs to troubleshoot port conflicts on 80, 443, or 3000, or reason about whether a target service belongs in a single-container deployment, a compose stack, or a multi-node setup.\nIntegration points are practical and specific. Agents can use Dokploy’s documented installation flow, its Git and container deployment model, and its template-driven app provisioning to create repeatable deployment runbooks. The docs also describe manual installation paths and environment variable overrides for pinning stable, canary, or explicit versions. Because the project is active, widely starred, and backed by a real documentation set, it clears the intake bar for verified metadata publication and gives ASE users a credible source-backed option for self-hosted application delivery workflows."
verification: security_reviewed
source: "https://github.com/Dokploy/dokploy"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Dokploy/dokploy"
  github_stars: 32998
---

# Dokploy Self-Hosted Application Deployment Platform

Dokploy is an open source deployment platform for running applications, databases, and Docker Compose stacks on your own servers. The upstream project is maintained at github.com/Dokploy/dokploy, with official documentation at docs.dokploy.com. It is designed for teams that want a Heroku, Vercel, or Netlify style workflow without giving up control of their VPS, Docker host, or swarm environment.
This skill is a good fit when an agent needs to help with self-hosted deployment work that has a concrete operational target. That includes installing Dokploy on a fresh VPS, setting up the control plane, deploying a Git-based application, configuring environment variables and domains, attaching persistent volumes, and working with Dokploy’s built-in support for Docker Compose, databases, backups, and Traefik-based routing. It also applies when an agent needs to troubleshoot port conflicts on 80, 443, or 3000, or reason about whether a target service belongs in a single-container deployment, a compose stack, or a multi-node setup.
Integration points are practical and specific. Agents can use Dokploy’s documented installation flow, its Git and container deployment model, and its template-driven app provisioning to create repeatable deployment runbooks. The docs also describe manual installation paths and environment variable overrides for pinning stable, canary, or explicit versions. Because the project is active, widely starred, and backed by a real documentation set, it clears the intake bar for verified metadata publication and gives ASE users a credible source-backed option for self-hosted application delivery workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dokploy-self-hosted-application-deployment-platform
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dokploy-self-hosted-application-deployment-platform` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dokploy-self-hosted-application-deployment-platform/)
