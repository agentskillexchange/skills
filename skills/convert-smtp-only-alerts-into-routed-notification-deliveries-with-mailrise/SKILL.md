---
title: "Convert SMTP-only alerts into routed notification deliveries with Mailrise"
description: "Use Mailrise to accept ordinary email alerts and fan them out through Apprise-backed notification channels when legacy systems can only speak SMTP."
verification: "security_reviewed"
source: "https://github.com/YoRyan/mailrise"
author: "YoRyan and contributors"
publisher_type: "oss"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "YoRyan/mailrise"
  github_stars: 1514
---

# Convert SMTP-only alerts into routed notification deliveries with Mailrise

Use Mailrise to accept ordinary email alerts and fan them out through Apprise-backed notification channels when legacy systems can only speak SMTP.

## Prerequisites

Mailrise daemon or Docker image; Apprise configuration

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Deploy Mailrise from the upstream repository or official Docker image, provide a Mailrise configuration that references one or more Apprise configs, then point SMTP-only alert senders at the Mailrise host and route by recipient address pattern.
```

## Documentation

- https://github.com/YoRyan/mailrise

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-smtp-only-alerts-into-routed-notification-deliveries-with-mailrise/)
