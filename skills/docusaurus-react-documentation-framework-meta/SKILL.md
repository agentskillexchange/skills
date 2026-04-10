---
name: "Docusaurus React Documentation Framework by Meta"
description: "Docusaurus is an open-source static site generator built with React, developed and maintained by Meta. It enables teams to build, deploy, and maintain documentation websites, blogs, and marketing pages with Markdown content, versioning support, and a rich plugin ecosystem."
verification: security_reviewed
source: "https://github.com/facebook/docusaurus"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "facebook/docusaurus"
  github_stars: 64315
  ase_npm_package: "docusaurus"
  npm_weekly_downloads: 21265
---

# Docusaurus React Documentation Framework by Meta

Docusaurus is a React-based documentation framework created by Meta (formerly Facebook) to help open source projects build and maintain beautiful documentation websites. With over 50,000 GitHub stars, it powers documentation for React Native, Jest, Prettier, Redux, and hundreds of other major projects.
Core Architecture
Docusaurus generates a fully static site that can be deployed anywhere. Content is written in Markdown or MDX (Markdown with JSX), allowing authors to embed interactive React components directly within documentation pages. The framework provides built-in docs versioning, i18n/localization support via CrowdIn integration, a blog plugin, full-text search via Algolia DocSearch, and automatic SEO metadata generation.
Key Features
The theming system uses a layered approach with swizzling, letting teams customize any component without forking. The plugin architecture supports custom pages, sidebars, and data sources. Docusaurus supports MDX v3, TypeScript configuration, live code editing with react-live, and Mermaid diagram rendering. It ships with a responsive default theme that includes dark mode, an announcement bar, and a configurable navigation.
Agent Integration
AI coding agents can scaffold a Docusaurus site with npm init docusaurus@latest, create documentation pages as Markdown files in the docs/ directory, configure sidebars in sidebars.js, customize the site in docusaurus.config.js, and deploy with a single command. The CLI provides docusaurus start for local development and docusaurus build for production output. Deployment integrations exist for GitHub Pages, Vercel, Netlify, and any static hosting provider. Licensed under MIT.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusaurus-react-documentation-framework-meta/)
