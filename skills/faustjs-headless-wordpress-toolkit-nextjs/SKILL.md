---
name: "Faust.js Headless WordPress Toolkit for Next.js"
description: "Faust.js by WP Engine is a JavaScript framework and WordPress plugin that streamlines building headless WordPress sites with Next.js. It handles data fetching via WPGraphQL, authentication, content previews, and server-side rendering, providing a production-ready bridge between WordPress as a CMS and React-based frontends."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/wpengine/faustjs"
tool_ecosystem:
  github_repo: "https://github.com/wpengine/faustjs"
  github_stars: 1568
---
# Faust.js Headless WordPress Toolkit for Next.js

Faust.js by WP Engine is a JavaScript framework and WordPress plugin that streamlines building headless WordPress sites with Next.js. It handles data fetching via WPGraphQL, authentication, content previews, and server-side rendering, providing a production-ready bridge between WordPress as a CMS and React-based frontends.

Faust.js is an open-source headless WordPress toolkit developed and maintained by WP Engine. It consists of NPM packages and a companion WordPress plugin that together solve the core challenges of building decoupled WordPress sites using Next.js and React. The framework reduces the complexity of data fetching, authentication, and content previewing that typically makes headless WordPress projects difficult.

Architecture and Components

Faust.js is built around several key packages:

- @faustwp/core: The core Next.js framework integration that provides routing, data fetching hooks, and template resolution based on WordPress content types

- @faustwp/cli: A command-line tool for generating TypeScript types from your WordPress GraphQL schema and scaffolding new projects

- @faustwp/blocks: A block rendering system that maps WordPress Gutenberg blocks to React components on the frontend

- FaustWP Plugin: A WordPress plugin that enables authenticated previews, rewrites, and configuration management from the WordPress admin

Key Features

Faust.js provides first-class support for WPGraphQL, the most popular GraphQL implementation for WordPress. It includes built-in authentication handling that lets editors preview unpublished content through the Next.js frontend. The template hierarchy system mirrors WordPress’s native template resolution, so developers can create templates for specific post types, taxonomies, and archives just as they would in a traditional WordPress theme.

Developer Experience

The framework supports both static site generation (SSG) and server-side rendering (SSR) through Next.js. Its CLI tool generates TypeScript types from your WordPress schema, providing type safety across the data layer. Faust.js projects can be deployed to any hosting platform that supports Next.js, including Vercel, Netlify, and WP Engine’s own Atlas platform.

Agent Skill Applications

A Faust.js skill enables AI agents to scaffold headless WordPress projects, configure the WordPress-to-Next.js bridge, manage WPGraphQL queries, and troubleshoot common issues in decoupled WordPress architectures. Agents can use it to generate component templates for WordPress block types, set up authenticated preview flows, and optimize data fetching strategies for headless WordPress sites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill faustjs-headless-wordpress-toolkit-nextjs
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill faustjs-headless-wordpress-toolkit-nextjs -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill faustjs-headless-wordpress-toolkit-nextjs -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill faustjs-headless-wordpress-toolkit-nextjs -a codex
```

### OpenClaw

```bash
clawhub install faustjs-headless-wordpress-toolkit-nextjs
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/faustjs-headless-wordpress-toolkit-nextjs/)
