---
name: "Validate Team Brain retrieval and access boundaries"
slug: "validate-team-brain-retrieval-and-access-boundaries"
description: "Run Team Brain’s seeded Oracle test-schema diagnostic and return retrieval, permission-check and setup failures before connecting real team data."
verification: "security_reviewed"
source: "https://github.com/oracle-devrel/oracle-ai-developer-hub/tree/d9ffc5eb1872ee788d2a659f0de7b1bf570c2d3c/apps/team-brain"
author: "Cole Medin (Team Brain); Oracle Developer Relations (repository)"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Validate Team Brain retrieval and access boundaries

Run Team Brain’s seeded Oracle test-schema diagnostic and return retrieval, permission-check and setup failures before connecting real team data.

## Prerequisites

Git, Python 3.12+, uv, Docker Compose v2, disposable Oracle AI Database 26ai Free container, Oracle container registry access

## Installation

Install or set up from the source-backed instructions:

Use a new checkout and a disposable local Oracle AI Database 26ai Free environment. Prerequisites: Git, Python 3.12+, uv, Docker Compose v2 with --wait, an Oracle account with the container-image licence accepted, and docker login container-registry.oracle.com completed by the operator. Ports 1521 must be free. Bootstrap downloads an approximately 117 MB ONNX model. Run: git clone https://github.com/oracle-devrel/oracle-ai-developer-hub.git cd oracle-ai-developer-hub git checkout --detach d9ffc5eb1872ee788d2a659f0de7b1bf570c2d3c cd apps/team-brain uv sync --extra dev --locked Inspect the pinned README and Compose configuration. Confirm all Oracle connection/environment settings target only the disposable container; keep TEAMBRAIN_LIVE unset and leave ORACLE_USER_TEST at TEAMBRAIN_TEST. With operator authorization to create local containers and disposable database schemas, run: docker compose up -d --wait --wait-timeout 900 uv run python scripts/bootstrap_db.py uv run team-brain doctor Bootstrap connects as SYS to create the demo and test schemas and grants. Doctor initializes and truncates the test documents before seeding fixtures. Never target existing business data. Demo passwords and tokens are for isolated local use. No MCP client or external LLM credential is required for this diagnostic workflow.

- Source: https://github.com/oracle-devrel/oracle-ai-developer-hub/tree/d9ffc5eb1872ee788d2a659f0de7b1bf570c2d3c/apps/team-brain

## Documentation

- https://github.com/oracle-devrel/oracle-ai-developer-hub/tree/d9ffc5eb1872ee788d2a659f0de7b1bf570c2d3c/apps/team-brain/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-team-brain-retrieval-and-access-boundaries/)
