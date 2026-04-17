---
title: "Build and debug interactive WordPress frontends with data-wp directives"
description: "This entry is based on the wp-interactivity-api skill from the official WordPress/agent-skills repository. The agent behavior is precise: detect existing Interactivity API usage, identify stores and directives, align server-rendered state with client hydration, and debug why interactive markup is inert or inconsistent. That is a concrete job-to-be-done, not a generic description of a frontend API.\nUse this when a user wants an agent to build or repair directive-based WordPress interactivity, especially around data-wp-interactive, data-wp-on--*, data-wp-bind--*, viewScriptModule, or @wordpress/interactivity stores. It is the right skill when a block or theme should stay inside WordPress’s intended interactivity model instead of drifting into improvised SPA patterns or brittle event wiring.\nThe scope boundary matters here. This is not a listing for the WordPress framework, the block editor, or a JavaScript package. The skill tells an agent when to inspect directives, when to define state in PHP, when to verify server-side rendering, and how to chase hydration mismatches or missing module loads. Integration points include block.json, viewScriptModule entries, PHP helpers such as wp_interactivity_state(), directive markup in templates, and downstream end-to-end tests once the interactive path is working again."
verification: security_reviewed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wordpress/agent-skills"
  github_stars: 1219
---

# Build and debug interactive WordPress frontends with data-wp directives

This entry is based on the wp-interactivity-api skill from the official WordPress/agent-skills repository. The agent behavior is precise: detect existing Interactivity API usage, identify stores and directives, align server-rendered state with client hydration, and debug why interactive markup is inert or inconsistent. That is a concrete job-to-be-done, not a generic description of a frontend API.
Use this when a user wants an agent to build or repair directive-based WordPress interactivity, especially around data-wp-interactive, data-wp-on--*, data-wp-bind--*, viewScriptModule, or @wordpress/interactivity stores. It is the right skill when a block or theme should stay inside WordPress’s intended interactivity model instead of drifting into improvised SPA patterns or brittle event wiring.
The scope boundary matters here. This is not a listing for the WordPress framework, the block editor, or a JavaScript package. The skill tells an agent when to inspect directives, when to define state in PHP, when to verify server-side rendering, and how to chase hydration mismatches or missing module loads. Integration points include block.json, viewScriptModule entries, PHP helpers such as wp_interactivity_state(), directive markup in templates, and downstream end-to-end tests once the interactive path is working again.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives/)
