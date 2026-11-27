---
name: "Audit Codebases with OpenCode Swarm Coverage Ledgers and Validated Findings"
slug: "audit-codebases-with-opencode-swarm-coverage-ledgers"
description: "Run the portable codebase-review-swarm skill to produce source-grounded findings, validation evidence and explicit coverage records without editing source."
verification: "security_reviewed"
source: "https://github.com/ZaxbyHub/opencode-swarm/tree/7fb699debb40e60005e8952e2914e95a3de36647/.opencode/skills/codebase-review-swarm"
author: "ZaxbyHub"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
---

# Audit Codebases with OpenCode Swarm Coverage Ledgers and Validated Findings

Run the portable codebase-review-swarm skill to produce source-grounded findings, validation evidence and explicit coverage records without editing source.

## Prerequisites

Git; Codex, Claude Code or OpenCode supporting local Agent Skills; repository-specific safe validators; Python 3 for optional package helpers

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/ZaxbyHub/opencode-swarm.git and check out 7fb699debb40e60005e8952e2914e95a3de36647 in the new checkout. Set TARGET_REPO to the target repository absolute path. From the clone root run mkdir -p "$TARGET_REPO/.agents/skills" then cp -R .opencode/skills/codebase-review-swarm "$TARGET_REPO/.agents/skills/". For Claude Code substitute .claude/skills for .agents/skills. Copy the full canonical folder, including references, assets and scripts. Invoke $codebase-review-swarm or request the named skill. The full opencode-swarm plugin is not required for this portable installation.

- Source: https://github.com/ZaxbyHub/opencode-swarm/tree/7fb699debb40e60005e8952e2914e95a3de36647/.opencode/skills/codebase-review-swarm

## Documentation

- https://github.com/ZaxbyHub/opencode-swarm/tree/7fb699debb40e60005e8952e2914e95a3de36647/.opencode/skills/codebase-review-swarm/INSTALL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-codebases-with-opencode-swarm-coverage-ledgers/)
