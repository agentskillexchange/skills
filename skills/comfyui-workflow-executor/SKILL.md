---
title: "ComfyUI Workflow Executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint."
verification: "security_reviewed"
source: "https://github.com/Comfy-Org/ComfyUI"
category:
  - "Image & Creative Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "Comfy-Org/ComfyUI"
  github_stars: 109121
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/comfyui-workflow-executor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/comfyui-workflow-executor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/comfyui-workflow-executor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/)
