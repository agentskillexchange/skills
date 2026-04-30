---
title: "Cockpit CMS Headless Content Platform with REST and GraphQL APIs"
description: "Cockpit CMS is a lightweight headless content platform for teams that want flexible models, REST and GraphQL APIs, and self-hosted deployment without a heavy stack. It supports websites, apps, and multi-language content workflows with either SQLite or MongoDB backends."
verification: "security_reviewed"
source: "https://github.com/Cockpit-HQ/Cockpit"
author: "Cockpit-HQ"
publisher_type: "Open Source Project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "Cockpit-HQ/Cockpit"
  github_stars: 686
---

# Cockpit CMS Headless Content Platform with REST and GraphQL APIs

Cockpit CMS is a lightweight headless content platform for teams that want flexible models, REST and GraphQL APIs, and self-hosted deployment without a heavy stack. It supports websites, apps, and multi-language content workflows with either SQLite or MongoDB backends.

## Prerequisites

PHP 8.3+, SQLite or MongoDB, Apache or Nginx, Docker optional

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
docker run -d --name cockpit -p 8080:80 -v cockpit_storage:/var/www/html/storage cockpithq/cockpit:core-latest
```

## Documentation

- https://getcockpit.com/documentation

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cockpit-cms-headless-content-platform-rest-graphql-apis/)
