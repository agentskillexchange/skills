---
name: "VHS Terminal Session Recorder and GIF Generator"
description: "Create terminal session recordings as GIFs, videos, or images using VHS (charmbracelet/vhs). Write declarative .tape scripts that define typed commands, delays, and settings — then render pixel-perfect terminal demos automatically."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/charmbracelet/vhs"
tool_ecosystem:
  github_repo: "charmbracelet/vhs"
  github_stars: 19204
---
# VHS Terminal Session Recorder and GIF Generator

Create terminal session recordings as GIFs, videos, or images using VHS (charmbracelet/vhs). Write declarative .tape scripts that define typed commands, delays, and settings — then render pixel-perfect terminal demos automatically.

VHS from Charm is a CLI tool that records terminal sessions and renders them as GIF animations, MP4 videos, or WebM files. Instead of manually recording your screen, you write a declarative .tape script that specifies what commands to type, how fast to type them, when to pause, and how the terminal should be configured. VHS then executes the script in a virtual terminal and produces a recording. The project has 19,000+ GitHub stars and is actively maintained under the MIT license.

A .tape file uses a simple line-based syntax. The Type command simulates typing text with configurable speed. Enter, Space, Tab, and other key commands simulate key presses. Sleep adds delays between actions. The Output directive sets the filename and format. Configuration commands like Set FontSize, Set Width, Set Height, Set Theme, and Set Padding control the terminal appearance. VHS ships with dozens of built-in themes and supports custom color schemes.

VHS uses ffmpeg for video encoding and a headless browser for rendering, but handles all dependencies automatically. It can record any CLI application, interactive shell session, or scripted workflow. The virtual terminal supports full ANSI/256-color/truecolor rendering, making recordings look identical to a real terminal. Multiple Output directives in a single tape file can produce a GIF, an MP4, and a PNG screenshot from the same session in one run.

This skill enables agents to create professional terminal recordings for documentation, README files, blog posts, and tutorials. Agents can generate .tape scripts from natural language descriptions, preview and iterate on recordings, optimize GIF file sizes, batch-render multiple demos, and embed results in markdown documentation. The skill outputs .tape script files and rendered media (GIF, MP4, WebM, PNG).

Integration points include GitHub README documentation (animated GIFs), CI pipelines for automated demo generation, documentation sites, developer onboarding materials, and CLI tool marketing pages. VHS is installable via Homebrew, Nix, AUR, and go install. It requires ffmpeg as a runtime dependency, which is available on all major platforms.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vhs-terminal-session-recorder-gif-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vhs-terminal-session-recorder-gif-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vhs-terminal-session-recorder-gif-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vhs-terminal-session-recorder-gif-generator -a codex
```

### OpenClaw

```bash
clawhub install vhs-terminal-session-recorder-gif-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vhs-terminal-session-recorder-gif-generator/)
