---
title: "Configure and interpret LaunchDarkly AI Config online evaluations with judge attachments"
description: "Attach judges to LaunchDarkly AI Config variations, create custom judges, set sampling rates, and interpret production quality signals from online evaluations."
verification: "security_reviewed"
source: "https://github.com/launchdarkly/ai-tooling/tree/main/skills/ai-configs/aiconfig-online-evals"
category:
  - "Monitoring & Alerts"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "launchdarkly/ai-tooling"
  github_stars: 6
---

# Configure and interpret LaunchDarkly AI Config online evaluations with judge attachments

This skill helps an agent set up and reason about LaunchDarkly AI Config online evaluations. The agent can create or attach judge configs, configure sampling rates, enable fallthrough correctly, and interpret quality scores for production variations using LaunchDarkly’s online evaluation model. The workflow is specifically about evaluation plumbing and rollout-quality measurement for AI Configs, not generic prompt experimentation.

Use this when a user is shipping or monitoring LaunchDarkly AI Config changes and wants the agent to wire up online judges, compare evaluation behavior, and catch regressions in production-facing traffic. This is more appropriate than using LaunchDarkly normally when the need is to orchestrate the evaluation setup and explain what those scores mean operationally.

The scope boundary is clear: this is not a plain LaunchDarkly or SDK listing. It is a narrow workflow around online evaluation setup, judge configuration, sampling strategy, and result interpretation for AI Config variations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/configure-and-interpret-launchdarkly-ai-config-online-evaluations-with-judge-attachments/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/configure-and-interpret-launchdarkly-ai-config-online-evaluations-with-judge-attachments
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/configure-and-interpret-launchdarkly-ai-config-online-evaluations-with-judge-attachments`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/configure-and-interpret-launchdarkly-ai-config-online-evaluations-with-judge-attachments/)
