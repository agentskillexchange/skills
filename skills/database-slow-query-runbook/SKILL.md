---
name: "Database Slow Query Runbook"
description: "Use this skill to identify and fix slow database queries through systematic analysis of query execution plans, indexes, and database performance metrics. It walks through EXPLAIN/EXPLAIN ANALYZE output and recommends optimizations. Trigger when database queries are slow, timeouts are occurring, or database CPU/IO is spiking."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/database-slow-query-runbook/"
---

# Database Slow Query Runbook

Use this skill to identify and fix slow database queries through systematic analysis of query execution plans, indexes, and database performance metrics. It walks through EXPLAIN/EXPLAIN ANALYZE output and recommends optimizations. Trigger when database queries are slow, timeouts are occurring, or database CPU/IO is spiking.

## Overview

Use this skill to identify and fix slow database queries through systematic analysis of query execution plans, indexes, and database performance metrics. It walks through EXPLAIN/EXPLAIN ANALYZE output and recommends optimizations. Trigger when database queries are slow, timeouts are occurring, or database CPU/IO is spiking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill database-slow-query-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill database-slow-query-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill database-slow-query-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill database-slow-query-runbook -a codex
```

### OpenClaw

```bash
clawhub install database-slow-query-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/database-slow-query-runbook/
