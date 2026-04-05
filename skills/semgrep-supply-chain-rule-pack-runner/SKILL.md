---
name: "Semgrep Supply Chain Rule Pack Runner"
description: "Runs Semgrep code and supply-chain checks with `semgrep scan`, registry rule packs, and dependency-aware findings to surface risky patterns early. Useful when agents need to summarize security results in repo terms developers can act on immediately."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
tool_ecosystem:
  tool: semgrep
  github_repo: semgrep/semgrep
  github_stars: 14632
---
# Semgrep Supply Chain Rule Pack Runner

Runs Semgrep code and supply-chain checks with `semgrep scan`, registry rule packs, and dependency-aware findings to surface risky patterns early. Useful when agents need to summarize security results in repo terms developers can act on immediately.

## Overview

Semgrep Supply Chain Rule Pack Runner is intended for repositories that want fast, explainable security feedback without forcing every developer to become an AppSec specialist. It works with `semgrep scan`, Semgrep registry rule packs, and dependency-aware findings to identify risky code patterns and supply-chain issues in a way that is closer to developer workflows than a traditional audit memo. That makes it useful in pull-request review, repo health checks, and pre-release validation.

The skill can group findings by severity, file, rule pack, and likely remediation path so a human reviewer gets more than a pile of raw matches. It is particularly helpful for agents that need to turn scanner output into actionable summaries for maintainers, because it can frame results in the language of code ownership, touched files, and recurring rule themes. That usually makes security review easier to prioritize.

Use this skill when you want fast static analysis grounded in Semgrep’s own rule model and when agent-generated summaries should point clearly toward fixes instead of just amplifying scanner noise.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-supply-chain-rule-pack-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-supply-chain-rule-pack-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-supply-chain-rule-pack-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-supply-chain-rule-pack-runner -a codex
```

### OpenClaw

```bash
clawhub install semgrep-supply-chain-rule-pack-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-supply-chain-rule-pack-runner/)
