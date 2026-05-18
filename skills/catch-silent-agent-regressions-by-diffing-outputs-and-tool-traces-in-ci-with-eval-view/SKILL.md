---
name: "Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view"
slug: "catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view"
description: "Snapshot agent behavior, compare outputs and tool-call paths, and block releases when a model or prompt change quietly shifts behavior."
github_stars: 84
verification: "listed"
source: "https://github.com/hidai25/eval-view"
author: "hidai25"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hidai25/eval-view"
  github_stars: 84
---

# Catch silent agent regressions by diffing outputs and tool traces in CI with eval-view

Snapshot agent behavior, compare outputs and tool-call paths, and block releases when a model or prompt change quietly shifts behavior.

## Prerequisites

Python environment, eval-view installation, repeatable agent scenarios or tests, CI runner or local shell, supported agent stack under test

## Installation

Basic usage or getting-started notes:
- **The loop closes:** detection → investigation → graded verdict → quarantine governance → broadcast. You wake up, run progress, triage with drift, confirm with check --statistical, and the team sees the digest before...
- | 📉 **DRIFTING** | Trend sliding with graded confidence (low/med/high) | Run evalview drift <test> |
- | 🔎 **INVESTIGATE** | Verdict layer wants statistical replay | Run evalview check --statistical 5 |

- Source: https://github.com/hidai25/eval-view
- Extracted from upstream docs: https://raw.githubusercontent.com/hidai25/eval-view/HEAD/README.md

## Documentation

- https://github.com/hidai25/eval-view

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-silent-agent-regressions-by-diffing-outputs-and-tool-traces-in-ci-with-eval-view/)
