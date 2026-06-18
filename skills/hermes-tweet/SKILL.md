---
name: "Hermes Tweet"
slug: "hermes-tweet"
description: "Use Hermes Tweet when Hermes Agent needs a native X/Twitter plugin for reading posts, exploring public data, and running explicitly gated tweet actions through Xquik."
github_stars: 10
verification: "listed"
source: "https://github.com/Xquik-dev/hermes-tweet"
author: "Xquik-dev"
publisher_type: "tool_vendor"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Xquik-dev/hermes-tweet"
  github_stars: 10
---

# Hermes Tweet

Hermes Tweet packages X/Twitter automation as a native Hermes Agent plugin backed by the public Xquik integration surface. Use it when a Hermes workflow needs X search, profile lookup, timeline reads, post inspection, or tweet actions without hand-rolling tool definitions. The plugin separates read-only exploration from write-capable actions, keeps tweet actions behind an explicit enablement gate, and prompts for the required `XQUIK_API_KEY` instead of embedding credentials in skill text or source files. It is best suited for agents that need repeatable social research, launch monitoring, account context, or controlled publishing workflows from Hermes Agent while preserving clear operator intent before any action that can affect an X account.

The upstream repository includes the Hermes plugin manifest, Python handlers, a bundled Hermes skill, validation tests, package metadata, and public safety checks. Treat the bundled upstream skill as the source of truth for runtime-specific instructions, and use this Agent Skill Exchange entry as the discovery and install pointer for agent catalogs.

## Installation

### Hermes Agent

Install from the upstream Hermes Tweet repository and follow the plugin README for current Hermes Agent setup:

```bash
git clone https://github.com/Xquik-dev/hermes-tweet.git
cd hermes-tweet
uv sync --extra dev
```

Configure `XQUIK_API_KEY` in the Hermes Agent environment. Enable tweet actions only when the workflow intentionally needs write access and the operator has confirmed the target account and action.

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
mkdir -p ~/.agent-skills
cp -R skills/hermes-tweet ~/.agent-skills/hermes-tweet
```

## Source

- [Hermes Tweet](https://github.com/Xquik-dev/hermes-tweet)
- [Bundled Hermes Tweet skill](https://github.com/Xquik-dev/hermes-tweet/blob/master/skills/hermes-tweet/SKILL.md)
