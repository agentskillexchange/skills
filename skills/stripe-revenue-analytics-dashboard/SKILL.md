---
name: Stripe Revenue Analytics Dashboard Builder
description: Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metaba
category: Data Extraction & Transformation
framework: MCP
verification: security_reviewed
rating: 4.9
reviews: 64
source: https://agentskillexchange.com/skill/stripe-revenue-analytics-dashboard/
---

# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Overview

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard
```

### OpenClaw

```bash
openclaw install stripe-revenue-analytics-dashboard
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | MCP |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (64 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/stripe-revenue-analytics-dashboard/)*
