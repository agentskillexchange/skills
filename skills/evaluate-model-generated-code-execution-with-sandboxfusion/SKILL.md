---
name: "Evaluate model-generated code execution with SandboxFusion"
slug: "evaluate-model-generated-code-execution-with-sandboxfusion"
description: "Use SandboxFusion to run and judge LLM-generated code in controlled sandboxes across many languages and benchmark-style evaluation tasks."
github_stars: 1022
verification: "security_reviewed"
source: "https://github.com/bytedance/SandboxFusion"
author: "ByteDance"
publisher_type: "Open Source Project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bytedance/SandboxFusion"
  github_stars: 1022
---

# Evaluate model-generated code execution with SandboxFusion

Use SandboxFusion to run and judge LLM-generated code in controlled sandboxes across many languages and benchmark-style evaluation tasks.

## Prerequisites

Docker, or conda and Poetry for manual installation

## Installation

Use the upstream install or setup path that matches your environment:
- docker build -f ./scripts/Dockerfile.base -t code_sandbox:base .
- docker build -f ./scripts/Dockerfile.server -t code_sandbox:server .
- docker run -d --rm -p 8080:8080 code_sandbox:server make run-online
- conda create -n sandbox -y python=3.12

Requirements and caveats from upstream:
- Python (python, pytest)
- Python (GPU)
- **Online Judge**: Implementation of Evaluation & RL datasets that requires code running

Basic usage or getting-started notes:
- **Code Runner**: Run and return the result of a code snippet
- Build the image locally:
- sed -i '1s/.*/FROM code_sandbox:base/' ./scripts/Dockerfile.server

- Source: https://github.com/bytedance/SandboxFusion
- Extracted from upstream docs: https://raw.githubusercontent.com/bytedance/SandboxFusion/HEAD/README.md

## Documentation

- https://bytedance.github.io/SandboxFusion/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-model-generated-code-execution-with-sandboxfusion/)
