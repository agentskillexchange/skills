---
name: "Convert SMTP-only alerts into routed notification deliveries with Mailrise"
slug: "convert-smtp-only-alerts-into-routed-notification-deliveries-with-mailrise"
description: "Use Mailrise to accept ordinary email alerts and fan them out through Apprise-backed notification channels when legacy systems can only speak SMTP."
github_stars: 1514
verification: "listed"
source: "https://github.com/YoRyan/mailrise"
author: "YoRyan and contributors"
publisher_type: "oss"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "YoRyan/mailrise"
  github_stars: 1514
---

# Convert SMTP-only alerts into routed notification deliveries with Mailrise

Use Mailrise to accept ordinary email alerts and fan them out through Apprise-backed notification channels when legacy systems can only speak SMTP.

## Prerequisites

Mailrise daemon or Docker image; Apprise configuration

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -e .[testing]
- make use of variables that communicate information about the email message. Use
- docker-compose.yml:

Requirements and caveats from upstream:
- .. |docker| image:: https://badgen.net/docker/pulls/yoryan/mailrise
- :alt: Docker pulls
- |docker| |commit| |checks|

Basic usage or getting-started notes:
- A minimalist Mailrise configuration, for example, might contain a single Apprise
- ============
- ---------------------

- Source: https://github.com/YoRyan/mailrise
- Extracted from upstream docs: https://raw.githubusercontent.com/YoRyan/mailrise/HEAD/README.rst

## Documentation

- https://github.com/YoRyan/mailrise

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-smtp-only-alerts-into-routed-notification-deliveries-with-mailrise/)
