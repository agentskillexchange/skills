---
name: NocoDB Self-Hosted No-Code Database Platform with REST API
description: NocoDB turns any SQL database into a smart spreadsheet with a full REST
  API. It provides a self-hosted Airtable alternative that connects to PostgreSQL,
  MySQL, SQLite, and other databases, enabling no-code data management with automation,
  collaboration, and API-first access.
verification: security_reviewed
source: https://github.com/nocodb/nocodb
category:
- Integrations &amp; Connectors
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: nocodb/nocodb
  github_stars: 62560
  ase_npm_package: nocodb
  npm_weekly_downloads: 486
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nocodb-self-hosted-no-code-database-rest-api/)
