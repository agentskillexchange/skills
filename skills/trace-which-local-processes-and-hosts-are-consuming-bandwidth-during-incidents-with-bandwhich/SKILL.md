---
title: "Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich"
slug: "trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich"
description: "Identify which processes, connections, and remote hosts are actually using bandwidth before you chase the wrong incident hypothesis."
github_stars: 11691
verification: "security_reviewed"
source: "https://github.com/imsnif/bandwhich"
author: "imsnif"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "imsnif/bandwhich"
  github_stars: 11691
---

# Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich

Identify which processes, connections, and remote hosts are actually using bandwidth before you chase the wrong incident hypothesis.

## Prerequisites

bandwhich CLI, network interface access, elevated privileges on Linux

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a prebuilt binary from GitHub Releases or build from source with Cargo. On Linux, follow the upstream least-privilege packet-capture capability guidance before incident use.
```

## Documentation

- https://github.com/imsnif/bandwhich

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich/)
