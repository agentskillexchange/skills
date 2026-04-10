---
title: "Grist Self-Hosted Relational Spreadsheet and Database Platform"
description: "Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance."
slug: "grist-self-hosted-relational-spreadsheet-database"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/gristlabs/grist-core"
tool_ecosystem:
  github_repo: "gristlabs/grist-core"
  github_stars: 10827
---

# Grist Self-Hosted Relational Spreadsheet and Database Platform

Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance.

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
clawhub install grist-self-hosted-relational-spreadsheet-database
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Grist is an open-source relational spreadsheet platform developed by Grist Labs. It bridges the gap between traditional spreadsheets and databases, giving users the formula-driven flexibility of Excel combined with the structural integrity and relational capabilities of a real database.
How It Works
Grist stores data in SQLite-based documents where columns are typed (like a database) but can be filled by formulas (like a spreadsheet). This hybrid approach means you get automatic updates when referenced cells change, while maintaining data integrity through typed columns and relational references between tables.
Key Features
Python Formulas: Full Python syntax is supported in formulas, including the standard library. This goes far beyond typical spreadsheet formula languages, enabling complex data transformations, API calls, and custom logic directly in cells.
REST API: Grist provides a comprehensive REST API for reading and writing document data, managing workspaces, and automating workflows. Agents can programmatically create, query, and modify spreadsheets, making Grist an excellent structured data backend for automation.
AI Formula Assistant: Built-in AI-powered formula generation works with OpenAI, Llama, and any OpenAI-compatible endpoint via OpenRouter. Describe what you want in natural language and get working Python formulas.
Self-Hosted: Run Grist on your own infrastructure via Docker, with full control over your data. The portable SQLite-based format means documents can be backed up, migrated, and read by any SQLite-compatible tool.
Drag-and-Drop Dashboards: Create interactive dashboards with charts, card views, calendar widgets, custom widgets, and map visualizations. Link widgets to filter data across views.
Access Control: Fine-grained permissions let you control who can see or edit specific tables, columns, or even individual rows based on user attributes.
Integration Points
The REST API enables integration with any agent framework. Incoming and outgoing webhooks support event-driven automation. Grist can import from CSV, Excel, JSON, and Google Sheets, and export to those formats plus the native .grist format.
Agent Use Cases
AI agents can use Grist as a structured data store for tracking projects, managing inventories, aggregating research data, or building dashboards. The Python formula engine and REST API make it particularly powerful for automated data processing and reporting workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grist-self-hosted-relational-spreadsheet-database/)
