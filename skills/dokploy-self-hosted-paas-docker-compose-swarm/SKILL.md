---
name: "Dokploy Open Source Self-Hosted PaaS with Docker Compose and Swarm Support"
description: "Dokploy is a free, self-hostable Platform as a Service that simplifies deploying and managing applications and databases. It supports Docker Compose natively, multi-node scaling with Docker Swarm, automated backups, and 280+ one-click templates with "
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Dokploy/dokploy"
---

# Dokploy Open Source Self-Hosted PaaS with Docker Compose and Swarm Support

Dokploy is a free, self-hostable Platform as a Service that simplifies deploying and managing applications and databases. It supports Docker Compose natively, multi-node scaling with Docker Swarm, automated backups, and 280+ one-click templates with Traefik integration.

## Overview

Dokploy is a free, open-source, self-hostable Platform as a Service (PaaS) that simplifies the deployment and management of applications and databases on your own infrastructure. It positions itself as a modern alternative to Vercel, Netlify, and Heroku, with a focus on Docker Compose native support and multi-node orchestration via Docker Swarm.

## Application Deployment

Dokploy supports deploying any application type including Node.js, PHP, Python, Go, and Ruby. It provides multiple build strategies: Nixpacks for automatic detection, Dockerfile-based builds, and Heroku Buildpacks. Git integration supports GitHub, GitLab, Bitbucket, and custom Git repositories with automatic deployments on push.

## Docker Compose Native Support

Unlike many PaaS alternatives, Dokploy provides first-class Docker Compose support, allowing you to deploy complex multi-container applications defined in `docker-compose.yml` files directly. This makes migrating existing Docker Compose setups straightforward without rewriting configuration.

## Database Management

Create and manage databases with support for MySQL, PostgreSQL, MongoDB, MariaDB, libSQL, and Redis. Automated backups can be configured to external S3-compatible storage destinations with customizable schedules and retention policies.

## Multi-Node Scaling

Dokploy uses Docker Swarm to scale applications across multiple nodes. You can add remote servers to your cluster and distribute workloads across them. The built-in Traefik integration automatically handles routing, load balancing, and SSL certificate management across the cluster.

## Monitoring and Notifications

Real-time monitoring tracks CPU, memory, storage, and network usage for every deployed resource. Deployment notifications can be sent via Slack, Discord, Telegram, and email to keep teams informed of success or failure events.

## CLI and API

Dokploy provides both a CLI and REST API for managing applications and databases programmatically. AI agents can use the API to trigger deployments, check service status, manage environment variables, and orchestrate multi-service deployments as part of automated workflows.

## Installation

Install with a single command: `curl -sSL https://dokploy.com/install.sh | sh`. Requires a Linux server with root access. The dashboard is accessible via web browser after installation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dokploy-self-hosted-paas-docker-compose-swarm
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dokploy-self-hosted-paas-docker-compose-swarm -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dokploy-self-hosted-paas-docker-compose-swarm -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dokploy-self-hosted-paas-docker-compose-swarm -a codex
```

### OpenClaw

```bash
clawhub install dokploy-self-hosted-paas-docker-compose-swarm
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dokploy-self-hosted-paas-docker-compose-swarm/)