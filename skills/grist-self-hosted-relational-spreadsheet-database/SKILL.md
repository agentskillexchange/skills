---
name: "Grist Self-Hosted Relational Spreadsheet and Database Platform"
description: "Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/gristlabs/grist-core"
tool_ecosystem:
  github_repo: "https://github.com/gristlabs/grist-core"
  github_stars: 10827
  license: "Apache-2.0"
---
# Grist Self-Hosted Relational Spreadsheet and Database Platform

Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance.

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

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grist-self-hosted-relational-spreadsheet-database
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grist-self-hosted-relational-spreadsheet-database -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grist-self-hosted-relational-spreadsheet-database -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grist-self-hosted-relational-spreadsheet-database -a codex
```

### OpenClaw

```bash
clawhub install grist-self-hosted-relational-spreadsheet-database
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grist-self-hosted-relational-spreadsheet-database/)
