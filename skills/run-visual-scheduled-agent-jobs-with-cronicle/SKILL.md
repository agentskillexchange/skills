---
title: "Run visual scheduled agent jobs with Cronicle"
description: "Use Cronicle to schedule, run, monitor, and manually trigger recurring agent maintenance jobs across one or more worker servers from a web UI and REST API."
verification: "security_reviewed"
source: "https://github.com/jhuckaby/Cronicle"
author: "Cronicle contributors"
publisher_type: "open_source"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jhuckaby/Cronicle"
  github_stars: 5771
---

# Run visual scheduled agent jobs with Cronicle

Use Cronicle to schedule, run, monitor, and manually trigger recurring agent maintenance jobs across one or more worker servers from a web UI and REST API.

## Prerequisites

Cronicle server, Node.js and npm, POSIX host or worker servers, shell commands or Cronicle plugins, optional REST API keys and webhooks

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Node.js and npm, then run curl -s https://raw.githubusercontent.com/jhuckaby/Cronicle/master/bin/install.js | node as root. Start Cronicle with /opt/cronicle/bin/control.sh start, open the web UI, configure workers, API keys, plugins, and scheduled events for repeatable agent operations.
```

## Documentation

- http://cronicle.net

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-visual-scheduled-agent-jobs-with-cronicle/)
