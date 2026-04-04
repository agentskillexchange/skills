---
name: "Coolify Self-Hosted PaaS for Application and Database Deployment"
description: "Coolify is an open-source, self-hostable Platform as a Service alternative to Vercel, Heroku, and Netlify. It lets you deploy static sites, databases, full-stack applications, and 280+ one-click services on your own servers with just an SSH connectio"
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/coollabsio/coolify"
---

# Coolify Self-Hosted PaaS for Application and Database Deployment

Coolify is an open-source, self-hostable Platform as a Service alternative to Vercel, Heroku, and Netlify. It lets you deploy static sites, databases, full-stack applications, and 280+ one-click services on your own servers with just an SSH connection.

## Overview

Coolify is an open-source, self-hostable Platform as a Service (PaaS) that provides a complete alternative to cloud platforms like Vercel, Heroku, and Netlify. Built with Laravel and Vue.js, it enables developers and teams to deploy and manage applications, databases, and services on their own infrastructure — whether that is a VPS, bare metal server, or even a Raspberry Pi.

## Core Capabilities

Coolify supports deploying virtually any application type through Git integration with GitHub, GitLab, Bitbucket, and Gitea. It provides automatic SSL certificates via Let’s Encrypt, built-in reverse proxy configuration with Traefik, and zero-downtime deployments. The platform includes native support for Docker and Docker Compose, with Nixpacks and Dockerfiles as build options.

## Database Management

Deploy and manage PostgreSQL, MySQL, MariaDB, MongoDB, Redis, and other databases with automated backups to S3-compatible storage. Each database gets its own isolated container with configurable resources.

## Multi-Server and Team Features

Coolify supports multi-server deployments, allowing you to manage applications across multiple VPS instances from a single dashboard. It includes team management with role-based access, real-time deployment logs, and webhook-based CI/CD integration. Notifications can be sent via Slack, Discord, Telegram, or email on deployment events.

## One-Click Services

The platform offers 280+ one-click service templates including Plausible Analytics, Grafana, Minio, Gitea, and many more popular self-hosted applications. Each template comes pre-configured for production use.

## Installation

Installation requires a single command: `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`. The minimum requirement is a Linux server with SSH access and Docker support. The platform runs on x86_64 and ARM64 architectures.

## Agent Integration

AI coding agents can use Coolify’s REST API to programmatically manage deployments, check application status, trigger rebuilds, and manage environment variables. This makes it suitable for automated deployment pipelines orchestrated by agent workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas-deployment-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas-deployment-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas-deployment-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-paas-deployment-3 -a codex
```

### OpenClaw

```bash
clawhub install coolify-self-hosted-paas-deployment-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coolify-self-hosted-paas-deployment-3/)