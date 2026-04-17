---
title: "Front Matter CMS Visual Studio Code Headless CMS"
description: "Front Matter CMS is a Visual Studio Code extension that transforms the editor into a full-featured headless content management system for static site generators. Unlike traditional CMS platforms that run as separate web applications, Front Matter CMS operates entirely within the VS Code environment, providing content management capabilities without leaving the development workflow. This skill automates Front Matter CMS configuration and content operations for agent-driven publishing pipelines.\nCore Capabilities\nThe skill manages Front Matter CMS configurations defined in frontmatter.json, including content type definitions, taxonomy registrations, custom field schemas, snippet templates, and media folder mappings. It can scaffold new content entries with pre-populated front matter fields, manage draft and published states, handle taxonomy creation and assignment, and configure custom sorting and filtering rules for the content dashboard.\nHow It Works\nFront Matter CMS stores all configuration in a frontmatter.json file at the project root and manages content as Markdown or MDX files with YAML, TOML, or JSON front matter. The skill generates and modifies these configuration files based on content modeling requirements, creates content files with properly structured front matter, manages media assets in configured public folders, and handles data files for reusable content blocks. Content types support custom fields including strings, numbers, booleans, dates, images, tags, categories, choice lists, and nested block fields.\nContent Dashboard and Workflow\nThe CMS provides a visual dashboard within VS Code showing all content entries with their status, date, and metadata. The skill can query content status, trigger bulk operations like publishing scheduled drafts, update SEO metadata fields including title, description, and social sharing images, and manage multilingual content through configured locale settings. It supports custom scripts that run on content creation or save events.\nIntegration Points\nFront Matter CMS works with Hugo, Jekyll, Next.js, Gatsby, Astro, Hexo, Eleventy, Docusaurus, and any framework that uses file-based content with front matter metadata. The skill handles framework-specific front matter conventions, preview URL generation for local development servers, and Git-based content versioning. It supports custom placeholders in content templates and data file references for structured content relationships.\nTechnical Details\nFront Matter CMS is written in TypeScript, distributed through the VS Code Marketplace and on GitHub, and licensed under MIT. The project has over 2,400 GitHub stars with active development through March 2026. It supports extensibility through custom scripts, content type inheritance, field conditions, and webhook integrations for external build triggers."
verification: security_reviewed
source: "https://github.com/estruyf/vscode-front-matter"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "estruyf/vscode-front-matter"
  github_stars: 2482
---

# Front Matter CMS Visual Studio Code Headless CMS

Front Matter CMS is a Visual Studio Code extension that transforms the editor into a full-featured headless content management system for static site generators. Unlike traditional CMS platforms that run as separate web applications, Front Matter CMS operates entirely within the VS Code environment, providing content management capabilities without leaving the development workflow. This skill automates Front Matter CMS configuration and content operations for agent-driven publishing pipelines.
Core Capabilities
The skill manages Front Matter CMS configurations defined in frontmatter.json, including content type definitions, taxonomy registrations, custom field schemas, snippet templates, and media folder mappings. It can scaffold new content entries with pre-populated front matter fields, manage draft and published states, handle taxonomy creation and assignment, and configure custom sorting and filtering rules for the content dashboard.
How It Works
Front Matter CMS stores all configuration in a frontmatter.json file at the project root and manages content as Markdown or MDX files with YAML, TOML, or JSON front matter. The skill generates and modifies these configuration files based on content modeling requirements, creates content files with properly structured front matter, manages media assets in configured public folders, and handles data files for reusable content blocks. Content types support custom fields including strings, numbers, booleans, dates, images, tags, categories, choice lists, and nested block fields.
Content Dashboard and Workflow
The CMS provides a visual dashboard within VS Code showing all content entries with their status, date, and metadata. The skill can query content status, trigger bulk operations like publishing scheduled drafts, update SEO metadata fields including title, description, and social sharing images, and manage multilingual content through configured locale settings. It supports custom scripts that run on content creation or save events.
Integration Points
Front Matter CMS works with Hugo, Jekyll, Next.js, Gatsby, Astro, Hexo, Eleventy, Docusaurus, and any framework that uses file-based content with front matter metadata. The skill handles framework-specific front matter conventions, preview URL generation for local development servers, and Git-based content versioning. It supports custom placeholders in content templates and data file references for structured content relationships.
Technical Details
Front Matter CMS is written in TypeScript, distributed through the VS Code Marketplace and on GitHub, and licensed under MIT. The project has over 2,400 GitHub stars with active development through March 2026. It supports extensibility through custom scripts, content type inheritance, field conditions, and webhook integrations for external build triggers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/front-matter-cms-vscode-headless-cms
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/front-matter-cms-vscode-headless-cms` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/front-matter-cms-vscode-headless-cms/)
