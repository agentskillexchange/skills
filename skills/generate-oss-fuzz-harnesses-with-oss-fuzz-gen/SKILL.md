---
title: "Generate OSS-Fuzz harnesses with oss-fuzz-gen"
description: "Use LLM-assisted harness generation to expand fuzz coverage for real projects before manual fuzzing work begins."
verification: "listed"
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

Use this skill when an agent needs to bootstrap fuzz targets for a project that would otherwise require manual harness authoring. It is a fit for security-focused engineering work where broader fuzz coverage matters more than starting from scratch by hand. Invoke it instead of using oss-fuzz-gen as a raw project when the operator task is to generate candidate fuzz harnesses, evaluate whether they compile and exercise useful code paths, and iterate toward targets worth keeping. This stays skill-shaped because the scope is the harness-generation workflow, not OSS-Fuzz as a platform overall.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-oss-fuzz-harnesses-with-oss-fuzz-gen/)
