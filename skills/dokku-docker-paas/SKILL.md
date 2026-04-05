---
name: "Dokku Docker-Powered Mini-Heroku Self-Hosted PaaS"
description: "Dokku is a self-hosted Platform-as-a-Service built on Docker that provides Heroku-like git-push deployment on your own infrastructure. With 32,000+ GitHub stars, it supports buildpacks, Dockerfiles, custom domains, SSL via Let’s Encrypt, and a rich plugin ecosystem for databases, caching, and storage."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/dokku/dokku"
---
# Dokku Docker-Powered Mini-Heroku Self-Hosted PaaS

Dokku is a self-hosted Platform-as-a-Service built on Docker that provides Heroku-like git-push deployment on your own infrastructure. With 32,000+ GitHub stars, it supports buildpacks, Dockerfiles, custom domains, SSL via Let’s Encrypt, and a rich plugin ecosystem for databases, caching, and storage.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dokku-docker-paas
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dokku-docker-paas -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dokku-docker-paas -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dokku-docker-paas -a codex
```

### OpenClaw

```bash
clawhub install dokku-docker-paas
```

## Details

Dokku bills itself as “the smallest PaaS implementation you’ve ever seen” — a Docker-powered mini-Heroku that lets you deploy applications with a simple git push. With over 31,900 GitHub stars, an MIT license, and commits as recent as today, Dokku remains one of the most actively maintained self-hosted PaaS solutions available.

What It Does
Dokku turns any Ubuntu or Debian server into a complete application hosting platform. Push your code via git, and Dokku automatically builds it (using Cloud Native Buildpacks or Dockerfiles), provisions a container, configures networking, and routes traffic to it. It handles zero-downtime deploys, environment variable management, process scaling, and log streaming out of the box.

Key Features
Dokku supports Heroku buildpacks and Dockerfiles for builds, custom domain mapping with automatic SSL via Let’s Encrypt, persistent storage volumes, cron job scheduling, and HTTP/HTTPS routing with Nginx or Caddy. The plugin system extends Dokku with official plugins for PostgreSQL, MySQL, Redis, MongoDB, RabbitMQ, Elasticsearch, and more — each provisioned as isolated Docker containers.

How Agents Use It
AI agents managing deployment workflows benefit from Dokku’s CLI-driven architecture. Every operation — creating apps, setting config vars, scaling processes, managing domains, provisioning databases — is a single shell command. Agents can automate the full deployment lifecycle: dokku apps:create myapp, dokku postgres:create mydb, dokku postgres:link mydb myapp, dokku domains:add myapp example.com, dokku letsencrypt:enable myapp. The predictable command structure makes it ideal for agent-driven infrastructure automation.

Integration Points
Dokku integrates with GitHub Actions and GitLab CI for automated deployments. It supports Docker registries for image-based deploys, Webhooks for notification pipelines, and the Dokku HTTP API for programmatic control. The SSH-based deployment model works with any git client, and the CLI can be invoked remotely via SSH for agents running on separate machines.

Installation
On a fresh Ubuntu 22.04 or 24.04 server: wget -NP . https://dokku.com/install/v0.37.7/bootstrap.sh && sudo DOKKU_TAG=v0.37.7 bash bootstrap.sh. Then configure your domain with dokku domains:set-global your-domain.com and add your SSH key with dokku ssh-keys:add admin path/to/key.pub.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dokku-docker-paas/)
