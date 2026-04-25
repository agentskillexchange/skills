---
title: "Design and verify LaunchDarkly feature-flag targeting and rollout changes with MCP safety checks"
description: "Inspect a LaunchDarkly flag’s current state, choose the right targeting approach, apply rollout or rule changes through the LaunchDarkly MCP server, and verify the outcome safely."
verification: "security_reviewed"
source: "https://github.com/launchdarkly/ai-tooling/tree/main/skills/feature-flags/launchdarkly-flag-targeting"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "launchdarkly/ai-tooling"
  github_stars: 6
---

# Design and verify LaunchDarkly feature-flag targeting and rollout changes with MCP safety checks

This skill helps an agent make safe, auditable LaunchDarkly targeting changes instead of treating LaunchDarkly as a generic product listing. The agent first reads the current flag state, checks whether the flag is on, reviews existing rules, individual targets, fallthrough behavior, prerequisites, and approval requirements, then chooses the right targeting operation for the requested rollout. It supports toggling flags, percentage rollouts, targeting rules, individual targets, cross-environment config copy, and approval-gated changes.

Use this when a user wants an agent to change who sees a feature flag, roll out a variation by percentage, target specific segments or users, or promote tested targeting from one environment to another. This is the right invocation shape when the user wants the agent to reason about evaluation order, safety checks, approval workflows, and post-change verification instead of clicking around the LaunchDarkly UI manually.

The scope boundary is clear: this is not a generic LaunchDarkly or feature-flag product card. It is a narrowly defined operator workflow for targeting and rollout control through MCP tools, with explicit preflight checks, approval handling, and verification after mutation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/design-and-verify-launchdarkly-feature-flag-targeting-and-rollout-changes-with-mcp-safety-checks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/design-and-verify-launchdarkly-feature-flag-targeting-and-rollout-changes-with-mcp-safety-checks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/design-and-verify-launchdarkly-feature-flag-targeting-and-rollout-changes-with-mcp-safety-checks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/design-and-verify-launchdarkly-feature-flag-targeting-and-rollout-changes-with-mcp-safety-checks/)
