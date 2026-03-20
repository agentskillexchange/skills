---
name: Prometheus Alert Rule Tester
description: Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing con
category: Runbooks & Diagnostics
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 34
source: https://agentskillexchange.com/skill/prometheus-alert-rule-tester/
---

# Prometheus Alert Rule Tester

Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations.

## Overview

The Prometheus Alert Rule Tester skill validates and backtests Prometheus alerting rules before deployment to production. It uses promtool for syntax validation and rule unit testing, and the Prometheus HTTP API /api/v1/query_range endpoint to backtest rules against real historical metric data.
The testing workflow begins with promtool check rules to validate YAML syntax and PromQL expression correctness. It then runs promtool test rules with scenario files that define input metric series and expected alert firing/resolution sequences. For realistic validation, the skill queries the Prometheus query_range API with the actual PromQL expressions over historical time windows to determine how often alerts would have fired.
Alert routing validation checks Alertmanager configuration using the amtool CLI to verify that alerts route to the correct receivers based on label matchers. The skill simulates alert payloads and traces them through the routing tree, identifying potential misroutes or silenced alerts. It also validates recording rules by comparing their output against direct PromQL query results for numerical accuracy. Reports include alert firing frequency analysis, estimated notification volume, and suggested threshold adjustments based on historical metric distributions.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-tester
```

### OpenClaw

```bash
openclaw install prometheus-alert-rule-tester
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (34 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/prometheus-alert-rule-tester/)*
