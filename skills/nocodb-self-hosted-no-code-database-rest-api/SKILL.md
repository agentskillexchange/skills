---
title: "NocoDB Self-Hosted No-Code Database Platform with REST API"
description: "NocoDB turns any SQL database into a smart spreadsheet with a full REST API. It provides a self-hosted Airtable alternative that connects to PostgreSQL, MySQL, SQLite, and other databases, enabling no-code data management with automation, collaboration, and API-first access."
slug: "nocodb-self-hosted-no-code-database-rest-api"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/nocodb/nocodb"
tool_ecosystem:
  github_repo: "nocodb/nocodb"
  github_stars: 62560
  npm_package: "nocodb"
  npm_weekly_downloads: 486
listed: true
---

# NocoDB Self-Hosted No-Code Database Platform with REST API

NocoDB turns any SQL database into a smart spreadsheet with a full REST API. It provides a self-hosted Airtable alternative that connects to PostgreSQL, MySQL, SQLite, and other databases, enabling no-code data management with automation, collaboration, and API-first access.

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
clawhub install nocodb-self-hosted-no-code-database-rest-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
NocoDB is an open-source platform that transforms any relational database into a collaborative spreadsheet interface with a comprehensive REST API. With over 62,000 GitHub stars, it has become the leading self-hosted alternative to Airtable, giving teams full control over their data while providing the ease of a no-code spreadsheet UI.
How It Works
NocoDB sits on top of your existing database (PostgreSQL, MySQL, MariaDB, SQLite, or SQL Server) and generates a spreadsheet-like interface automatically. Every table, view, and record is also accessible through a full-featured REST API, making it ideal for both human users and AI agents that need programmatic database access.
Key Capabilities
The platform supports multiple view types including Grid, Gallery, Kanban, Form, and Calendar views. It offers rich field types such as attachments, checkboxes, multi-select, links between tables, lookups, rollups, and formulas. Built-in automation features allow webhook triggers, scheduled actions, and custom logic flows.
Agent Integration
For AI agents and coding assistants, NocoDB provides a complete REST API with Swagger documentation. Agents can create, read, update, and delete records; manage table schemas; configure views and filters; and trigger automations through standard HTTP calls. The API supports authentication via tokens, making it straightforward to integrate into agent workflows.
Deployment
NocoDB can be deployed with a single Docker command (docker run nocodb/nocodb) or through the auto-upstall script for production setups with PostgreSQL, Redis, Minio, and Traefik. Binary downloads are available for macOS, Linux, and Windows for local testing.
Collaboration and Security
The platform supports role-based access control, shared views with password protection, audit logs, and SSO integration. Multiple users can collaborate in real-time on the same base, making it suitable for team environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nocodb-self-hosted-no-code-database-rest-api/)
