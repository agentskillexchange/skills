---
title: "Metabase Open Source Business Intelligence and Embedded Analytics"
description: "Metabase is an open source business intelligence platform for querying data, building dashboards, and embedding analytics. It gives agents a real analytics surface for answering operational questions, creating dashboards, and wiring self-service reporting to databases or warehouse backends."
verification: security_reviewed
source: "https://github.com/metabase/metabase"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "metabase/metabase"
  github_stars: 46828
  npm_package: "metabase"
  npm_weekly_downloads: 15
---

# Metabase Open Source Business Intelligence and Embedded Analytics

Metabase is an open source business intelligence platform maintained by the Metabase organization. The upstream repository, metabase/metabase, positions it as an easy-to-use BI and embedded analytics tool that lets teams work with data without building custom reporting interfaces from scratch. In practice, that gives agents a concrete job-to-be-done: connect to a database, ask structured questions, create charts and dashboards, share answers, and help users operationalize reporting without writing every query manually. It is also relevant for embedded analytics use cases where a product team wants to expose dashboards or saved questions inside an application.

The official documentation covers installation, setup, dashboards, SQL and GUI queries, alerts, embedding, permissions, and database connectivity. That breadth matters because it lets an agent move from initial deployment guidance into ongoing usage, such as creating dashboards for an operations review, checking whether a source system is connected, or helping a user navigate saved questions and chart configuration. The repository is actively maintained, has very strong GitHub adoption, and is clearly tied to a real upstream project with docs and releases. For ASE taxonomy purposes, Metabase fits best as a data extraction and transformation adjacent platform because it sits directly on top of databases and turns raw operational data into reusable questions, dashboards, and exports. It is a credible intake candidate for agents that support analytics workflows, reporting handoffs, lightweight BI ops, and customer-facing embedded reporting.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metabase-open-source-business-intelligence-and-embedded-analytics/)
