---
name: Storyblok Management API and JavaScript Client
description: Use Storyblok’s Management API and JavaScript client to automate stories,
  components, assets, spaces, and editorial workflows in a headless CMS stack. This
  skill is for agents that need to operate Storyblok as a structured content system
  with schemas, environments, and publish states.
category: "WordPress &amp; CMS"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/storyblok/storyblok-js-client"
tool_ecosystem:
  github_repo: "https://github.com/storyblok/storyblok-js-client"
  github_stars: 137
  license: MIT
---
# Storyblok Management API and JavaScript Client

Use Storyblok’s Management API and JavaScript client to automate stories, components, assets, spaces, and editorial workflows in a headless CMS stack. This skill is for agents that need to operate Storyblok as a structured content system with schemas, environments, and publish states.

Storyblok is a headless CMS with a component-driven content model, and its Management API together with the official JavaScript client gives agents a reliable way to manipulate content programmatically. A skill built around Storyblok is valuable for concrete jobs like creating stories from a template, updating component data at scale, syncing product content, migrating entries between spaces, uploading assets, or enforcing content structure across teams.

The skill would authenticate with the Storyblok Management API, select the target space, inspect components and folder structure, create or update stories, manage assets, and publish or stage changes based on workflow rules. It can return story IDs, slugs, publish status, asset references, validation errors, and normalized JSON that downstream automations can consume. That makes it useful in publishing pipelines, composable commerce stacks, multilingual content operations, and headless website deployments.

Key integration points include Storyblok spaces, stories, components, datasource entries, asset APIs, preview workflows, and the storyblok-js-client package. Technical terms that matter include content blocks, schemas, slug generation, draft versus published state, API tokens, rate limits, and structured field payloads. This keeps the skill tightly anchored to the real Storyblok platform and describes the actual mechanics and outputs an agent would handle when working inside a CMS automation workflow.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill storyblok-management-api-and-javascript-client
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill storyblok-management-api-and-javascript-client -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill storyblok-management-api-and-javascript-client -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill storyblok-management-api-and-javascript-client -a codex
```

### OpenClaw

```bash
clawhub install storyblok-management-api-and-javascript-client
```


## Source

- [GitHub](https://github.com/storyblok/storyblok-js-client)
