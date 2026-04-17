---
title: "Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA"
description: "Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing."
verification: listed
source: "https://github.com/gepa-ai/gepa"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gepa-ai/gepa"
  github_stars: 3550
  ase_npm_package: "gepa"
  npm_weekly_downloads: 4095897
---

# Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA

Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/)
