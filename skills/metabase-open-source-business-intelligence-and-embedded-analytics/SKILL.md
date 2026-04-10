---
name: Metabase Open Source Business Intelligence and Embedded Analytics
description: Metabase is an open source business intelligence platform for querying
  data, building dashboards, and embedding analytics. It gives agents a real analytics
  surface for answering operational questions, creating dashboards, and wiring self-service
  reporting to databases or warehouse backends.
verification: security_reviewed
source: https://github.com/metabase/metabase
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: metabase/metabase
  github_stars: 46811
  ase_npm_package: metabase
  npm_weekly_downloads: 11
---
# Metabase Open Source Business Intelligence and Embedded Analytics

Metabase is an open source business intelligence platform maintained by the Metabase organization. The upstream repository, metabase/metabase, positions it as an easy-to-use BI and embedded analytics tool that lets teams work with data without building custom reporting interfaces from scratch. In practice, that gives agents a concrete job-to-be-done: connect to a database, ask structured questions, create charts and dashboards, share answers, and help users operationalize reporting without writing every query manually. It is also relevant for embedded analytics use cases where a product team wants to expose dashboards or saved questions inside an application.
The official documentation covers installation, setup, dashboards, SQL and GUI queries, alerts, embedding, permissions, and database connectivity. That breadth matters because it lets an agent move from initial deployment guidance into ongoing usage, such as creating dashboards for an operations review, checking whether a source system is connected, or helping a user navigate saved questions and chart configuration. The repository is actively maintained, has very strong GitHub adoption, and is clearly tied to a real upstream project with docs and releases. For ASE taxonomy purposes, Metabase fits best as a data extraction and transformation adjacent platform because it sits directly on top of databases and turns raw operational data into reusable questions, dashboards, and exports. It is a credible intake candidate for agents that support analytics workflows, reporting handoffs, lightweight BI ops, and customer-facing embedded reporting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metabase-open-source-business-intelligence-and-embedded-analytics/)
