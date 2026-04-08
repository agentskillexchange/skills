---
title: Checkly CLI Monitoring as Code for API and Browser Checks
description: 'Checkly CLI is the official command-line workflow from Checkly for writing
  and deploying synthetic monitoring as code. The upstream repository is checkly/checkly-cli
  , and the official docs describe it as a JavaScript and TypeScript native workflow
  for coding, testing, and deploying monitoring at scale. Its practical job-to-be-done
  is clear: an agent can scaffold monitoring, log into a Checkly account, run checks
  locally, and deploy API checks and browser checks directly from a repository. Because
  the CLI has native @playwright/test support, it fits especially well when a team
  already has browser automation or end-to-end coverage and wants to turn those checks
  into ongoing production monitoring. For ASE, this is a strong source-backed intake
  candidate because the project has an official GitHub repository, public documentation,
  tagged releases through GitHub, a permissive Apache 2.0 license, and recent maintenance
  activity. The docs also give concrete commands for getting started, including npx
  checkly init , npx checkly login , npx checkly test , and npx checkly deploy . That
  means an agent can do more than merely describe the platform, it can guide setup,
  validate checks in CI, and reason about monitoring deployments in a repeatable way.
  Checkly CLI is a good fit for reliability workflows, release verification, synthetic
  smoke tests, and browser journey monitoring where the underlying checks should be
  versioned, reviewed, and shipped like code.'
verification: security_reviewed
source: https://github.com/checkly/checkly-cli
category:
- Monitoring &amp; Alerts
framework:
- Multi-Framework
---

# Checkly CLI Monitoring as Code for API and Browser Checks

Checkly CLI is the official command-line workflow from Checkly for writing and deploying synthetic monitoring as code. The upstream repository is checkly/checkly-cli , and the official docs describe it as a JavaScript and TypeScript native workflow for coding, testing, and deploying monitoring at scale. Its practical job-to-be-done is clear: an agent can scaffold monitoring, log into a Checkly account, run checks locally, and deploy API checks and browser checks directly from a repository. Because the CLI has native @playwright/test support, it fits especially well when a team already has browser automation or end-to-end coverage and wants to turn those checks into ongoing production monitoring. For ASE, this is a strong source-backed intake candidate because the project has an official GitHub repository, public documentation, tagged releases through GitHub, a permissive Apache 2.0 license, and recent maintenance activity. The docs also give concrete commands for getting started, including npx checkly init , npx checkly login , npx checkly test , and npx checkly deploy . That means an agent can do more than merely describe the platform, it can guide setup, validate checks in CI, and reason about monitoring deployments in a repeatable way. Checkly CLI is a good fit for reliability workflows, release verification, synthetic smoke tests, and browser journey monitoring where the underlying checks should be versioned, reviewed, and shipped like code.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkly-cli-monitoring-as-code-for-api-and-browser-checks/)
