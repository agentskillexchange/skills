---
name: "dbt Model Lineage & Test Coverage Checker"
description: "Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
---

# dbt Model Lineage & Test Coverage Checker

dbt Model Lineage & Test Coverage Checker is built around dbt transformation framework. The underlying ecosystem is represented by dbt-labs/dbt-core (12,457+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like manifest.json, catalog.json, dbt run/test/build, dbt Cloud API and preserving the operational context that matters for real tasks.
For testing and review work, the skill wraps the normal dbt commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The original use case is clear: Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status. The implementation typically relies on manifest.json, catalog.json, dbt run/test/build, dbt Cloud API, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses manifest.json, catalog.json, dbt run/test/build, dbt Cloud API instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as warehouse modeling, lineage, test coverage, docs, and transformation CI.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include warehouse modeling, lineage, test coverage, docs, and transformation CI. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/)
