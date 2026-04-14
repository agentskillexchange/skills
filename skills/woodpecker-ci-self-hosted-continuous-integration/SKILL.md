---
title: "Woodpecker CI Self-Hosted Continuous Integration Engine"
description: "Woodpecker is a simple yet powerful self-hosted CI/CD engine written in Go with great extensibility. It runs pipelines defined in YAML, supports plugins for extensibility, uses minimal resources, and is the CI engine behind Codeberg."
verification: security_reviewed
source: "https://github.com/woodpecker-ci/woodpecker"
category:
  - "CI/CD Integrations"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woodpecker-ci-self-hosted-continuous-integration/)
