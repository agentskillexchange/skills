---
title: "SonarQube Quality Gate Enforcer"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Quality Gate Enforcer

The SonarQube Quality Gate Enforcer skill integrates SonarQube quality gate enforcement into pull request workflows. It queries the SonarQube Web API measures/component endpoint to fetch real-time quality metrics including code coverage, duplicated lines percentage, cognitive complexity, and security hotspot counts. The skill monitors the ce/task endpoint for analysis completion and evaluates results against configurable quality gate profiles. When violations are detected, it posts detailed PR comments breaking down each failed condition with specific file-level metrics and remediation guidance. Supports multi-language projects with per-language threshold overrides. Can enforce differential quality gates that apply stricter standards to new code versus legacy code. Integrates with GitHub Check Runs API to create blocking status checks. Generates trend reports showing quality metric trajectories across releases. Works with SonarQube Community, Developer, and Enterprise editions.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/)
