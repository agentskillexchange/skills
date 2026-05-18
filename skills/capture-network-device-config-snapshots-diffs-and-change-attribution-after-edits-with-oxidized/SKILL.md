---
name: "Capture network device config snapshots diffs and change attribution after edits with Oxidized"
slug: "capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized"
description: "Pull running configs from routers and switches on a schedule or after change events so you can diff drift, audit edits, and recover known-good state."
github_stars: 3350
verification: "listed"
source: "https://github.com/ytti/oxidized"
author: "ytti"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ytti/oxidized"
  github_stars: 3350
---

# Capture network device config snapshots diffs and change attribution after edits with Oxidized

Pull running configs from routers and switches on a schedule or after change events so you can diff drift, audit edits, and recover known-good state.

## Prerequisites

Oxidized, network device access credentials, supported source inventory, and storage/output backend such as Git or files

## Installation

Use the upstream install or setup path that matches your environment:
- gem install oxidized
- gem install oxidized-web # Web interface and rest API
- gem install oxidized-script # Script-based input/output extensions
- git clone https://github.com/ytti/oxidized.git

Requirements and caveats from upstream:
- Restful API to a move node immediately to head-of-queue (GET/PUT /node/next/[NODE])
- Restful API to fetch configurations (/node/fetch/[NODE] or /node/fetch/group/[NODE])
- Restful API to show list of version for a node (/node/version[NODE]) and diffs

Basic usage or getting-started notes:
- Syslog udp+file example to catch config change events (IOS/JunOS) and trigger a config fetch
- ### Debian and Ubuntu
- Debian 12 "bookworm" or newer and Ubuntu 22.04 (Jammy Jellyfish) or newer are recommended. On Ubuntu, begin by enabling the universe

- Source: https://github.com/ytti/oxidized
- Extracted from upstream docs: https://raw.githubusercontent.com/ytti/oxidized/HEAD/README.md

## Documentation

- https://github.com/ytti/oxidized

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized/)
