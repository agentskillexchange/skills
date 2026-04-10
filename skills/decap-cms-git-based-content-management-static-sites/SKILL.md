---
name: Decap CMS Git-Based Content Management for Static Sites
description: An agent skill built on Decap CMS (formerly Netlify CMS), the open-source
  Git-based content management system for static site generators. Provides a visual
  editing interface backed by Git commits, enabling content workflows for Hugo, Jekyll,
  Gatsby, Next.js, and other Jamstack frameworks.
verification: security_reviewed
source: https://github.com/decaporg/decap-cms
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: decaporg/decap-cms
  github_stars: 18998
  ase_npm_package: decap-cms
  npm_weekly_downloads: 1853
---
# Decap CMS Git-Based Content Management for Static Sites

Decap CMS is an open-source content management system that stores content as files in a Git repository rather than a traditional database. Originally created as Netlify CMS, it was rebranded to Decap CMS to reflect its vendor-neutral nature. This skill enables agents to manage content creation, editing, and publishing workflows through Decap CMS's API and configuration system.
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

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decap-cms-git-based-content-management-static-sites/)
