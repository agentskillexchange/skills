---
title: "Scan LLM-generated code before use with CodeShield"
slug: "scan-llm-generated-code-before-use-with-codeshield"
description: "Run CodeShield on model-produced code or command suggestions before they reach a user, a repo, or an execution step, so insecure patterns get blocked or warned on first."
verification: "security_reviewed"
source: "https://github.com/meta-llama/PurpleLlama/tree/main/CodeShield"
author: "Meta Purple Llama"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
---

# Scan LLM-generated code before use with CodeShield

Run CodeShield on model-produced code or command suggestions before they reach a user, a repo, or an execution step, so insecure patterns get blocked or warned on first.

## Prerequisites

CodeShield integrated into an LLM output pipeline or coding assistant workflow

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the CodeShield repository instructions and notebook examples in the Purple Llama CodeShield directory, then insert CodeShield into the path where generated code is scanned before it is surfaced or executed.
```

## Documentation

- https://github.com/meta-llama/PurpleLlama/tree/main/CodeShield

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-llm-generated-code-before-use-with-codeshield/)
