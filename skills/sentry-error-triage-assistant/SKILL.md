---
title: "Sentry Error Triage Assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43576
---

# Sentry Error Triage Assistant

The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration.

This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments.

Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors.

Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
