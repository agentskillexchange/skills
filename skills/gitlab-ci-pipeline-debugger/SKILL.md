---
title: "GitLab CI Pipeline Debugger"
description: "Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Debugger

The GitLab CI Pipeline Debugger agent provides intelligent troubleshooting for failed GitLab CI/CD pipelines. It connects to your GitLab instance via the REST API v4, fetching pipeline details, job logs, and runner configurations to diagnose build failures quickly and accurately.

When a pipeline fails, the agent parses your .gitlab-ci.yml file to understand the pipeline structure including stages, jobs, dependencies, and rules. It then fetches the specific job logs using the GitLab Jobs API, applying pattern matching to identify common failure modes such as missing dependencies, Docker image pull failures, artifact expiration issues, and runner tag mismatches.

The debugger understands GitLab-specific concepts like DAG dependencies with needs keyword, dynamic child pipelines, merge request pipelines vs branch pipelines, and protected variable scoping. It can trace failures across multi-project pipelines by following trigger relationships. Recommendations include specific .gitlab-ci.yml fixes with line references, runner configuration adjustments, and cache optimization strategies using the GitLab cache API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/)
