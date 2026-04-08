---
title: CircleCI Orb Configuration Manager
description: The CircleCI Orb Configuration Manager skill generates and maintains
  .circleci/config.yml files using the CircleCI 2.1 configuration specification. It
  integrates certified orbs including circleci/node@5, circleci/docker@2, circleci/aws-s3@4,
  circleci/slack@4, and circleci/browser-tools@1 to streamline pipeline setup. The
  skill configures job executors (Docker, machine, macOS, Windows), sets resource
  classes (small, medium, large, xlarge, 2xlarge) for cost optimization, and manages
  workspace persistence using persist_to_workspace and attach_workspace steps. It
  supports test splitting with circleci tests split –split-by=timings for parallel
  execution across containers. Advanced features include pipeline parameter definition
  using the parameters key, conditional workflow execution with when/unless clauses,
  scheduled workflow triggers via cron expressions, and dynamic configuration using
  the continuation orb (circleci/continuation@1). The manager also handles SSH key
  management for deployment, Docker layer caching (DLC) configuration, and custom
  orb development using the circleci CLI (circleci orb init, circleci orb publish).
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-configuration-manager/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---

# CircleCI Orb Configuration Manager

The CircleCI Orb Configuration Manager skill generates and maintains .circleci/config.yml files using the CircleCI 2.1 configuration specification. It integrates certified orbs including circleci/node@5, circleci/docker@2, circleci/aws-s3@4, circleci/slack@4, and circleci/browser-tools@1 to streamline pipeline setup. The skill configures job executors (Docker, machine, macOS, Windows), sets resource classes (small, medium, large, xlarge, 2xlarge) for cost optimization, and manages workspace persistence using persist_to_workspace and attach_workspace steps. It supports test splitting with circleci tests split –split-by=timings for parallel execution across containers. Advanced features include pipeline parameter definition using the parameters key, conditional workflow execution with when/unless clauses, scheduled workflow triggers via cron expressions, and dynamic configuration using the continuation orb (circleci/continuation@1). The manager also handles SSH key management for deployment, Docker layer caching (DLC) configuration, and custom orb development using the circleci CLI (circleci orb init, circleci orb publish).

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-configuration-manager/)
