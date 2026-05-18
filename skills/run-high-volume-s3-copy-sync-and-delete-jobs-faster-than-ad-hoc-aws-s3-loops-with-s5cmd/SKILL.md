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

Use the upstream install or setup path that matches your environment:
- brew install peak/tap/s5cmd
- conda config --add channels conda-forge
- conda config --set channel_priority strict
- conda install s5cmd

Requirements and caveats from upstream:
- ### Docker
- s5cmd uses official AWS SDK to access S3. SDK requires credentials to sign

Basic usage or getting-started notes:
- ![](./doc/usage.png)
- Command file support to run commands in batches at very high execution speeds
- Dry run support

- Source: https://github.com/peak/s5cmd
- Extracted from upstream docs: https://raw.githubusercontent.com/peak/s5cmd/HEAD/README.md

## Documentation

- https://github.com/peak/s5cmd

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-high-volume-s3-copy-sync-and-delete-jobs-faster-than-ad-hoc-aws-s3-loops-with-s5cmd/)
