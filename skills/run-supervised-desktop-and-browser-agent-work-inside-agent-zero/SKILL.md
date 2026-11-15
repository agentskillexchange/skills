---
name: "Run supervised desktop and browser agent work inside Agent Zero"
slug: "run-supervised-desktop-and-browser-agent-work-inside-agent-zero"
description: "Use Agent Zero to give an agent an isolated Linux desktop, browser, plugins, skills, and host connector for supervised file, web, and GUI workflows."
github_stars: 17805
verification: "security_reviewed"
source: "https://github.com/agent0ai/agent-zero"
author: "Agent Zero"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "agent0ai/agent-zero"
  github_stars: 17805
---

# Run supervised desktop and browser agent work inside Agent Zero

Use Agent Zero to give an agent an isolated Linux desktop, browser, plugins, skills, and host connector for supervised file, web, and GUI workflows.

## Prerequisites

Docker or the Agent Zero installer, Agent Zero Web UI, configured LLM provider, optional plugins, MCP servers, skills, browser, desktop, and A0 CLI connector

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 80:80 -v a0_usr:/a0/usr agent0ai/agent-zero

Requirements and caveats from upstream:
- Agent Zero is an open, dynamic, organic agentic framework. One Docker container ships a full Linux system with a desktop and a plugin hub that the agent can extend using Skills.
- ### Docker already installed? Run this directly
- The Docker browser is the default live Browser surface. Browser history keeps screenshots of important steps, so older chats can still show what the agent saw. The Browser also supports Chrome extensions inside the Do...

Basic usage or getting-started notes:
- <img alt="Agent Zero driving Blender in its built-in XFCE desktop" src="docs/res/usage/webui/agentzero-xfce-computer.gif" />
- That means the agent can drive *real desktop software*: open Blender to model a 3D object, jump into a terminal window, manage files visually, run a GUI tool that has no API.
- <img alt="Annotating a webpage element in the Agent Zero browser" src="docs/res/usage/browser/annotation.gif" />

- Source: https://github.com/agent0ai/agent-zero
- Extracted from upstream docs: https://raw.githubusercontent.com/agent0ai/agent-zero/HEAD/README.md

## Documentation

- https://agent-zero.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-supervised-desktop-and-browser-agent-work-inside-agent-zero/)
