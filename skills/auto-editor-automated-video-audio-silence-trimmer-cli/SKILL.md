---
name: "Auto-Editor Automated Video and Audio Silence Trimmer CLI"
description: "Auto-Editor is a command-line application that automatically edits video and audio by analyzing loudness, motion, and other signals to cut dead space. It exports to Premiere Pro, DaVinci Resolve, Final Cut Pro, ShotCut, and Kdenlive timelines."
verification: security_reviewed
source: "https://github.com/WyattBlue/auto-editor"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wyattblue/auto-editor"
  github_stars: 4089
---

# Auto-Editor Automated Video and Audio Silence Trimmer CLI

Auto-Editor is a command-line tool written in Nim and Python that performs automated first-pass editing on video and audio files. The core concept is simple: analyze media for silence, motionlessness, or other signals, then cut out the dead space automatically. This saves editors hours of tedious work trimming pauses and gaps from recordings, lectures, podcasts, and vlogs.
How It Works
Run auto-editor path/to/your/video.mp4 and it analyzes audio loudness by default (threshold configurable via --edit audio:threshold=0.04). It can also detect motion (--edit motion:threshold=0.02) or combine methods (--edit "(or audio:0.03 motion:0.06)"). The --margin flag adds padding around cuts for natural-feeling edits.
Export Formats
Auto-Editor can render the final output directly or export edit decision lists for professional NLEs: --export premiere (FCP7 XML for Premiere Pro), --export resolve (DaVinci Resolve), --export final-cut-pro, --export shotcut, --export kdenlive, and --export clip-sequence for individual clips.
Agent Integration
As a CLI tool, Auto-Editor integrates naturally into agent workflows. An agent can run it in a shell to automatically process raw recordings, apply configurable edit thresholds, and produce timeline files ready for manual review. The --cut-out and --add-in flags allow precise segment control, while --edit none or --edit all provide full manual override. Install via pip install auto-editor. The tool is in the public domain.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/auto-editor-automated-video-audio-silence-trimmer-cli/)
