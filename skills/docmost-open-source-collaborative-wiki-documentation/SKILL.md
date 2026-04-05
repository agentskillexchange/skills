---
name: "Docmost Open Source Collaborative Wiki and Documentation Platform"
description: "Docmost is an open-source collaborative wiki and documentation platform that serves as a self-hosted alternative to Confluence and Notion. It features real-time collaboration, nested pages, diagrams, spaces, and granular permissions management."
category: "Calendar, Email &amp; Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/docmost/docmost"
tool_ecosystem:
  github_repo: "docmost/docmost"
  github_stars: 19690
---
# Docmost Open Source Collaborative Wiki and Documentation Platform

Docmost is an open-source collaborative wiki and documentation platform that serves as a self-hosted alternative to Confluence and Notion. It features real-time collaboration, nested pages, diagrams, spaces, and granular permissions management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docmost-open-source-collaborative-wiki-documentation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docmost-open-source-collaborative-wiki-documentation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docmost-open-source-collaborative-wiki-documentation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docmost-open-source-collaborative-wiki-documentation -a codex
```

### OpenClaw

```bash
clawhub install docmost-open-source-collaborative-wiki-documentation
```

## Details

Overview
Docmost is an open-source collaborative wiki and documentation software designed as a self-hosted alternative to Confluence and Notion. Built with TypeScript using NestJS on the backend and React on the frontend, it provides real-time collaborative editing, nested page hierarchies, and team-based workspaces. With nearly 20,000 GitHub stars and active development, Docmost has emerged as one of the most capable open-source documentation platforms available.

Core Capabilities
Docmost provides a rich collaborative editing experience built on the ProseMirror editor framework. Multiple users can edit the same document simultaneously with real-time cursor tracking and change synchronization. The platform organizes content into Spaces (similar to Confluence spaces or Notion workspaces), each with their own permission settings, page hierarchies, and member access controls.

Diagram and Embed Support
The editor natively supports three diagramming tools: Draw.io for general-purpose diagrams, Excalidraw for hand-drawn-style sketches, and Mermaid for code-based diagrams including flowcharts, sequence diagrams, and Gantt charts. Docmost also supports embedding content from external services including Airtable, Loom, Miro, and other platforms that provide embed URLs.

Agent Integration Points
AI agents can interact with Docmost through its REST API to create, read, update, and manage documentation programmatically. This enables workflows where coding agents automatically generate or update technical documentation as code changes, maintain runbooks and operational guides, and organize knowledge base content. Agents can create pages within specific spaces, manage page hierarchies, and attach files to documentation.

Key Features

Real-time collaborative editing with multi-user support
Spaces for organizing content into team workspaces
Nested page hierarchies for structured documentation
Built-in diagrams: Draw.io, Excalidraw, and Mermaid
Granular permissions and group-based access control
Full-text search across all content
Page history and version tracking
File attachment support
Comment threads on documents
Internationalization with 10+ language translations

Deployment
Docmost is deployed via Docker Compose. It requires PostgreSQL for data storage and Redis for caching and real-time features. A typical deployment runs with three containers: the Docmost application, PostgreSQL, and Redis.

docker compose up -d
The application is accessible on port 3000 by default. For production use, a reverse proxy with SSL termination (such as Caddy or Nginx) is recommended.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docmost-open-source-collaborative-wiki-documentation/)
