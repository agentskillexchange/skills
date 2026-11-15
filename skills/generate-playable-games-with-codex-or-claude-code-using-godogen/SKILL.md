---
name: "Generate playable games with Codex or Claude Code using Godogen"
slug: "generate-playable-games-with-codex-or-claude-code-using-godogen"
description: "Use Godogen to publish a thin game-generation repo where Codex or Claude Code builds, runs, captures, and iterates on Godot, Bevy, or Babylon.js games from a short prompt."
github_stars: 6977
verification: "security_reviewed"
source: "https://github.com/htdt/godogen"
author: "htdt"
publisher_type: "independent"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "htdt/godogen"
  github_stars: 6977
---

# Generate playable games with Codex or Claude Code using Godogen

Use Godogen to publish a thin game-generation repo where Codex or Claude Code builds, runs, captures, and iterates on Godot, Bevy, or Babylon.js games from a short prompt.

## Prerequisites

Claude Code or Codex, Godot 4 .NET or Rust/Cargo or Node.js depending on engine choice, Python, Chrome or Chromium for Babylon capture, ffmpeg, ImageMagick, optional GPU host, and optional GOOGLE_API_KEY, XAI_API_KEY, and TRIPO_API_KEY for asset generation.

## Installation

Install or set up from the source-backed instructions:

Clone the repository, install the engine and system prerequisites from setup.md, then publish a fresh runtime repo with commands such as ./publish.sh --engine godot --agent claude --out ~/my-game, ./publish.sh --engine babylon --agent codex --out ~/my-game, or ./publish.sh --engine bevy --agent claude --out ~/my-game. Run the selected coding agent inside the generated repo with the game brief.

- Source: https://github.com/htdt/godogen

## Documentation

- https://github.com/htdt/godogen

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-playable-games-with-codex-or-claude-code-using-godogen/)
