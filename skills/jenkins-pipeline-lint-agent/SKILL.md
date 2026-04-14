---
title: "Jenkins Pipeline Lint Agent"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter API endpoint. Checks for deprecated step usage, security anti-patterns, and Groovy sandbox violations."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Lint Agent

The Jenkins Pipeline Lint Agent skill submits Jenkinsfile contents to the Jenkins /pipeline-model-converter/validate REST endpoint for server-side syntax validation. Beyond basic linting, it performs static analysis on both declarative and scripted pipeline syntax to detect deprecated step names, insecure credential handling patterns, and Groovy sandbox escape attempts. The skill maintains a knowledge base of Jenkins plugin compatibility matrices, flagging steps that require specific plugin versions. It checks for common anti-patterns like unbounded node blocks, missing timeout wrappers, and improper shared library imports. The agent can process multi-branch pipeline configurations, validating Jenkinsfile variants across branches via the Jenkins Blue Ocean REST API. Results include line-level annotations with fix suggestions, severity ratings, and links to Jenkins documentation for each finding.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/)
