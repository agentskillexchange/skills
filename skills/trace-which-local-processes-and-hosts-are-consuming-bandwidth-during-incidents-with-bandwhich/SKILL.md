---
name: "Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich"
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

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/imsnif/bandwhich.git
- cargo build --release
- cargo install --git https://github.com/cross-rs/cross.git cross

Requirements and caveats from upstream:
- Since bandwhich sniffs network packets, it requires elevated privileges.
- Require privilege escalation every time.

Basic usage or getting-started notes:
- [Usage](#usage)
- ### Downstream packaging status
- For detailed instructions for each platform, see [INSTALL.md](INSTALL.md).

- Source: https://github.com/imsnif/bandwhich
- Extracted from upstream docs: https://raw.githubusercontent.com/imsnif/bandwhich/HEAD/README.md

## Documentation

- https://github.com/imsnif/bandwhich

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich/)
