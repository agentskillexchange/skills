---
title: "SonarQube Quality Gate Explainer"
description: "Fetches the latest SonarQube project analysis result, explains why the Quality Gate failed in plain English, and links to specific issues. Covers coverage drops, new bugs, and security hotspots. Supports SonarQube Server and SonarCloud. Diagnostic only."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
tool_ecosystem:
  github_repo: "SonarSource/sonarqube"
  github_stars: 10426
---

# SonarQube Quality Gate Explainer

Fetches the latest SonarQube project analysis result, explains why the Quality Gate failed in plain English, and links to specific issues. Covers coverage drops, new bugs, and security hotspots. Supports SonarQube Server and SonarCloud. Diagnostic only.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-explainer/)
