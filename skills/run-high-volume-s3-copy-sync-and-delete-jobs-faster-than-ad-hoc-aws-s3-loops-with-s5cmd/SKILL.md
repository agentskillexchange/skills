---
title: "Run high-volume S3 copy, sync, and delete jobs faster than ad hoc aws s3 loops with s5cmd"
description: "Execute large parallel object-store operations from command files or shell pipelines when agents need speed and repeatability beyond basic aws s3 loops."
verification: "listed"
source: "https://github.com/peak/s5cmd"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "peak/s5cmd"
  github_stars: 4007
---

# Run high-volume S3 copy, sync, and delete jobs faster than ad hoc aws s3 loops with s5cmd

Use s5cmd when an agent needs to perform large batches of S3-compatible copy, sync, list, or delete operations quickly and predictably. Invoke it instead of hand-rolled `aws s3` loops when the job is high-volume object movement or cleanup with parallel execution and reproducible command sets. The scope boundary is tight: batch object-storage operations at scale, not general cloud administration, storage platform hosting, or a generic SDK listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd/)
