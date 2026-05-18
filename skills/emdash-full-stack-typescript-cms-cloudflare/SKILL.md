---
name: "EmDash Full-Stack TypeScript CMS by Cloudflare"
slug: "emdash-full-stack-typescript-cms-cloudflare"
description: "EmDash is an open-source, full-stack TypeScript CMS built on Astro and Cloudflare, designed as a spiritual successor to WordPress. It features sandboxed plugins, structured content via Portable Text, a built-in MCP server for AI agents, and runs on Cloudflare Workers, D1, and R2 or any Node.js server with SQLite."
github_stars: 9237
verification: "listed"
source: "https://github.com/emdash-cms/emdash"
category: "WordPress & CMS"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "emdash-cms/emdash"
  github_stars: 9237
---

# EmDash Full-Stack TypeScript CMS by Cloudflare

EmDash is an open-source, full-stack TypeScript CMS built on Astro and Cloudflare, designed as a spiritual successor to WordPress. It features sandboxed plugins, structured content via Portable Text, a built-in MCP server for AI agents, and runs on Cloudflare Workers, D1, and R2 or any Node.js server with SQLite.

## Installation

Use the upstream install or setup path that matches your environment:
- npm create emdash@latest
- npx emdash types
- git clone https://github.com/emdash-cms/emdash.git && cd emdash
- pnpm install

Requirements and caveats from upstream:
- EmDash depends on Dynamic Workers to run secure sandboxed plugins. Dynamic Workers are currently only available on paid accounts. [Upgrade your account](https://www.cloudflare.com/plans/developer-platform/) (starting...
- EmDash runs on Cloudflare (D1 + R2 + Workers) or any Node.js server with SQLite. No PHP, no separate hosting tier -- just deploy your Astro site.

Basic usage or getting-started notes:
- A full-stack TypeScript CMS built on [Astro](https://astro.build/) and [Cloudflare](https://www.cloudflare.com/). EmDash takes the ideas that made WordPress dominant -- extensibility, admin UX, a plugin ecosystem -- a...
- **Sandboxed plugins.** WordPress plugins have full access to the database, filesystem, and user data. A single vulnerable plugin can compromise the entire site. EmDash plugins run in isolated [Worker sandboxes](https:...
- to: "editors@example.com",

- Source: https://github.com/emdash-cms/emdash
- Extracted from upstream docs: https://raw.githubusercontent.com/emdash-cms/emdash/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/emdash-full-stack-typescript-cms-cloudflare/)
