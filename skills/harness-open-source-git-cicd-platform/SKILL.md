---
title: "Harness Open Source Self-Hosted Git and CI/CD Development Platform"
description: "Harness Open Source (formerly Gitness) is an end-to-end developer platform that integrates Git repository hosting, CI/CD pipelines, hosted development environments, and artifact registries in a single self-hosted binary."
slug: "harness-open-source-git-cicd-platform"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/harness/harness"
listed: true
---

# Harness Open Source Self-Hosted Git and CI/CD Development Platform

Harness Open Source (formerly Gitness) is an end-to-end developer platform that integrates Git repository hosting, CI/CD pipelines, hosted development environments, and artifact registries in a single self-hosted binary.

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
clawhub install harness-open-source-git-cicd-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Harness Open Source, originally launched as Gitness, is an open-source developer platform built by Harness that combines source code management, CI/CD pipelines, hosted development environments (Gitspaces), and artifact registries into one self-hosted solution. It represents the next generation of Drone CI, expanding from continuous integration into a full development lifecycle platform.
Architecture and Deployment
Harness Open Source ships as a single Docker container. Getting started requires one command: docker run -d -p 3000:3000 -p 3022:3022 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/harness:/data --name harness --restart always harness/harness. The platform is accessible at localhost:3000 immediately after launch. Data is stored in a volume for persistence.
Source Code Management
The built-in Git server supports repository hosting with pull requests, code review, branch protection rules, and webhooks. Automated migration tools allow importing repositories and pipelines from GitHub, GitLab, and Bitbucket with minimal effort. SSH access is available on port 3022 for Git operations.
CI/CD Pipelines
Pipeline execution in Harness Open Source is designed for speed, claiming 4x faster execution compared to traditional CI systems. Pipelines are defined in YAML and support Docker-based steps, parallelism, caching, and template reuse. The pipeline engine inherits Drone CI’s battle-tested architecture while adding new capabilities around orchestration and artifact management.
Development Environments
Gitspaces provide on-demand, cloud-based development environments that spin up pre-configured workspaces for any repository. These environments come ready with the project’s dependencies and tooling, reducing onboarding time for new contributors.
Agent Integration
AI agents can interact with Harness Open Source through its REST API for repository management, pipeline triggering, and artifact queries. The platform’s API-first design makes it suitable for automated workflows where agents need to create repositories, manage branches, trigger builds, and monitor pipeline status programmatically.
Migration from Drone
While Harness Open Source is the successor to Drone, the Drone codebase is maintained as a feature branch for teams that need standalone CI. The goal is eventual feature parity, allowing teams to transition from Drone to Harness Open Source at their own pace.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/harness-open-source-git-cicd-platform/)
