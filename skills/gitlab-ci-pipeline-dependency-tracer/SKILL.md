---
title: "GitLab CI Pipeline Dependency Tracer"
description: "Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Dependency Tracer

This skill uses the GitLab REST API (gitlab.com/api/v4) to fetch pipeline definitions and job dependency metadata. It builds a directed acyclic graph (DAG) of job relationships using the needs keyword and identifies critical path bottlenecks that force serialization. The skill calls the GitLab Pipelines API to pull historical duration data across branches and computes median stage latency. When bottlenecks are detected, it generates refactored .gitlab-ci.yml snippets with corrected needs declarations. Integration with the GitLab Merge Requests API enables automatic posting of a structured optimization report as an MR comment, including a Mermaid diagram of the corrected pipeline graph. Compatible with GitLab SaaS, self-managed, and GitLab Dedicated.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/)
