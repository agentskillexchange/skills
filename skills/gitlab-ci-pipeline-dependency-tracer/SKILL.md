---
name: "GitLab CI Pipeline Dependency Tracer"
slug: "gitlab-ci-pipeline-dependency-tracer"
description: "Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments."
github_stars: 24298
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category: "CI/CD Integrations"
framework: "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Dependency Tracer

Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Installation

Basic usage or getting-started notes:
- Please see the [requirements documentation](doc/install/requirements.md) for system requirements and more information about the supported operating systems.
- The recommended way to install GitLab is with the [Omnibus packages](https://docs.gitlab.com/install/package/) on our package server.
- Compared to [a self-compiled installation](https://docs.gitlab.com/install/self_compiled/), this is faster and less error prone.

- Source: https://github.com/gitlabhq/gitlabhq
- Extracted from upstream docs: https://raw.githubusercontent.com/gitlabhq/gitlabhq/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/)
