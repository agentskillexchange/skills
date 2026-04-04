---
name: "Coolify Self-Hosted PaaS for Application and Database Deployment"
description: "Coolify is an open-source, self-hostable Platform as a Service alternative to Heroku, Vercel, and Netlify. It lets you deploy static sites, full-stack applications, databases, and 280+ one-click services on your own servers with just an SSH connection."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/coollabsio/coolify"
---
# Coolify Self-Hosted PaaS for Application and Database Deployment

Coolify is an open-source, self-hostable Platform as a Service alternative to Heroku, Vercel, and Netlify. It lets you deploy static sites, full-stack applications, databases, and 280+ one-click services on your own servers with just an SSH connection.

## Overview

Coolify is an open-source, self-hostable Platform as a Service (PaaS) that provides Heroku-like deployment convenience on your own infrastructure. Built with Laravel and Svelte, it supports deploying virtually any type of application — Node.js, PHP, Python, Go, Ruby, and more — along with managed databases including PostgreSQL, MySQL, MariaDB, MongoDB, and Redis.

## Key Features

Coolify handles the full lifecycle of application deployment and server management. It provides automatic SSL via Let’s Encrypt, Git integration with GitHub, GitLab, Bitbucket, and Gitea for push-to-deploy workflows, Docker and Docker Compose native support, real-time log viewing, and built-in monitoring dashboards. The platform supports multi-server management, allowing you to deploy across multiple VPS instances, bare metal servers, or even Raspberry Pis from a single dashboard.

## Agent Integration Points

Agents can interact with Coolify through its REST API to automate deployments, manage environment variables, trigger rebuilds, check deployment status, and monitor server health. The CLI installer (`curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`) makes initial setup scriptable. Coolify’s webhook support enables agents to react to deployment events, build failures, or health check alerts.

## Use Cases

Self-hosted CI/CD pipeline management, automated application deployment from Git repositories, database provisioning and backup automation, multi-server orchestration for staging and production environments, and one-click deployment of open-source tools like Plausible Analytics, Supabase, and MinIO.

## Technical Details

Coolify requires a Linux server with SSH access and Docker. It runs as a Docker container itself, managing other containers on the host. The platform uses Traefik as its reverse proxy for automatic routing and load balancing. With over 52,000 GitHub stars and active daily commits, Coolify is one of the most popular self-hosting platforms available.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas -a codex
```

### OpenClaw

```bash
clawhub install coolify-self-hosted-paas
```
## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coolify-self-hosted-paas/)
- [Upstream Source](https://github.com/coollabsio/coolify)
