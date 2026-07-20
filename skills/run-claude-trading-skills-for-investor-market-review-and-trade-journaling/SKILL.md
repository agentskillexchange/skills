---
name: "Run Claude Trading Skills for investor market review and trade journaling"
slug: "run-claude-trading-skills-for-investor-market-review-and-trade-journaling"
description: "Use the Claude Trading Skills pack to run structured market-regime checks, portfolio reviews, swing-trade screens, trade journals, and performance retrospectives inside Claude workflows."
github_stars: 2450
verification: "security_reviewed"
source: "https://github.com/tradermonty/claude-trading-skills"
author: "tradermonty"
publisher_type: "community"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "tradermonty/claude-trading-skills"
  github_stars: 2450
---

# Run Claude Trading Skills for investor market review and trade journaling

Use the Claude Trading Skills pack to run structured market-regime checks, portfolio reviews, swing-trade screens, trade journals, and performance retrospectives inside Claude workflows.

## Prerequisites

Claude Skills or Claude Code, local portfolio/trading files, optional FMP/FINVIZ Elite/Alpaca data integrations depending on workflow

## Installation

Requirements and caveats from upstream:
- | Weekly long-term portfolio review | [core-portfolio-weekly](workflows/core-portfolio-weekly.yaml) | portfolio-manager, kanchi-dividend-review-monitor, trader-memory-core | Alpaca required; manual CSV is a degraded f...
- skillsets/ – Purpose-specific install bundles defining required / recommended / optional skills for major goals (4 core skillsets shipped: market-regime, core-portfolio, swing-opportunity, trade-memory; consumed by th...
- | **FTD Detector** (ftd-detector) | Detects Follow-Through Day (FTD) signals for market bottom confirmation using William O'Neil's methodology. | fmp **required** | production |

Basic usage or getting-started notes:
- This repository is for educational, research, and process-improvement purposes only. It is not financial advice, investment advisory service, tax advice, legal advice, a signal service, or a broker execution platform....
- See [workflows/README.md](workflows/README.md) for how to read a manifest and run it manually. For a one-page "which workflow fits my situation?" guide, see [Find Your Workflow](docs/en/find-your-workflow.md) ([日本語](d...
- If you do not have FMP / FINVIZ / Alpaca subscriptions, start with these five skills and run them manually:

- Source: https://github.com/tradermonty/claude-trading-skills
- Extracted from upstream docs: https://raw.githubusercontent.com/tradermonty/claude-trading-skills/HEAD/README.md

## Documentation

- https://tradermonty.github.io/claude-trading-skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-trading-skills-for-investor-market-review-and-trade-journaling/)
