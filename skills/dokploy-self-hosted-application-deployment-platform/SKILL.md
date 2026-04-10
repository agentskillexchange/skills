---
name: "Dokploy Self-Hosted Application Deployment Platform"
description: "Deploy and manage Dockerized apps on your own infrastructure with Dokploy, an open source platform positioned as an alternative to Heroku, Vercel, and Netlify. This skill is useful when agents need to stand up services, manage compose stacks, provision databases, and reason about Traefik-backed deployment workflows from real Dokploy docs and project conventions."
verification: security_reviewed
source: "https://github.com/Dokploy/dokploy"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
---

# Dokploy Self-Hosted Application Deployment Platform

Dokploy is an open source deployment platform for running applications, databases, and Docker Compose stacks on your own servers. The upstream project is maintained at github.com/Dokploy/dokploy, with official documentation at docs.dokploy.com. It is designed for teams that want a Heroku, Vercel, or Netlify style workflow without giving up control of their VPS, Docker host, or swarm environment.
This skill is a good fit when an agent needs to help with self-hosted deployment work that has a concrete operational target. That includes installing Dokploy on a fresh VPS, setting up the control plane, deploying a Git-based application, configuring environment variables and domains, attaching persistent volumes, and working with Dokploy's built-in support for Docker Compose, databases, backups, and Traefik-based routing. It also applies when an agent needs to troubleshoot port conflicts on 80, 443, or 3000, or reason about whether a target service belongs in a single-container deployment, a compose stack, or a multi-node setup.
Integration points are practical and specific. Agents can use Dokploy's documented installation flow, its Git and container deployment model, and its template-driven app provisioning to create repeatable deployment runbooks. The docs also describe manual installation paths and environment variable overrides for pinning stable, canary, or explicit versions. Because the project is active, widely starred, and backed by a real documentation set, it clears the intake bar for verified metadata publication and gives ASE users a credible source-backed option for self-hosted application delivery workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dokploy-self-hosted-application-deployment-platform/)
