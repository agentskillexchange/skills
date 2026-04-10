---
name: ChartDB Database Schema Visualization and Diagram Editor
description: ChartDB is a web-based database diagramming editor that instantly visualizes
  your schema from a single SQL query. It supports AI-powered DDL export for cross-database
  migration, interactive schema editing, and works entirely in the browser with no
  account required.
verification: security_reviewed
source: https://github.com/chartdb/chartdb
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: chartdb/chartdb
  github_stars: 21734
---
# ChartDB Database Schema Visualization and Diagram Editor

What ChartDB Does
ChartDB turns your existing database schema into an interactive visual diagram with a single query. You run one &#8220;Smart Query&#8221; against your database (PostgreSQL, MySQL, SQLite, MariaDB, SQL Server), paste the resulting JSON into ChartDB, and get a full entity-relationship diagram. From there you can edit the schema visually, add annotations, and export DDL scripts for any target database dialect using AI-powered translation.
Why It Matters for Agents
Database schema documentation is one of those tasks that everyone knows is important but nobody wants to maintain manually. ChartDB automates the initial extraction and visualization step, and its AI export capability handles the tedious work of translating DDL between database dialects. For agents working on database migration tasks, schema documentation, or data architecture reviews, ChartDB provides structured schema data that can feed into downstream analysis.
Key Features

Single-query schema import: Run one SQL query to extract your entire schema as JSON
Multi-database support: PostgreSQL, MySQL, SQLite, MariaDB, and SQL Server
AI-powered DDL export: Generate migration scripts between database dialects using OpenAI or custom LLM endpoints
Interactive editor: Visual schema editing with drag-and-drop table positioning
No account required: Full functionality without signup — runs entirely client-side
Self-hostable: Docker deployment with optional AI capabilities via API key
Open source: AGPL-3.0 license with active community development

Integration Points
ChartDB integrates into database documentation workflows, migration planning, and architecture review processes. The Docker deployment supports environment variable configuration for AI backends, including custom OpenAI-compatible endpoints like vLLM. Schema exports produce standard DDL that can be version-controlled or fed into migration tools like dbmate or Flyway.
Install Notes
Run locally with npm install && npm run dev, or deploy via Docker: docker run -e OPENAI_API_KEY=your-key -p 8080:80 ghcr.io/chartdb/chartdb:latest. For custom LLM endpoints: set OPENAI_API_ENDPOINT and LLM_MODEL_NAME environment variables. The cloud version is available at app.chartdb.io.
Source: github.com/chartdb/chartdb

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chartdb-database-schema-visualization/)
