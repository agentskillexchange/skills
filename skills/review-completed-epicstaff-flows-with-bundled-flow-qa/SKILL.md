---
name: "Review completed EpicStaff flows with the bundled Flow QA skill"
slug: "review-completed-epicstaff-flows-with-bundled-flow-qa"
description: "Review a completed EpicStaff graph with flow-qa and return static findings for wiring, variable paths and node contracts."
verification: "security_reviewed"
source: "https://github.com/EpicStaff/EpicStaff/blob/d304a01d8c392aa4dafe5f8c2a68bd72f7838c4a/src/django_app/tables/services/flow_assistant/skills/flow-qa/SKILL.md"
author: "EpicStaff"
publisher_type: "Organization"
category: "Code Quality & Review"
framework: "Custom Agents"
---

# Review completed EpicStaff flows with the bundled Flow QA skill

Review a completed EpicStaff graph with flow-qa and return static findings for wiring, variable paths and node contracts.

## Prerequisites

EpicStaff Flow Assistant; list_skills; load_skill; get_flow_overview; get_node; get_edges_from; get_edges_to; list_node_types

## Installation

Install or set up from the source-backed instructions:

Use an EpicStaff deployment containing the bundled flow-qa skill. Open the target flow in Flow Assistant, call list_skills, then load_skill(name="flow-qa") when listed. No separate npm package or MCP server is required. For a new deployment, follow the upstream README setup for the selected version; production configuration differs from development defaults.

- Source: https://github.com/EpicStaff/EpicStaff/blob/d304a01d8c392aa4dafe5f8c2a68bd72f7838c4a/src/django_app/tables/services/flow_assistant/skills/flow-qa/SKILL.md

## Documentation

- https://github.com/EpicStaff/EpicStaff/blob/d304a01d8c392aa4dafe5f8c2a68bd72f7838c4a/src/django_app/tables/services/flow_assistant/skills/flow-qa/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-completed-epicstaff-flows-with-bundled-flow-qa/)
