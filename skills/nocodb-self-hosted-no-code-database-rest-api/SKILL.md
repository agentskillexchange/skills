---
title: "NocoDB Self-Hosted No-Code Database Platform with REST API"
description: "Overview\nNocoDB is an open-source platform that transforms any relational database into a collaborative spreadsheet interface with a comprehensive REST API. With over 62,000 GitHub stars, it has become the leading self-hosted alternative to Airtable, giving teams full control over their data while providing the ease of a no-code spreadsheet UI.\nHow It Works\nNocoDB sits on top of your existing database (PostgreSQL, MySQL, MariaDB, SQLite, or SQL Server) and generates a spreadsheet-like interface automatically. Every table, view, and record is also accessible through a full-featured REST API, making it ideal for both human users and AI agents that need programmatic database access.\nKey Capabilities\nThe platform supports multiple view types including Grid, Gallery, Kanban, Form, and Calendar views. It offers rich field types such as attachments, checkboxes, multi-select, links between tables, lookups, rollups, and formulas. Built-in automation features allow webhook triggers, scheduled actions, and custom logic flows.\nAgent Integration\nFor AI agents and coding assistants, NocoDB provides a complete REST API with Swagger documentation. Agents can create, read, update, and delete records; manage table schemas; configure views and filters; and trigger automations through standard HTTP calls. The API supports authentication via tokens, making it straightforward to integrate into agent workflows.\nDeployment\nNocoDB can be deployed with a single Docker command (docker run nocodb/nocodb) or through the auto-upstall script for production setups with PostgreSQL, Redis, Minio, and Traefik. Binary downloads are available for macOS, Linux, and Windows for local testing.\nCollaboration and Security\nThe platform supports role-based access control, shared views with password protection, audit logs, and SSO integration. Multiple users can collaborate in real-time on the same base, making it suitable for team environments."
verification: security_reviewed
source: "https://github.com/nocodb/nocodb"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nocodb/nocodb"
  github_stars: 62560
  ase_npm_package: "nocodb"
  npm_weekly_downloads: 682
---

# NocoDB Self-Hosted No-Code Database Platform with REST API

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nocodb-self-hosted-no-code-database-rest-api
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/nocodb-self-hosted-no-code-database-rest-api` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nocodb-self-hosted-no-code-database-rest-api/)
