---
name: "Activepieces Open Source Workflow Automation"
description: "Activepieces is an open-source, self-hostable workflow automation platform with 200+ integrations. It provides a visual builder for creating automated workflows and exposes all its connectors as MCP servers for AI agent use."
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/activepieces/activepieces"
---
# Activepieces Open Source Workflow Automation

Activepieces is an open-source, self-hostable workflow automation platform with 200+ integrations. It provides a visual builder for creating automated workflows and exposes all its connectors as MCP servers for AI agent use.

## Overview

Activepieces is an open-source workflow automation platform that serves as a self-hostable alternative to Zapier and Make. With over 21,000 GitHub stars and an active TypeScript codebase, Activepieces combines a visual no-code builder with a type-safe pieces framework that makes it equally accessible to non-technical users and developers. The platform supports 200+ pre-built integrations (called “pieces”) covering services like Google Sheets, Slack, OpenAI, Discord, GitHub, Notion, Stripe, and many more.

What sets Activepieces apart in the agent ecosystem is its MCP-first architecture. Every piece in the Activepieces catalog is automatically exposed as an MCP server, meaning AI agents running in Claude Desktop, Cursor, Windsurf, or any MCP-compatible client can leverage the full library of 280+ connectors without any additional configuration. This turns Activepieces into a massive toolkit for AI agents — giving them authenticated access to hundreds of APIs through a standardized protocol. Community contributions drive 60% of the piece library, and all piece source code is open and published to npm.

The workflow builder supports standard automation primitives including loops, conditional branches, auto-retries, HTTP requests, inline code with npm package support, and AI-assisted code generation. Workflows are fully versioned, support human-in-the-loop approval steps with configurable delays, and include built-in chat and form interfaces for human input triggers. The platform offers enterprise features like white-labeling, custom branding, and role-based access control.

Deployment is flexible: Activepieces runs as a Docker container for self-hosting or is available as a managed cloud service. The piece development SDK uses TypeScript with full type safety, hot reloading for local development, and a well-documented API for creating custom integrations. For teams building AI-powered automation, Activepieces bridges the gap between visual workflow design and programmatic agent orchestration, providing a battle-tested execution engine with observability, error handling, and scheduling built in.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill activepieces-open-source-workflow-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill activepieces-open-source-workflow-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill activepieces-open-source-workflow-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill activepieces-open-source-workflow-automation -a codex
```

### OpenClaw

```bash
clawhub install activepieces-open-source-workflow-automation
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/activepieces-open-source-workflow-automation/)
