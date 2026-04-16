---
title: "CircleCI Orb Linter"
description: "Validates CircleCI configuration files and custom Orbs using the CircleCI CLI (circleci config validate) and Orb Development Kit. Checks for deprecated images, inefficient caching strategies, and security anti-patterns."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Linter

The CircleCI Orb Linter agent validates CircleCI pipeline configurations and custom Orb definitions using the CircleCI CLI (circleci config validate, circleci orb validate). It performs deep structural analysis of .circleci/config.yml files to identify misconfigurations, deprecated Docker images, and suboptimal workflow definitions.

The agent checks caching strategies by analyzing save_cache and restore_cache key patterns, flagging overly broad or stale cache configurations that waste storage or slow builds. It validates resource class assignments against actual job requirements to optimize compute costs and identifies jobs that could benefit from parallelism or test splitting.

For Orb development, the agent validates Orb source YAML against the CircleCI Orb schema, checks command parameter types, and verifies executor compatibility. It detects security anti-patterns like hardcoded secrets, overly permissive context usage, and missing approval gates for production deployments. Supports config packing for Orb publishing and integration with the CircleCI Insights API for performance-based optimization suggestions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-linter/)
