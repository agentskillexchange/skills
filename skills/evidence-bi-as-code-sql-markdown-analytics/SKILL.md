---
title: "Evidence BI-as-Code SQL and Markdown Analytics Framework"
description: "Evidence is an open-source framework for building data products with SQL and Markdown. It generates interactive dashboards and reports as static sites, providing a code-driven alternative to drag-and-drop BI tools with version control and reproducibility built in."
verification: "security_reviewed"
source: "https://github.com/evidence-dev/evidence"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "evidence-dev/evidence"
  github_stars: 6116
---

# Evidence BI-as-Code SQL and Markdown Analytics Framework

Evidence is an open-source business intelligence framework that treats analytics reports as code. Available at github.com/evidence-dev/evidence, it enables data teams to build interactive dashboards, reports, and decision-support tools by writing SQL queries embedded in Markdown files rather than dragging components in a visual editor. The workflow is straightforward: developers write Markdown pages containing SQL statements that query connected data sources. Evidence executes those queries and renders the results as charts, tables, and interactive visualizations. The framework supports templated pages that generate many output pages from a single template, control flow with loops and if/else conditionals, and a component library for common chart types including bar, line, scatter, area, and funnel charts. Each page becomes a route in a generated web application. Evidence connects to most modern data warehouses and databases out of the box, including PostgreSQL, BigQuery, Snowflake, DuckDB, MySQL, SQLite, Databricks, and ClickHouse. Because reports are just Markdown files in a Git repository, teams get version control, code review, branching, and CI/CD for their analytics work. Changes to dashboards go through the same pull request process as application code changes. The generated output is a static site that can deploy to Netlify, Vercel, GitHub Pages, or any static hosting platform. This means dashboards load fast and scale without managing a BI server. Evidence also provides a VS Code extension for a rich editing experience with live preview. An agent skill wrapping Evidence enables automated report generation from data sources, dashboard scaffolding, query optimization review, and deployment pipeline integration. The skill can compose Markdown pages with embedded SQL, configure data source connections, and trigger builds. Evidence is MIT-licensed and actively maintained.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/evidence-bi-as-code-sql-markdown-analytics/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/evidence-bi-as-code-sql-markdown-analytics
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/evidence-bi-as-code-sql-markdown-analytics`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evidence-bi-as-code-sql-markdown-analytics/)
