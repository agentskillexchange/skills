---
title: "Verify agent policy coverage and risky-action guardrails before production rollout with Agent Governance Toolkit"
description: "Run deterministic governance checks and policy verification before agents get real autonomy, so risky tool use and weak runtime evidence are caught early."
verification: "security_reviewed"
source: "https://github.com/microsoft/agent-governance-toolkit"
author: "Microsoft"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/agent-governance-toolkit"
  github_stars: 1056
  npm_package: "agent-governance-toolkit"
  npm_weekly_downloads: 20863
---

# Verify agent policy coverage and risky-action guardrails before production rollout with Agent Governance Toolkit

Run deterministic governance checks and policy verification before agents get real autonomy, so risky tool use and weak runtime evidence are caught early.

## Prerequisites

Python environment or supported SDK runtime, Agent Governance Toolkit CLI or SDK, policy definitions, target agent workflow, optional runtime evidence JSON for verification

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the toolkit from the upstream package instructions, run agt doctor to confirm the environment, then use agt verify and the documented SDK or policy flows against the target agent workflow.
```

## Documentation

- https://github.com/microsoft/agent-governance-toolkit

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-agent-policy-coverage-and-risky-action-guardrails-before-production-rollout-with-agent-governance-toolkit/)
