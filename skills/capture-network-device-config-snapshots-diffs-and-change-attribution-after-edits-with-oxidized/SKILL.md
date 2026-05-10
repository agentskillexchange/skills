---
title: "Capture network device config snapshots diffs and change attribution after edits with Oxidized"
slug: "capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized"
description: "Pull running configs from routers and switches on a schedule or after change events so you can diff drift, audit edits, and recover known-good state."
github_stars: 3350
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Oxidized from the upstream package, gem, container, or source instructions, configure the device source and output backend, then run scheduled or event-triggered config fetches against the target network fleet.
```

## Documentation

- https://github.com/ytti/oxidized

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-network-device-config-snapshots-diffs-and-change-attribution-after-edits-with-oxidized/)
