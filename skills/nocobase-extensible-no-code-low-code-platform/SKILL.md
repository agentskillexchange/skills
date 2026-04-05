---
name: "NocoBase Extensible AI-Powered No-Code and Low-Code Platform"
description: "NocoBase is the most extensible open-source no-code/low-code platform for building business applications. It features a data model-driven architecture, AI employee integration, plugin system, and WYSIWYG interface builder."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/nocobase/nocobase"
---
# NocoBase Extensible AI-Powered No-Code and Low-Code Platform

NocoBase is the most extensible open-source no-code/low-code platform for building business applications. It features a data model-driven architecture, AI employee integration, plugin system, and WYSIWYG interface builder.

NocoBase is an open-source no-code and low-code platform designed for building business applications and enterprise solutions. Unlike rigid no-code tools that limit you to predefined templates, NocoBase separates data structure from user interface, allowing unlimited flexibility in how data is modeled, displayed, and interacted with. The project has gained significant traction on GitHub and is actively maintained with frequent releases.



Data Model-Driven Architecture

NocoBase’s core design principle is that UI and data structure are fully decoupled. You define your data models (tables, fields, relationships) independently, then create any number of blocks, views, and actions on top of them. A single table can have multiple list views, form views, kanban boards, calendars, and chart visualizations simultaneously. The platform supports the main database, external databases, and third-party APIs as data sources.



AI Employee System

NocoBase integrates AI capabilities directly into business workflows through its AI Employee feature. You can define AI roles (translator, analyst, researcher, assistant) that operate within the platform’s interfaces and automation workflows. The AI integration is context-aware, meaning AI employees can access and act on the data within your NocoBase application, making them practical for real business tasks rather than isolated demos.



Plugin Architecture

Everything in NocoBase is a plugin. The core platform provides the foundation, and all features—from field types and block types to authentication methods and workflow nodes—are implemented as plugins. This architecture means you can add, remove, or replace any capability without touching the core. Custom plugins can be written in TypeScript/JavaScript and installed through the plugin manager.



WYSIWYG Interface Builder

NocoBase provides a visual interface builder where pages serve as canvases for arranging blocks and actions, similar to Notion. A one-click toggle switches between usage mode and configuration mode. The configuration interface is designed for business users, not just programmers, making it accessible for teams without dedicated developers.



Workflow Automation

The built-in workflow engine supports event-driven automation with conditional branching, loops, data manipulation, HTTP requests, and integrations. Workflows can be triggered by data changes, schedules, or manual actions. Combined with the AI employee system, workflows can include AI-powered decision-making steps.



Installation

NocoBase can be installed via Docker: docker compose up -d using the official compose file, or via npm/yarn for development setups. Detailed instructions are available at docs.nocobase.com.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nocobase-extensible-no-code-low-code-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nocobase-extensible-no-code-low-code-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nocobase-extensible-no-code-low-code-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nocobase-extensible-no-code-low-code-platform -a codex
```

### OpenClaw

```bash
clawhub install nocobase-extensible-no-code-low-code-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nocobase-extensible-no-code-low-code-platform/)
