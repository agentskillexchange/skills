---
name: "Give text-only agents vision workflows with Agent Vision Toolkit"
slug: "give-text-only-agents-vision-workflows-with-agent-vision-toolkit"
description: "Install Agent Vision Toolkit so shell-capable coding agents can inspect screenshots, run OCR, locate UI elements, restore interfaces, and operate GUIs through repeatable local vision playbooks."
github_stars: 335
verification: "security_reviewed"
source: "https://github.com/Anionex/agent-vision-toolkit"
author: "Anionex"
publisher_type: "independent"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Anionex/agent-vision-toolkit"
  github_stars: 335
---

# Give text-only agents vision workflows with Agent Vision Toolkit

Install Agent Vision Toolkit so shell-capable coding agents can inspect screenshots, run OCR, locate UI elements, restore interfaces, and operate GUIs through repeatable local vision playbooks.

## Prerequisites

Python 3.11+, shell access, an OpenAI-compatible vision API for model-backed image tools, optional Pillow/numpy/vtracer for advanced local operations

## Installation

Install or set up from the source-backed instructions:

Configure VISION_API_KEY, VISION_BASE_URL, and VISION_MODEL in ~/.config/agent-vision-toolkit/env, then restrict that file to the current user.

git clone https://github.com/Anionex/agent-vision-toolkit.git
export PATH="$PWD/agent-vision-toolkit/bin:$PATH"

Copy agent-vision-toolkit/skills/vision-tools/ into your agent skills directory and restart the agent. Review the upstream AGENT_INSTALL.md only when adding the optional proxy or native integration for your runtime.

- Source: https://github.com/Anionex/agent-vision-toolkit

## Documentation

- https://agent-vision.anionex.me

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-text-only-agents-vision-workflows-with-agent-vision-toolkit/)
