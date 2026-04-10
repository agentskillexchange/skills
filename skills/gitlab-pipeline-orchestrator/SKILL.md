---
name: "GitLab Pipeline Orchestrator"
description: "Automates GitLab CI/CD pipeline creation using the GitLab Pipelines API and .gitlab-ci.yml DSL. Manages multi-stage builds with artifact caching via the GitLab Artifacts API and triggers downstream pipelines through bridge jobs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-pipeline-orchestrator/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitLab Pipeline Orchestrator

The GitLab Pipeline Orchestrator skill provides comprehensive automation for GitLab CI/CD workflows. It leverages the GitLab Pipelines API v4 to programmatically create, trigger, and monitor pipeline runs across multiple projects. The skill generates optimized .gitlab-ci.yml configurations with proper stage ordering, dependency management, and parallel job execution. It integrates with the GitLab Artifacts API to configure intelligent caching strategies that reduce build times by up to 60%. Bridge jobs enable cross-project pipeline triggering for monorepo and microservice architectures. The skill supports dynamic child pipelines using the trigger:include pattern, environment-specific deployments with manual approval gates, and auto-scaling runners configuration. It also handles merge request pipelines with detached mode, security scanning integration via GitLab SAST/DAST templates, and deployment freezes during critical periods.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-orchestrator/)
