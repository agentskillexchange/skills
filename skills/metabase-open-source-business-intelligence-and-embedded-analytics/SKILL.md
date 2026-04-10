---
title: "Metabase Open Source Business Intelligence and Embedded Analytics"
description: "Metabase is an open source business intelligence platform for querying data, building dashboards, and embedding analytics. It gives agents a real analytics surface for answering operational questions, creating dashboards, and wiring self-service reporting to databases or warehouse backends."
slug: "metabase-open-source-business-intelligence-and-embedded-analytics"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/metabase/metabase"
tool_ecosystem:
  github_repo: "metabase/metabase"
  github_stars: 46811
  npm_package: "metabase"
  npm_weekly_downloads: 11
listed: true
---

# Metabase Open Source Business Intelligence and Embedded Analytics

Metabase is an open source business intelligence platform for querying data, building dashboards, and embedding analytics. It gives agents a real analytics surface for answering operational questions, creating dashboards, and wiring self-service reporting to databases or warehouse backends.

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
clawhub install metabase-open-source-business-intelligence-and-embedded-analytics
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Metabase is an open source business intelligence platform maintained by the Metabase organization. The upstream repository, metabase/metabase, positions it as an easy-to-use BI and embedded analytics tool that lets teams work with data without building custom reporting interfaces from scratch. In practice, that gives agents a concrete job-to-be-done: connect to a database, ask structured questions, create charts and dashboards, share answers, and help users operationalize reporting without writing every query manually. It is also relevant for embedded analytics use cases where a product team wants to expose dashboards or saved questions inside an application.
The official documentation covers installation, setup, dashboards, SQL and GUI queries, alerts, embedding, permissions, and database connectivity. That breadth matters because it lets an agent move from initial deployment guidance into ongoing usage, such as creating dashboards for an operations review, checking whether a source system is connected, or helping a user navigate saved questions and chart configuration. The repository is actively maintained, has very strong GitHub adoption, and is clearly tied to a real upstream project with docs and releases. For ASE taxonomy purposes, Metabase fits best as a data extraction and transformation adjacent platform because it sits directly on top of databases and turns raw operational data into reusable questions, dashboards, and exports. It is a credible intake candidate for agents that support analytics workflows, reporting handoffs, lightweight BI ops, and customer-facing embedded reporting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metabase-open-source-business-intelligence-and-embedded-analytics/)
