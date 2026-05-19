---
name: "Heisenberg Supply Chain Health Checker"
slug: "heisenberg-supply-chain-health-checker"
description: "An open-source software supply chain health check tool that analyzes dependencies using deps.dev, SBOMs, and external advisories. Heisenberg generates health scores, detects risky packages, and produces CSV reports for individual dependencies or entire GitHub organization portfolios."
github_stars: 123
verification: "security_reviewed"
source: "https://github.com/AppOmni-Labs/heisenberg-ssc-health-check"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "AppOmni-Labs/heisenberg-ssc-health-check"
  github_stars: 123
---

# Heisenberg Supply Chain Health Checker

An open-source software supply chain health check tool that analyzes dependencies using deps.dev, SBOMs, and external advisories. Heisenberg generates health scores, detects risky packages, and produces CSV reports for individual dependencies or entire GitHub organization portfolios.

## Installation

Use the upstream install or setup path that matches your environment:
- # 2. Install with pipx [if you don't want to install keep reading]
- pipx install "git+https://github.com/AppOmni-Labs/heisenberg-ssc-health-check"
- git clone https://github.com/AppOmni-Labs/heisenberg-ssc-health-check
- pip install -e .

Requirements and caveats from upstream:
- Heisenberg requires python 3.11.
- If you do not wish to install the tool you can just clone it and run it directly with python
- python -m heisenberg.main sbom -r my_repo

Basic usage or getting-started notes:
- bash
- # 1. Set up your GitHub token
- export GITHUB_TOKEN=ghp_YOUR_TOKEN

- Source: https://github.com/AppOmni-Labs/heisenberg-ssc-health-check
- Extracted from upstream docs: https://raw.githubusercontent.com/AppOmni-Labs/heisenberg-ssc-health-check/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/heisenberg-supply-chain-health-checker/)
