---
name: "Hoppscotch Open Source API Development Ecosystem"
description: "Hoppscotch is a lightweight, open-source API development platform that serves as an alternative to Postman and Insomnia. It supports REST, GraphQL, WebSocket, SSE, MQTT, and Socket.IO protocols with a fast, browser-based interface available as PWA, desktop app, and CLI."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/hoppscotch/hoppscotch"
---
# Hoppscotch Open Source API Development Ecosystem

Hoppscotch is a lightweight, open-source API development platform that serves as an alternative to Postman and Insomnia. It supports REST, GraphQL, WebSocket, SSE, MQTT, and Socket.IO protocols with a fast, browser-based interface available as PWA, desktop app, and CLI.

## Overview

Hoppscotch is a free and open-source API development ecosystem that gives developers a fast, lightweight way to build, test, and debug APIs. Available at [github.com/hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) with over 65,000 GitHub stars, it has become one of the most popular alternatives to commercial API clients like Postman and Insomnia.

The platform supports a comprehensive set of protocols beyond standard REST calls. Developers can work with GraphQL queries with schema introspection and multi-column docs, establish WebSocket connections for full-duplex communication, consume Server-Sent Events streams, interact with MQTT brokers, and connect to Socket.IO servers. Each protocol handler is purpose-built with its own testing interface rather than being bolted on as an afterthought.

Hoppscotch provides a complete request workflow including all HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, TRACE, CONNECT, and custom methods), authorization handling (Basic, Bearer, OAuth 2.0, OIDC), request body composition with FormData and JSON, pre-request scripts, environment variables, and response inspection with syntax highlighting for JSON, XML, and HTML. Requests can be organized into unlimited nested collections and folders that sync across sessions.

The tool is available in three deployment modes: the hosted web version at hoppscotch.io, a desktop application for Windows, macOS, and Linux, and a CLI tool for headless testing in CI/CD pipelines. The CLI can run entire collections and output results in multiple formats, making it suitable for automated API testing in continuous integration workflows. All versions support theming, keyboard shortcuts, and a distraction-free Zen mode.

Developers building agent skills around API testing, endpoint validation, or integration verification can use Hoppscotch as the underlying engine for automated API interaction, collection execution, and response validation. Its open-source nature and self-hostable architecture make it particularly suitable for teams that need on-premises API tooling.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hoppscotch-api-development-ecosystem
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hoppscotch-api-development-ecosystem -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hoppscotch-api-development-ecosystem -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hoppscotch-api-development-ecosystem -a codex
```

### OpenClaw

```bash
clawhub install hoppscotch-api-development-ecosystem
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hoppscotch-api-development-ecosystem/)
