---
title: "VHS Terminal Session Recorder and GIF Generator"
description: "Create terminal session recordings as GIFs, videos, or images using VHS (charmbracelet/vhs). Write declarative .tape scripts that define typed commands, delays, and settings — then render pixel-perfect terminal demos automatically."
verification: security_reviewed
source: "https://github.com/charmbracelet/vhs"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "charmbracelet/vhs"
  github_stars: 19204
---

# VHS Terminal Session Recorder and GIF Generator

VHS from Charm is a CLI tool that records terminal sessions and renders them as GIF animations, MP4 videos, or WebM files. Instead of manually recording your screen, you write a declarative .tape script that specifies what commands to type, how fast to type them, when to pause, and how the terminal should be configured. VHS then executes the script in a virtual terminal and produces a recording. The project has 19,000+ GitHub stars and is actively maintained under the MIT license.

A .tape file uses a simple line-based syntax. The Type command simulates typing text with configurable speed. Enter, Space, Tab, and other key commands simulate key presses. Sleep adds delays between actions. The Output directive sets the filename and format. Configuration commands like Set FontSize, Set Width, Set Height, Set Theme, and Set Padding control the terminal appearance. VHS ships with dozens of built-in themes and supports custom color schemes.

VHS uses ffmpeg for video encoding and a headless browser for rendering, but handles all dependencies automatically. It can record any CLI application, interactive shell session, or scripted workflow. The virtual terminal supports full ANSI/256-color/truecolor rendering, making recordings look identical to a real terminal. Multiple Output directives in a single tape file can produce a GIF, an MP4, and a PNG screenshot from the same session in one run.

This skill enables agents to create professional terminal recordings for documentation, README files, blog posts, and tutorials. Agents can generate .tape scripts from natural language descriptions, preview and iterate on recordings, optimize GIF file sizes, batch-render multiple demos, and embed results in markdown documentation. The skill outputs .tape script files and rendered media (GIF, MP4, WebM, PNG).

Integration points include GitHub README documentation (animated GIFs), CI pipelines for automated demo generation, documentation sites, developer onboarding materials, and CLI tool marketing pages. VHS is installable via Homebrew, Nix, AUR, and go install. It requires ffmpeg as a runtime dependency, which is available on all major platforms.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vhs-terminal-session-recorder-gif-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/vhs-terminal-session-recorder-gif-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vhs-terminal-session-recorder-gif-generator/)
