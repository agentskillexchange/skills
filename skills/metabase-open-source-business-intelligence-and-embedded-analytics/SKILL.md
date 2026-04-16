---
title: "Metabase Open Source Business Intelligence and Embedded Analytics"
description: "Metabase is an open source business intelligence platform for querying data, building dashboards, and embedding analytics. It gives agents a real analytics surface for answering operational questions, creating dashboards, and wiring self-service reporting to databases or warehouse backends."
verification: "security_reviewed"
source: "https://github.com/metabase/metabase"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "metabase/metabase"
  github_stars: 46828
  ase_npm_package: "metabase"
  npm_weekly_downloads: 15
---

# Metabase Open Source Business Intelligence and Embedded Analytics

Metabase is an open source business intelligence platform maintained by the Metabase organization. The upstream repository, metabase/metabase, positions it as an easy-to-use BI and embedded analytics tool that lets teams work with data without building custom reporting interfaces from scratch. In practice, that gives agents a concrete job-to-be-done: connect to a database, ask structured questions, create charts and dashboards, share answers, and help users operationalize reporting without writing every query manually. It is also relevant for embedded analytics use cases where a product team wants to expose dashboards or saved questions inside an application.

The official documentation covers installation, setup, dashboards, SQL and GUI queries, alerts, embedding, permissions, and database connectivity. That breadth matters because it lets an agent move from initial deployment guidance into ongoing usage, such as creating dashboards for an operations review, checking whether a source system is connected, or helping a user navigate saved questions and chart configuration. The repository is actively maintained, has very strong GitHub adoption, and is clearly tied to a real upstream project with docs and releases. For ASE taxonomy purposes, Metabase fits best as a data extraction and transformation adjacent platform because it sits directly on top of databases and turns raw operational data into reusable questions, dashboards, and exports. It is a credible intake candidate for agents that support analytics workflows, reporting handoffs, lightweight BI ops, and customer-facing embedded reporting.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metabase-open-source-business-intelligence-and-embedded-analytics/)
