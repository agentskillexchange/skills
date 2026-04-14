---
title: "Build and debug interactive WordPress frontends with data-wp directives"
description: "This skill helps an agent create or troubleshoot WordPress Interactivity API behavior, from store wiring to server-rendered state and hydration checks. Use it when a block, theme, or plugin needs directive-driven interactivity rather than ad hoc frontend glue."
verification: security_reviewed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api"
category:
  - "WordPress &amp; CMS"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives/)
