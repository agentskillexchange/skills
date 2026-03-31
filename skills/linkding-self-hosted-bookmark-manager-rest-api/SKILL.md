---
name: "linkding Self-Hosted Bookmark Manager with REST API"
description: "linkding is a minimal, fast, self-hosted bookmark manager with a full REST API, tag-based organization, automatic metadata extraction, web archiving, browser extensions, and SSO support. It runs in Docker and is built with Django and Python."
category: "Research &amp; Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/sissbruecker/linkding"
---
# linkding Self-Hosted Bookmark Manager with REST API

linkding is a minimal, fast, self-hosted bookmark manager with a full REST API, tag-based organization, automatic metadata extraction, web archiving, browser extensions, and SSO support. It runs in Docker and is built with Django and Python.

## Overview

linkding is a self-hosted bookmark manager designed to be minimal, fast, and easy to deploy using Docker. Created by Sascha Sissbruecker, it provides a clean web interface for managing bookmarks along with a comprehensive REST API that makes it ideal for integration with AI agents and automation workflows.

Core Features

Clean, readable UI with tag-based organization and full-text search
Bulk editing, Markdown notes attached to bookmarks, and read-it-later functionality
Automatic metadata extraction: titles, descriptions, and favicons from bookmarked URLs
Web archiving via local HTML snapshots or Internet Archive integration
Bookmark sharing between users or with guest access
Import and export in Netscape HTML format for migration
Progressive Web App (PWA) support for mobile usage
Browser extensions for Firefox and Chrome plus a bookmarklet
SSO support via OIDC or authentication proxies

REST API
The REST API is a key differentiator for agent integration. It provides full CRUD operations on bookmarks and tags, search and filtering capabilities, and bulk operations. Agents can use the API to save research links, organize bookmarks by project, search saved resources, and build knowledge bases from curated link collections.

Agent Integration
For AI agents, linkding serves as a persistent bookmark and research link store. Agents can save URLs discovered during research, tag them for later retrieval, add notes with context about why a link was saved, and search the bookmark database for relevant resources. The REST API with token authentication makes programmatic access straightforward.

Deployment
linkding runs as a Docker container with SQLite as the default database (PostgreSQL also supported). The application is built with Django and requires minimal resources. A community ecosystem includes mobile apps, additional browser extensions, and CLI tools like linkding-cli built on the aiolinkding Python library.

The project is MIT-licensed with over 10,300 GitHub stars. Full documentation is available at linkding.link. Deploy with docker pull sissbruecker/linkding and configure via environment variables.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill linkding-self-hosted-bookmark-manager-rest-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill linkding-self-hosted-bookmark-manager-rest-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill linkding-self-hosted-bookmark-manager-rest-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill linkding-self-hosted-bookmark-manager-rest-api -a codex
```

### OpenClaw

```bash
clawhub install linkding-self-hosted-bookmark-manager-rest-api
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linkding-self-hosted-bookmark-manager-rest-api/)
