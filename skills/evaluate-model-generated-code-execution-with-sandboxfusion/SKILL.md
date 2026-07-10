---
title: "Evaluate model-generated code execution with SandboxFusion"
description: "Use SandboxFusion to run and judge LLM-generated code in controlled sandboxes across many languages and benchmark-style evaluation tasks."
verification: "security_reviewed"
source: "https://github.com/bytedance/SandboxFusion"
author: "ByteDance"
publisher_type: "Open Source Project"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bytedance/SandboxFusion"
  github_stars: 1022
---

# Evaluate model-generated code execution with SandboxFusion

Use SandboxFusion to run and judge LLM-generated code in controlled sandboxes across many languages and benchmark-style evaluation tasks.

## Prerequisites

Docker, or conda and Poetry for manual installation

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Build the Docker images from scripts/Dockerfile.base and scripts/Dockerfile.server, then run the sandbox service with make run-online; manual setup uses Python 3.12, conda, Poetry, and runtime-specific language installers.
```

## Documentation

- https://bytedance.github.io/SandboxFusion/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-model-generated-code-execution-with-sandboxfusion/)
