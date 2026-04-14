---
title: "NocoBase Extensible AI-Powered No-Code and Low-Code Platform"
description: "NocoBase is the most extensible open-source no-code/low-code platform for building business applications. It features a data model-driven architecture, AI employee integration, plugin system, and WYSIWYG interface builder."
verification: security_reviewed
source: "https://github.com/nocobase/nocobase"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nocobase/nocobase"
  github_stars: 22114
  npm_package: "nocobase"
  npm_weekly_downloads: 746
---

# NocoBase Extensible AI-Powered No-Code and Low-Code Platform

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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nocobase-extensible-no-code-low-code-platform/)
