---
name: "Dokploy Open Source Self-Hosted Application Deployment Platform"
description: "Dokploy is a free, self-hostable Platform as a Service that simplifies deploying and managing applications and databases. It supports Docker Compose, multi-node Docker Swarm, automated backups, Traefik integration, and 50+ one-click templates."
category: "Developer Tools"
verification: listed
source: "https://github.com/dokploy/dokploy"
---
# Dokploy Open Source Self-Hosted Application Deployment Platform

Dokploy is a free, self-hostable Platform as a Service that simplifies deploying and managing applications and databases. It supports Docker Compose, multi-node Docker Swarm, automated backups, Traefik integration, and 50+ one-click templates.

## Overview

Dokploy is an open-source, self-hosted deployment platform that serves as a modern alternative to Vercel, Netlify, and Heroku. Written in TypeScript, it provides a clean web UI for managing applications, databases, Docker Compose stacks, and multi-server deployments. With over 32,000 GitHub stars, Dokploy has become one of the fastest-growing self-hosting platforms.

## Key Features

Dokploy supports deploying applications in any language — Node.js, PHP, Python, Go, Ruby, and more. It provides native Docker Compose support for managing complex multi-container applications, automated database backups to external storage (S3-compatible), and built-in support for MySQL, PostgreSQL, MongoDB, MariaDB, libSQL, and Redis. The platform integrates with Traefik for automatic SSL, routing, and load balancing.

## Multi-Node and Swarm Support

Dokploy supports Docker Swarm mode for scaling applications across multiple nodes. You can manage remote servers, distribute workloads, and monitor resource usage across your entire cluster from a single dashboard. Real-time CPU, memory, storage, and network monitoring is built in for every deployed resource.

## Agent Integration Points

Agents can interact with Dokploy through its REST API and CLI to automate deployments, manage environment variables, trigger builds, and monitor application health. The one-line installer (`curl -sSL https://dokploy.com/install.sh | sh`) enables fully automated server provisioning. Notification webhooks support Slack, Discord, Telegram, and email for deployment event automation.

## Templates and One-Click Deploys

Dokploy includes 50+ one-click deployment templates for popular open-source tools including Plausible, PocketBase, Cal.com, Supabase, and many more. This makes it ideal for agents that need to provision infrastructure components as part of larger workflows.

## Installation

Install this skill using one of these methods:

### ClawHub (Recommended)
```bash
clawhub install agentskillexchange/dokploy-self-hosted-deployment
```

### OpenClaw Chat
```
/install agentskillexchange/dokploy-self-hosted-deployment
```

### Manual Download
Download from [Agent Skill Exchange](https://agentskillexchange.com/skills/dokploy-self-hosted-deployment/) and place in your agent's skills directory.

### Git Clone
```bash
git clone https://github.com/agentskillexchange/skills.git
cp -r skills/skills/dokploy-self-hosted-deployment /your/skills/directory/
```

### Direct File
Copy the SKILL.md file from [skills/dokploy-self-hosted-deployment/SKILL.md](https://github.com/agentskillexchange/skills/tree/main/skills/dokploy-self-hosted-deployment/SKILL.md)

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dokploy-self-hosted-deployment/)
- [Upstream Source](https://github.com/dokploy/dokploy)
