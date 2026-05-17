---
name: "Run high-volume S3 copy, sync, and delete jobs faster than ad hoc aws s3 loops with s5cmd"
slug: "run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd"
description: "Execute large parallel object-store operations from command files or shell pipelines when agents need speed and repeatability beyond basic aws s3 loops."
github_stars: 4007
verification: "security_reviewed"
source: "https://github.com/peak/s5cmd"
author: "Peak"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "peak/s5cmd"
  github_stars: 4007
---

# Run high-volume S3 copy, sync, and delete jobs faster than ad hoc aws s3 loops with s5cmd

Execute large parallel object-store operations from command files or shell pipelines when agents need speed and repeatability beyond basic aws s3 loops.

## Prerequisites

s5cmd plus credentials for Amazon S3 or another compatible object store

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the s5cmd binary for your platform, configure standard S3 credentials, then run commands directly or place many operations in a command file and execute them with `s5cmd run`.
```

## Documentation

- https://github.com/peak/s5cmd

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd/)
