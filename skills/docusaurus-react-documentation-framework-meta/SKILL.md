---
title: "Docusaurus React Documentation Framework by Meta"
description: "Docusaurus is an open-source static site generator built with React, developed and maintained by Meta. It enables teams to build, deploy, and maintain documentation websites, blogs, and marketing pages with Markdown content, versioning support, and a rich plugin ecosystem."
slug: "docusaurus-react-documentation-framework-meta"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/facebook/docusaurus"
tool_ecosystem:
  github_repo: "facebook/docusaurus"
  github_stars: 64315
  npm_package: "docusaurus"
  npm_weekly_downloads: 21265
listed: true
---

# Docusaurus React Documentation Framework by Meta

Docusaurus is an open-source static site generator built with React, developed and maintained by Meta. It enables teams to build, deploy, and maintain documentation websites, blogs, and marketing pages with Markdown content, versioning support, and a rich plugin ecosystem.

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
clawhub install docusaurus-react-documentation-framework-meta
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Docusaurus is a React-based documentation framework created by Meta (formerly Facebook) to help open source projects build and maintain beautiful documentation websites. With over 50,000 GitHub stars, it powers documentation for React Native, Jest, Prettier, Redux, and hundreds of other major projects.
Core Architecture
Docusaurus generates a fully static site that can be deployed anywhere. Content is written in Markdown or MDX (Markdown with JSX), allowing authors to embed interactive React components directly within documentation pages. The framework provides built-in docs versioning, i18n/localization support via CrowdIn integration, a blog plugin, full-text search via Algolia DocSearch, and automatic SEO metadata generation.
Key Features
The theming system uses a layered approach with swizzling, letting teams customize any component without forking. The plugin architecture supports custom pages, sidebars, and data sources. Docusaurus supports MDX v3, TypeScript configuration, live code editing with react-live, and Mermaid diagram rendering. It ships with a responsive default theme that includes dark mode, an announcement bar, and a configurable navigation.
Agent Integration
AI coding agents can scaffold a Docusaurus site with npm init docusaurus@latest, create documentation pages as Markdown files in the docs/ directory, configure sidebars in sidebars.js, customize the site in docusaurus.config.js, and deploy with a single command. The CLI provides docusaurus start for local development and docusaurus build for production output. Deployment integrations exist for GitHub Pages, Vercel, Netlify, and any static hosting provider. Licensed under MIT.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusaurus-react-documentation-framework-meta/)
