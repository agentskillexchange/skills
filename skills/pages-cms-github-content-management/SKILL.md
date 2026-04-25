---
title: "Pages CMS Open Source Content Management for GitHub Repositories"
description: "Pages CMS is an open-source content management system built on top of GitHub. It provides a visual editing interface for managing content in Git repositories, purpose-built for static sites and content-driven apps using Jekyll, Hugo, Next.js, Astro, and similar frameworks."
verification: "security_reviewed"
source: "https://github.com/pagescms/pagescms"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pagescms/pagescms"
  github_stars: 3542
---

# Pages CMS Open Source Content Management for GitHub Repositories

Pages CMS is an open-source content management system that uses GitHub repositories as its content backend. It provides a clean, visual interface for editing Markdown, YAML, and JSON files stored in Git, making it ideal for static site generators and Jamstack applications. The project eliminates the need for databases, separate servers, or complex deployment pipelines. Core Capabilities Pages CMS provides a web-based editor for content stored in GitHub repositories. It supports editing Markdown files with frontmatter, managing media assets, and organizing content collections. The interface includes rich text editing, image uploads, and content type configuration through a simple YAML configuration file. Content changes are committed directly to the repository, leveraging Git for version history and collaboration. Technical Architecture Pages CMS is built with Next.js and uses PostgreSQL for session management and GitHub App credentials. It communicates with the GitHub API for all content operations. The system uses a GitHub App for authentication, providing fine-grained repository access permissions. Content is read from and written to GitHub repositories through the Git Contents and Trees APIs. Deployment Options A hosted version is available at app.pagescms.org for immediate use. For self-hosting, Pages CMS requires Node.js, PostgreSQL, and a GitHub App configuration. Docker Compose files are provided for local development. The setup involves creating a GitHub App, configuring environment variables, running database migrations, and starting the Next.js server. Framework Compatibility Pages CMS works with any static site generator or framework that reads content from files in a Git repository. Confirmed compatible frameworks include Jekyll, Hugo, Next.js, Astro, VuePress, Nuxt, Eleventy, and Gatsby. AI agents can leverage the GitHub API to programmatically manage content in repositories configured with Pages CMS, enabling automated content pipelines, bulk updates, and content migration workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pages-cms-github-content-management/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pages-cms-github-content-management
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pages-cms-github-content-management`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pages-cms-github-content-management/)
