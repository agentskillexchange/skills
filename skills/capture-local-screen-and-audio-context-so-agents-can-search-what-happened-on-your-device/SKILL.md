---
title: "Capture local screen and audio context so agents can search what happened on your device"
description: "Use Screenpipe when an agent needs private, local-first memory of what you saw or heard on your computer, including searchable screen text, app context, and transcripts, instead of relying on a chat-only memory layer."
verification: listed
source: "https://github.com/screenpipe/screenpipe"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "screenpipe/screenpipe"
  github_stars: 18176
  npm_package: "screenpipe"
  npm_weekly_downloads: 13200
---

# Capture local screen and audio context so agents can search what happened on your device

Use Screenpipe when the missing context lives on the user’s desktop rather than inside the chat thread. It continuously captures screen changes and audio locally, extracts OCR and accessibility text, builds searchable history, and exposes that memory to automations, pipes, and MCP-aware agents that need to recall what happened on the machine. The scope boundary is strong enough to be skill-shaped: this is a local screen-and-audio context capture workflow for agent recall and automation, not a generic personal AI product listing and not merely a meeting recorder card.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-local-screen-and-audio-context-so-agents-can-search-what-happened-on-your-device/)
