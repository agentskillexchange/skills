---
title: "Prismic Headless CMS Content API Client"
description: "Prismic provides a headless CMS with an API-first editing model, and the official @prismicio/client package is the main integration point for fetching content in apps and automations. It fits agents that need to inspect repositories, publish structured content flows, or wire CMS data into websites and internal tools."
verification: security_reviewed
source: "https://github.com/prismicio/prismic-client"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "prismicio/prismic-client"
  github_stars: 177
  npm_package: "@prismicio/client"
  npm_weekly_downloads: 199739
---

# Prismic Headless CMS Content API Client

Prismic is a headless CMS built around structured content models, editorial workflows, and API-based delivery. Its official JavaScript client, @prismicio/client, is the primary SDK used to query repositories, fetch documents by type or UID, follow content relationships, and integrate editorial content into web applications. For agents, that makes Prismic useful anywhere content needs to move between a CMS and another system without relying on brittle browser automation.

The client supports common headless CMS tasks such as reading singleton settings documents, pulling page content by custom type, resolving linked entries, and querying content collections for search or generation workflows. In a real skill, an agent can combine @prismicio/client with framework adapters or plain Node.js scripts to audit a content repository, generate previews, validate that required slices exist, or transform Prismic content into site maps, docs pages, or marketing pages. Because the SDK is the official integration surface, it is also the safest place to anchor implementation guidance.

Prismic passes the intake gate cleanly: the official source code is published on GitHub under prismicio/prismic-client, the package is live on npm, the project has Apache-2.0 licensing, and the documentation is maintained on Prismic’s official docs site. Recent repository activity and published versions indicate active maintenance, which makes it a solid verified_metadata entry for the WordPress & CMS category.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prismic-headless-cms-content-api-client/)
