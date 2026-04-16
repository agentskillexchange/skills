---
title: "Prometheus Alert Rule Tester"
description: "Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Tester

The Prometheus Alert Rule Tester skill validates and backtests Prometheus alerting rules before deployment to production. It uses promtool for syntax validation and rule unit testing, and the Prometheus HTTP API /api/v1/query_range endpoint to backtest rules against real historical metric data.

The testing workflow begins with promtool check rules to validate YAML syntax and PromQL expression correctness. It then runs promtool test rules with scenario files that define input metric series and expected alert firing/resolution sequences. For realistic validation, the skill queries the Prometheus query_range API with the actual PromQL expressions over historical time windows to determine how often alerts would have fired.

Alert routing validation checks Alertmanager configuration using the amtool CLI to verify that alerts route to the correct receivers based on label matchers. The skill simulates alert payloads and traces them through the routing tree, identifying potential misroutes or silenced alerts. It also validates recording rules by comparing their output against direct PromQL query results for numerical accuracy. Reports include alert firing frequency analysis, estimated notification volume, and suggested threshold adjustments based on historical metric distributions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-tester/)
