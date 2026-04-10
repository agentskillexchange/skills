---
name: GitLab Pipeline Optimizer
description: Analyzes and optimizes GitLab CI/CD pipelines using the GitLab REST API
  v4 and .gitlab-ci.yml schema. Reduces pipeline duration by identifying bottleneck
  stages, configuring DAG dependencies with needs keyword, and implementing rules-based
  job filtering.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-pipeline-optimizer/
category:
- CI/CD Integrations
framework:
- Claude Agents
---
# GitLab Pipeline Optimizer

The GitLab Pipeline Optimizer skill performs deep analysis of GitLab CI/CD pipeline configurations to reduce build times and resource consumption. It connects to the GitLab REST API v4 endpoints including /projects/:id/pipelines and /projects/:id/jobs to gather historical execution data and identify performance bottlenecks.
The skill parses .gitlab-ci.yml files and restructures them using directed acyclic graph (DAG) execution with the needs keyword, replacing sequential stage-based execution with parallel job graphs. It analyzes job dependency chains and recommends optimal grouping strategies.
Capabilities include configuring rules-based job filtering to skip unnecessary jobs on merge requests vs. default branch pushes, implementing extends and !reference tags for DRY configuration, setting up distributed caching with cache:key:files for package managers (npm, pip, composer), and configuring interruptible jobs with auto-cancel redundant pipelines. The skill also generates pipeline analytics dashboards using the GitLab pipeline analytics API and recommends runner fleet sizing based on job queue metrics from the /runners API endpoint.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-optimizer/)
