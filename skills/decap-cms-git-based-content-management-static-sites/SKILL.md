---
title: "Decap CMS Git-Based Content Management for Static Sites"
description: "An agent skill built on Decap CMS (formerly Netlify CMS), the open-source Git-based content management system for static site generators. Provides a visual editing interface backed by Git commits, enabling content workflows for Hugo, Jekyll, Gatsby, Next.js, and other Jamstack frameworks."
slug: "decap-cms-git-based-content-management-static-sites"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/decaporg/decap-cms"
tool_ecosystem:
  github_repo: "decaporg/decap-cms"
  github_stars: 18998
  npm_package: "decap-cms"
  npm_weekly_downloads: 1853
---

# Decap CMS Git-Based Content Management for Static Sites

An agent skill built on Decap CMS (formerly Netlify CMS), the open-source Git-based content management system for static site generators. Provides a visual editing interface backed by Git commits, enabling content workflows for Hugo, Jekyll, Gatsby, Next.js, and other Jamstack frameworks.

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
clawhub install decap-cms-git-based-content-management-static-sites
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Decap CMS is an open-source content management system that stores content as files in a Git repository rather than a traditional database. Originally created as Netlify CMS, it was rebranded to Decap CMS to reflect its vendor-neutral nature. This skill enables agents to manage content creation, editing, and publishing workflows through Decap CMS’s API and configuration system.
Core Capabilities
The skill manages Decap CMS configurations that define content collections, fields, and editorial workflows. It can generate and modify config.yml files that specify which Git branches to target, how content types are structured, what widgets to use for different field types (strings, markdown, images, dates, lists, objects, relations), and how media files are stored. The skill also handles editorial workflow states: draft, in review, and ready to publish, each mapped to Git branch operations.
How It Works
Decap CMS operates as a single-page React application that communicates with Git hosting providers (GitHub, GitLab, Bitbucket) through their APIs. When content is saved, changes are committed directly to the configured branch or, in editorial workflow mode, created as pull requests for review. The skill automates configuration generation based on content model descriptions, validates field definitions against supported widget types, and manages Git backend authentication settings including OAuth, implicit grant, and Git Gateway configurations.
Content Modeling
The skill translates content requirements into Decap CMS collection definitions. It supports folder collections for repeated content types like blog posts, file collections for singleton pages like site settings, and nested collections for hierarchical content structures. Each collection can define custom preview templates, slug patterns, summary formats, and field validation rules. The skill handles complex field types including nested objects, variable-type lists, and relation fields that reference entries from other collections.
Integration Points
Decap CMS works with any static site generator that reads content from files: Hugo (TOML, YAML, JSON front matter), Jekyll (YAML front matter with Markdown), Gatsby (MDX, JSON), Next.js, Nuxt, Eleventy, Hexo, and others. The skill generates framework-specific configurations and can set up the Decap CMS admin interface as a standalone page in the static site build output. It supports custom preview components written in React for live content preview during editing.
Technical Details
Decap CMS is written in JavaScript and React, distributed on npm as decap-cms and decap-cms-app, and licensed under MIT. The project has over 19,000 GitHub stars with active development and commits in March 2026. It supports extensibility through custom widgets, preview templates, editor components, and backend plugins.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decap-cms-git-based-content-management-static-sites/)
