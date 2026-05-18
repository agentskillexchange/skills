---
name: "Generate podcast-style audio narratives with Podcast Generation"
slug: "generate-podcast-style-audio-narratives-with-podcast-generation"
description: "Build a repeatable text-to-audio workflow around Azure OpenAI Realtime streaming, PCM collection, WAV conversion, and frontend playback for podcast-style output."
verification: "listed"
source: "https://github.com/microsoft/skills/tree/main/.github/skills/podcast-generation"
author: "Microsoft"
publisher_type: "organization"
category: "Media & Transcription"
framework: "Multi-Framework"
---

# Generate podcast-style audio narratives with Podcast Generation

Build a repeatable text-to-audio workflow around Azure OpenAI Realtime streaming, PCM collection, WAV conversion, and frontend playback for podcast-style output.

## Prerequisites

Azure OpenAI Realtime API access, WebSocket-capable backend, PCM to WAV conversion, frontend audio playback layer

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add microsoft/skills
- git clone https://github.com/microsoft/skills.git
- pnpm install
- pnpm harness --list

Requirements and caveats from upstream:
- | [Python](#python) | 39 | -py |
- ├── plugins/ # Language-based plugin bundles (azure-sdk-python, etc.)
- ├── python/ # -> ../.github/skills/*-py

Basic usage or getting-started notes:
- bash
- Select the skills you need from the wizard. Skills are installed to your chosen agent's directory (e.g., .github/skills/ for GitHub Copilot) and symlinked if you use multiple agents.
- <details>

- Source: https://github.com/microsoft/skills/tree/main/.github/skills/podcast-generation
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/skills/HEAD/README.md

## Documentation

- https://microsoft.github.io/skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-podcast-style-audio-narratives-with-podcast-generation/)
