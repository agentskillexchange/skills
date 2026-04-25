---
title: "Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA"
description: "Use reflective search to improve prompts or text-configured agent components against a real eval set instead of manual prompt tweaking."
verification: "listed"
source: "https://github.com/gepa-ai/gepa"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gepa-ai/gepa"
  github_stars: 3550
  npm_package: "gepa"
  npm_weekly_downloads: 4095897
---

# Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA

Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/)
