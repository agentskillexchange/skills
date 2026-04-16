---
title: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
verification: "security_reviewed"
source: "https://github.com/pulumi/pulumi"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 25042
  ase_npm_package: "@pulumi/pulumi"
  npm_weekly_downloads: 2073384
  license: "Apache-2.0"
---

# Pulumi Drift Detector & Reconciler

Pulumi Drift Detector & Reconciler is built around Pulumi infrastructure as code platform. The underlying ecosystem is represented by pulumi/pulumi (24,917+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like stacks, preview, refresh, state, providers, config, drift detection and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to pulumi so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources. The implementation typically relies on stacks, preview, refresh, state, providers, config, drift detection, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses stacks, preview, refresh, state, providers, config, drift detection instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as cloud provisioning with TypeScript, Python, Go, C#, and Java.

Key integration points include cloud provisioning with TypeScript, Python, Go, C#, and Java. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
