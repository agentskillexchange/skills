---
title: "Woodpecker CI Self-Hosted Continuous Integration Engine"
description: "Woodpecker CI is a simple, lightweight, and extensible continuous integration and continuous delivery engine. Written in Go, it provides a self-hosted alternative to cloud CI services with minimal resource requirements — approximately 100 MB RAM for the server and 30 MB for each agent at idle.\nPipeline Configuration\nWoodpecker pipelines are defined in YAML configuration files stored in the repository. Pipelines consist of steps that run in containers, with each step specifying an image, commands, and environment variables. The system supports multi-pipeline configurations, matrix builds, conditional execution, and pipeline dependencies. Secrets management is built in for handling credentials securely.\nArchitecture\nWoodpecker uses a server-agent architecture. The server handles the web UI, API, webhook processing, and pipeline scheduling. Agents connect to the server and execute pipeline steps in isolated containers. This separation allows scaling by adding more agents to handle increased build load. The server uses SQLite by default but also supports PostgreSQL and MySQL.\nPlugin Ecosystem\nWoodpecker supports plugins that run as container images, making it easy to extend functionality. The plugin ecosystem includes integrations for Docker image building and pushing, Helm chart deployment, S3 uploads, Slack notifications, and many more. Custom plugins can be built as simple Docker containers that read configuration from environment variables.\nGit Forge Integration\nWoodpecker integrates with multiple Git forges including GitHub, GitLab, Gitea, Forgejo, and Bitbucket. It receives webhook events for push, pull request, and tag events to trigger pipelines automatically. Woodpecker is notably the primary CI engine powering Codeberg, one of the largest alternative Git hosting platforms.\nAgent Integration\nAI agents can use Woodpecker for automated build, test, and deployment workflows. The REST API allows programmatic management of repositories, pipelines, secrets, and build logs. Agents can trigger builds, monitor pipeline status, retrieve logs, and manage configuration through the API.\nInstallation\nWoodpecker can be installed via Docker, Docker Compose, Kubernetes Helm charts, or binary releases. The recommended setup uses Docker Compose with a server container and one or more agent containers. The project is Apache 2.0 licensed with over 6,700 GitHub stars and active daily development."
verification: security_reviewed
source: "https://github.com/woodpecker-ci/woodpecker"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "woodpecker-ci/woodpecker"
  github_stars: 6760
---

# Woodpecker CI Self-Hosted Continuous Integration Engine

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/woodpecker-ci-self-hosted-continuous-integration
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/woodpecker-ci-self-hosted-continuous-integration` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woodpecker-ci-self-hosted-continuous-integration/)
