---
name: "Starlight Documentation Framework for Astro"
description: "Starlight is a documentation website framework built on Astro that generates beautiful, accessible, and high-performance documentation sites. It provides built-in navigation, search, i18n, syntax highlighting, and dark mode with minimal configuration."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/withastro/starlight"
tool_ecosystem:
  tool: starlight
  github_repo: withastro/starlight
  github_stars: 8213
  license: MIT
  maintained: true
---
# Starlight Documentation Framework for Astro

Starlight is a documentation website framework built on Astro that generates beautiful, accessible, and high-performance documentation sites. It provides built-in navigation, search, i18n, syntax highlighting, and dark mode with minimal configuration.

## Overview

Starlight is a full-featured documentation website framework built on top of Astro, the content-driven web framework. Developed and maintained by the Astro team, Starlight generates fast, accessible, and SEO-friendly documentation sites from Markdown and MDX content with minimal configuration required.

Built-in Features

Starlight ships with a comprehensive set of documentation features out of the box: automatic sidebar navigation generated from the file system, full-text search powered by Pagefind, internationalization (i18n) support with RTL language handling, syntax highlighting via Expressive Code, automatic dark and light mode, table of contents generation, and OpenGraph image support. The framework handles responsive layout, accessibility compliance, and performance optimization automatically.

Content Authoring

Documentation is written in standard Markdown or MDX files with frontmatter for metadata like title, description, sidebar order, and badges. Starlight supports custom components via MDX, allowing authors to embed interactive elements, callouts, tabs, and code groups within documentation pages. Content collections are validated at build time using Zod schemas.

Customization and Theming

Starlight sites are fully customizable through Astro configuration. Users can override any component, add custom CSS, configure navigation structure, add plugins, and extend functionality with the Astro ecosystem. The framework supports custom page layouts, component overrides, and theme customization through CSS custom properties.

Agent Integration

AI agents can use Starlight to generate and maintain documentation sites for projects, APIs, and tools. Agents can create Markdown files, configure the site structure, and deploy documentation through standard Astro build commands. The file-based content model makes it straightforward for agents to programmatically create, update, and organize documentation pages.

Installation

Create a new Starlight project with `npm create astro@latest -- --template starlight`. Starlight requires Node.js 18+ and integrates with all Astro deployment adapters including Vercel, Netlify, Cloudflare Pages, and static hosting. The project is MIT licensed with over 8,000 GitHub stars.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill starlight-documentation-framework-astro
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill starlight-documentation-framework-astro -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill starlight-documentation-framework-astro -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill starlight-documentation-framework-astro -a codex
```

### OpenClaw

```bash
clawhub install starlight-documentation-framework-astro
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/starlight-documentation-framework-astro/)
