---
name: "Auto-Editor Automated Video and Audio Silence Trimmer CLI"
description: "Auto-Editor is a command-line application that automatically edits video and audio by analyzing loudness, motion, and other signals to cut dead space. It exports to Premiere Pro, DaVinci Resolve, Final Cut Pro, ShotCut, and Kdenlive timelines."
category: "Media & Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/WyattBlue/auto-editor"
tool_ecosystem:
  tool: auto-editor
  github_repo: wyattblue/auto-editor
  github_stars: 4081
  license: Unlicense
  maintained: true
---
# Auto-Editor Automated Video and Audio Silence Trimmer CLI

Auto-Editor is a command-line application that automatically edits video and audio by analyzing loudness, motion, and other signals to cut dead space. It exports to Premiere Pro, DaVinci Resolve, Final Cut Pro, ShotCut, and Kdenlive timelines.

## Overview

Auto-Editor is a command-line tool written in Nim and Python that performs automated first-pass editing on video and audio files. The core concept is simple: analyze media for silence, motionlessness, or other signals, then cut out the dead space automatically. This saves editors hours of tedious work trimming pauses and gaps from recordings, lectures, podcasts, and vlogs.

How It Works

Run `auto-editor path/to/your/video.mp4` and it analyzes audio loudness by default (threshold configurable via `--edit audio:threshold=0.04`). It can also detect motion (`--edit motion:threshold=0.02`) or combine methods (`--edit "(or audio:0.03 motion:0.06)"`). The `--margin` flag adds padding around cuts for natural-feeling edits.

Export Formats

Auto-Editor can render the final output directly or export edit decision lists for professional NLEs: `--export premiere` (FCP7 XML for Premiere Pro), `--export resolve` (DaVinci Resolve), `--export final-cut-pro`, `--export shotcut`, `--export kdenlive`, and `--export clip-sequence` for individual clips.

Agent Integration

As a CLI tool, Auto-Editor integrates naturally into agent workflows. An agent can run it in a shell to automatically process raw recordings, apply configurable edit thresholds, and produce timeline files ready for manual review. The `--cut-out` and `--add-in` flags allow precise segment control, while `--edit none` or `--edit all` provide full manual override. Install via `pip install auto-editor`. The tool is in the public domain.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill auto-editor-automated-video-audio-silence-trimmer-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill auto-editor-automated-video-audio-silence-trimmer-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill auto-editor-automated-video-audio-silence-trimmer-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill auto-editor-automated-video-audio-silence-trimmer-cli -a codex
```

### OpenClaw

```bash
clawhub install auto-editor-automated-video-audio-silence-trimmer-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/auto-editor-automated-video-audio-silence-trimmer-cli/)
