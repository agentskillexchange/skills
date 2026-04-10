---
name: Sveltia CMS Git-Based Headless Content Management System
description: Sveltia CMS is a free, open-source, Git-based headless CMS that runs
  entirely in the browser. Built as the definitive successor to Netlify CMS and Decap
  CMS, it offers a modern editing UX, first-class internationalization, and framework-agnostic
  design.
verification: security_reviewed
source: https://github.com/sveltia/sveltia-cms
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: sveltia/sveltia-cms
  github_stars: 2245
  ase_npm_package: '@sveltia/cms'
  npm_weekly_downloads: 2372
  license: MIT
---
# Sveltia CMS Git-Based Headless Content Management System

Sveltia CMS is an open-source, Git-based headless content management system designed for Jamstack websites and modern web development. It runs entirely in the browser with no server-side component required, making it lightweight and maintenance-free. The project was built as a direct successor to Netlify CMS (now Decap CMS), addressing hundreds of longstanding issues while maintaining compatibility with the existing configuration format.
Core Features
Sveltia CMS provides a visual editing interface for managing content stored in Git repositories (GitHub, GitLab). It supports Markdown, YAML, JSON, and TOML content formats with rich text editing, media management, and live preview. The CMS offers first-class internationalization (i18n) support with per-locale content management, making it suitable for multilingual websites.
Technical Architecture
Built with Svelte, Sveltia CMS compiles to a small JavaScript bundle that loads in the browser. It communicates directly with Git hosting APIs (GitHub/GitLab) for content operations. The CMS uses the same configuration file format (.sveltia-cms/config.yml or netlify/config.yml) as Netlify CMS and Decap CMS, enabling straightforward migration. Content is committed directly to Git branches, enabling version control and pull-request-based editorial workflows.
Integration Points
Sveltia CMS works with any static site generator including Hugo, Astro, Jekyll, Next.js, Nuxt, Eleventy, and Gatsby. It integrates with Git hosting providers for authentication and content storage. The CMS can be deployed as a single HTML page added to any existing site, requiring no backend infrastructure. AI agents can interact with the underlying Git content files through standard Git operations or the GitHub/GitLab APIs for automated content management workflows.
Migration from Netlify/Decap CMS
Sites currently using Netlify CMS or Decap CMS can migrate by replacing a single script tag. The configuration format is highly compatible, and Sveltia CMS provides migration documentation covering any differences. The project has gained rapid adoption with 2,200+ GitHub stars as teams migrate for improved UX, better security, and active maintenance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sveltia-cms-git-based-headless-cms/)
