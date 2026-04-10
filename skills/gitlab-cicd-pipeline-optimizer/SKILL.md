---
name: GitLab CI/CD Pipeline Optimizer
description: Optimizes GitLab CI/CD pipelines using the .gitlab-ci.yml specification
  and GitLab API v4. Implements DAG pipelines, parallel testing, and dynamic child
  pipelines.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-cicd-pipeline-optimizer/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---
# GitLab CI/CD Pipeline Optimizer

The GitLab CI/CD Pipeline Optimizer analyzes and improves GitLab CI/CD configurations using the .gitlab-ci.yml specification and GitLab REST API v4 (/api/v4/projects/{id}/pipelines, /jobs, /bridges). It restructures pipeline stages for maximum parallelism and minimum execution time.
The agent implements Directed Acyclic Graph (DAG) pipelines using the needs keyword to break sequential stage dependencies. It configures parallel keyword for test splitting, rules-based job inclusion for merge request pipelines, and extends/include for DRY configuration across projects.
Dynamic child pipelines are generated using trigger:include for monorepo workflows, with parent-child pipeline communication via dotenv artifacts. The agent optimizes Docker layer caching through kaniko builds and GitLab Container Registry integration.
Advanced features include Auto DevOps customization, review app configuration with dynamic environments, and pipeline efficiency metrics tracking. The agent monitors pipeline analytics via the API and suggests optimizations based on job duration trends, failure rates, and resource utilization patterns.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-cicd-pipeline-optimizer/)
