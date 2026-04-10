---
title: "Prismic Headless CMS Content API Client"
description: "Prismic provides a headless CMS with an API-first editing model, and the official @prismicio/client package is the main integration point for fetching content in apps and automations. It fits agents that need to inspect repositories, publish structured content flows, or wire CMS data into websites and internal tools."
slug: "prismic-headless-cms-content-api-client"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/prismicio/prismic-client"
---

# Prismic Headless CMS Content API Client

Prismic provides a headless CMS with an API-first editing model, and the official @prismicio/client package is the main integration point for fetching content in apps and automations. It fits agents that need to inspect repositories, publish structured content flows, or wire CMS data into websites and internal tools.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install prismic-headless-cms-content-api-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Prismic is a headless CMS built around structured content models, editorial workflows, and API-based delivery. Its official JavaScript client, @prismicio/client, is the primary SDK used to query repositories, fetch documents by type or UID, follow content relationships, and integrate editorial content into web applications. For agents, that makes Prismic useful anywhere content needs to move between a CMS and another system without relying on brittle browser automation.
The client supports common headless CMS tasks such as reading singleton settings documents, pulling page content by custom type, resolving linked entries, and querying content collections for search or generation workflows. In a real skill, an agent can combine @prismicio/client with framework adapters or plain Node.js scripts to audit a content repository, generate previews, validate that required slices exist, or transform Prismic content into site maps, docs pages, or marketing pages. Because the SDK is the official integration surface, it is also the safest place to anchor implementation guidance.
Prismic passes the intake gate cleanly: the official source code is published on GitHub under prismicio/prismic-client, the package is live on npm, the project has Apache-2.0 licensing, and the documentation is maintained on Prismic’s official docs site. Recent repository activity and published versions indicate active maintenance, which makes it a solid verified_metadata entry for the WordPress & CMS category.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prismic-headless-cms-content-api-client/)
