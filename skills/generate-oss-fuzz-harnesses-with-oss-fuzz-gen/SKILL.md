---
title: "Generate OSS-Fuzz harnesses with oss-fuzz-gen"
description: "Use LLM-assisted harness generation to expand fuzz coverage for real projects before manual fuzzing work begins."
verification: listed
source: "https://github.com/google/oss-fuzz-gen"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "google/oss-fuzz-gen"
  github_stars: 1384
---

# Generate OSS-Fuzz harnesses with oss-fuzz-gen

Use this skill when an agent needs to bootstrap fuzz targets for a project that would otherwise require manual harness authoring. It is a fit for security-focused engineering work where broader fuzz coverage matters more than starting from scratch by hand.

Invoke it instead of using oss-fuzz-gen as a raw project when the operator task is to generate candidate fuzz harnesses, evaluate whether they compile and exercise useful code paths, and iterate toward targets worth keeping.

This stays skill-shaped because the scope is the harness-generation workflow, not OSS-Fuzz as a platform overall.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen/)
