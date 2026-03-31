---
name: "Docusaurus React Documentation Framework by Meta"
description: "Docusaurus is an open-source static site generator built with React, developed and maintained by Meta. It enables teams to build, deploy, and maintain documentation websites, blogs, and marketing pages with Markdown content, versioning support, and a rich plugin ecosystem."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/facebook/docusaurus"
tool_ecosystem:
  tool: docusaurus
  github_repo: facebook/docusaurus
  github_stars: 64315
  npm_weekly_downloads: 17913
  license: MIT
  maintained: true
---
# Docusaurus React Documentation Framework by Meta

Docusaurus is an open-source static site generator built with React, developed and maintained by Meta. It enables teams to build, deploy, and maintain documentation websites, blogs, and marketing pages with Markdown content, versioning support, and a rich plugin ecosystem.

## Overview

Docusaurus is a React-based documentation framework created by Meta (formerly Facebook) to help open source projects build and maintain beautiful documentation websites. With over 50,000 GitHub stars, it powers documentation for React Native, Jest, Prettier, Redux, and hundreds of other major projects.

Core Architecture
Docusaurus generates a fully static site that can be deployed anywhere. Content is written in Markdown or MDX (Markdown with JSX), allowing authors to embed interactive React components directly within documentation pages. The framework provides built-in docs versioning, i18n/localization support via CrowdIn integration, a blog plugin, full-text search via Algolia DocSearch, and automatic SEO metadata generation.

Key Features
The theming system uses a layered approach with swizzling, letting teams customize any component without forking. The plugin architecture supports custom pages, sidebars, and data sources. Docusaurus supports MDX v3, TypeScript configuration, live code editing with react-live, and Mermaid diagram rendering. It ships with a responsive default theme that includes dark mode, an announcement bar, and a configurable navigation.

Agent Integration
AI coding agents can scaffold a Docusaurus site with npm init docusaurus@latest, create documentation pages as Markdown files in the docs/ directory, configure sidebars in sidebars.js, customize the site in docusaurus.config.js, and deploy with a single command. The CLI provides docusaurus start for local development and docusaurus build for production output. Deployment integrations exist for GitHub Pages, Vercel, Netlify, and any static hosting provider. Licensed under MIT.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docusaurus-react-documentation-framework-meta
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docusaurus-react-documentation-framework-meta -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docusaurus-react-documentation-framework-meta -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docusaurus-react-documentation-framework-meta -a codex
```

### OpenClaw

```bash
clawhub install docusaurus-react-documentation-framework-meta
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusaurus-react-documentation-framework-meta/)
