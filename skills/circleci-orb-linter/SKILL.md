---
title: CircleCI Orb Linter
description: The CircleCI Orb Linter agent validates CircleCI pipeline configurations
  and custom Orb definitions using the CircleCI CLI (circleci config validate, circleci
  orb validate). It performs deep structural analysis of .circleci/config.yml files
  to identify misconfigurations, deprecated Docker images, and suboptimal workflow
  definitions. The agent checks caching strategies by analyzing save_cache and restore_cache
  key patterns, flagging overly broad or stale cache configurations that waste storage
  or slow builds. It validates resource class assignments against actual job requirements
  to optimize compute costs and identifies jobs that could benefit from parallelism
  or test splitting. For Orb development, the agent validates Orb source YAML against
  the CircleCI Orb schema, checks command parameter types, and verifies executor compatibility.
  It detects security anti-patterns like hardcoded secrets, overly permissive context
  usage, and missing approval gates for production deployments. Supports config packing
  for Orb publishing and integration with the CircleCI Insights API for performance-based
  optimization suggestions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-linter/
category:
- CI/CD Integrations
framework:
- Cursor
---

# CircleCI Orb Linter

The CircleCI Orb Linter agent validates CircleCI pipeline configurations and custom Orb definitions using the CircleCI CLI (circleci config validate, circleci orb validate). It performs deep structural analysis of .circleci/config.yml files to identify misconfigurations, deprecated Docker images, and suboptimal workflow definitions. The agent checks caching strategies by analyzing save_cache and restore_cache key patterns, flagging overly broad or stale cache configurations that waste storage or slow builds. It validates resource class assignments against actual job requirements to optimize compute costs and identifies jobs that could benefit from parallelism or test splitting. For Orb development, the agent validates Orb source YAML against the CircleCI Orb schema, checks command parameter types, and verifies executor compatibility. It detects security anti-patterns like hardcoded secrets, overly permissive context usage, and missing approval gates for production deployments. Supports config packing for Orb publishing and integration with the CircleCI Insights API for performance-based optimization suggestions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-linter/)
