---
title: "GitLab CI Pipeline Debugger"
slug: "gitlab-ci-pipeline-debugger"
description: "Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category: "CI/CD Integrations"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Debugger

Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/)
