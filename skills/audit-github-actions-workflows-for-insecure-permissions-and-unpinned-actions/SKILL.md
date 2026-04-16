---
title: "Audit GitHub Actions workflows for insecure permissions and unpinned actions"
description: "This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation."
verification: "security_reviewed"
source: "https://github.com/zizmorcore/zizmor"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4145
---

# Audit GitHub Actions workflows for insecure permissions and unpinned actions

This ASE skill is built around zizmor, the static analysis tool maintained by the zizmor project for GitHub Actions security. The concrete agent job is to inspect workflow YAML, composite actions, and related automation files, then surface high-signal security findings before a workflow change lands. zizmor is good at catching problems that are easy to miss in normal code review, such as excessive GITHUB_TOKEN permissions, unsafe expression handling, template injection paths, confusing refs, and other GitHub Actions specific hazards. That bounded job gives the entry a real operational shape rather than leaving it as a generic framework listing.


Invoke this when an agent is reviewing CI changes, onboarding third-party actions, hardening a repository before enabling new automation, or validating that a generated workflow is safe enough to merge. zizmor can run against explicit workflow files, local repositories, or remote GitHub repositories when a token is available, and it can emit plain diagnostics, JSON, SARIF, or GitHub-oriented output for downstream processing. That makes it a strong fit for pre-merge checks, repository audits, and CI hardening passes.


The scope boundary is clear: this skill is about GitHub Actions workflow security, not generic SAST, dependency auditing, or secret scanning across the whole codebase. Integration points include local repository audits, GitHub Actions pipelines, SARIF-consuming security dashboards, and policy checks that gate workflow changes. If the agent needs to answer “is this workflow safe enough to trust?” before merge, zizmor is the right upstream tool for that narrow job.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
