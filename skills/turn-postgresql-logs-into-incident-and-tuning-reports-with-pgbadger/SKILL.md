---
title: "Turn PostgreSQL logs into incident and tuning reports with pgBadger"
description: "Use pgBadger when an agent needs to convert raw PostgreSQL logs into readable evidence about slow queries, errors, and workload hotspots after an incident."
verification: "listed"
source: "https://github.com/darold/pgbadger"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "darold/pgbadger"
  github_stars: 3994
---

# Turn PostgreSQL logs into incident and tuning reports with pgBadger

pgBadger gives an agent a concrete post-incident job: parse PostgreSQL logs, summarize what happened, and output reports that help humans spot slow queries, lock pain, error bursts, and tuning opportunities. Invoke it when the real need is evidence-driven diagnosis from logs, not when you just need a database client or generic monitoring dashboard. The boundary is tight and skill-shaped: PostgreSQL log analysis and reporting, not broad database administration or a plain product listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-postgresql-logs-into-incident-and-tuning-reports-with-pgbadger/)
