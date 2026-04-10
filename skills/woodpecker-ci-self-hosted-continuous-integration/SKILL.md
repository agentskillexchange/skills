---
title: "Woodpecker CI Self-Hosted Continuous Integration Engine"
description: "Woodpecker is a simple yet powerful self-hosted CI/CD engine written in Go with great extensibility. It runs pipelines defined in YAML, supports plugins for extensibility, uses minimal resources, and is the CI engine behind Codeberg."
slug: "woodpecker-ci-self-hosted-continuous-integration"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/woodpecker-ci/woodpecker"
tool_ecosystem:
  github_repo: "woodpecker-ci/woodpecker"
  github_stars: 6760
---

# Woodpecker CI Self-Hosted Continuous Integration Engine

Woodpecker is a simple yet powerful self-hosted CI/CD engine written in Go with great extensibility. It runs pipelines defined in YAML, supports plugins for extensibility, uses minimal resources, and is the CI engine behind Codeberg.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install woodpecker-ci-self-hosted-continuous-integration
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Woodpecker CI is a simple, lightweight, and extensible continuous integration and continuous delivery engine. Written in Go, it provides a self-hosted alternative to cloud CI services with minimal resource requirements — approximately 100 MB RAM for the server and 30 MB for each agent at idle.
Pipeline Configuration
Woodpecker pipelines are defined in YAML configuration files stored in the repository. Pipelines consist of steps that run in containers, with each step specifying an image, commands, and environment variables. The system supports multi-pipeline configurations, matrix builds, conditional execution, and pipeline dependencies. Secrets management is built in for handling credentials securely.
Architecture
Woodpecker uses a server-agent architecture. The server handles the web UI, API, webhook processing, and pipeline scheduling. Agents connect to the server and execute pipeline steps in isolated containers. This separation allows scaling by adding more agents to handle increased build load. The server uses SQLite by default but also supports PostgreSQL and MySQL.
Plugin Ecosystem
Woodpecker supports plugins that run as container images, making it easy to extend functionality. The plugin ecosystem includes integrations for Docker image building and pushing, Helm chart deployment, S3 uploads, Slack notifications, and many more. Custom plugins can be built as simple Docker containers that read configuration from environment variables.
Git Forge Integration
Woodpecker integrates with multiple Git forges including GitHub, GitLab, Gitea, Forgejo, and Bitbucket. It receives webhook events for push, pull request, and tag events to trigger pipelines automatically. Woodpecker is notably the primary CI engine powering Codeberg, one of the largest alternative Git hosting platforms.
Agent Integration
AI agents can use Woodpecker for automated build, test, and deployment workflows. The REST API allows programmatic management of repositories, pipelines, secrets, and build logs. Agents can trigger builds, monitor pipeline status, retrieve logs, and manage configuration through the API.
Installation
Woodpecker can be installed via Docker, Docker Compose, Kubernetes Helm charts, or binary releases. The recommended setup uses Docker Compose with a server container and one or more agent containers. The project is Apache 2.0 licensed with over 6,700 GitHub stars and active daily development.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woodpecker-ci-self-hosted-continuous-integration/)
