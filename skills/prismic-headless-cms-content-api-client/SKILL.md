---
title: "Prismic Headless CMS Content API Client"
description: "Prismic provides a headless CMS with an API-first editing model, and the official @prismicio/client package is the main integration point for fetching content in apps and automations. It fits agents that need to inspect repositories, publish structured content flows, or wire CMS data into websites and internal tools."
verification: security_reviewed
source: "https://github.com/prismicio/prismic-client"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "prismicio/prismic-client"
  github_stars: 177
  npm_package: "@prismicio/client"
  npm_weekly_downloads: 199739
  license: "Apache-2.0"
---

# Prismic Headless CMS Content API Client

Prismic is a headless CMS built around structured content models, editorial workflows, and API-based delivery. Its official JavaScript client, @prismicio/client, is the primary SDK used to query repositories, fetch documents by type or UID, follow content relationships, and integrate editorial content into web applications. For agents, that makes Prismic useful anywhere content needs to move between a CMS and another system without relying on brittle browser automation.

The client supports common headless CMS tasks such as reading singleton settings documents, pulling page content by custom type, resolving linked entries, and querying content collections for search or generation workflows. In a real skill, an agent can combine @prismicio/client with framework adapters or plain Node.js scripts to audit a content repository, generate previews, validate that required slices exist, or transform Prismic content into site maps, docs pages, or marketing pages. Because the SDK is the official integration surface, it is also the safest place to anchor implementation guidance.

Prismic passes the intake gate cleanly: the official source code is published on GitHub under prismicio/prismic-client, the package is live on npm, the project has Apache-2.0 licensing, and the documentation is maintained on Prismic’s official docs site. Recent repository activity and published versions indicate active maintenance, which makes it a solid verified_metadata entry for the WordPress & CMS category.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prismic-headless-cms-content-api-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prismic-headless-cms-content-api-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prismic-headless-cms-content-api-client/)
