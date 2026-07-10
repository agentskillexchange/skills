---
title: "Generate local subtitles for video editing workflows with Auto Subs"
description: "Use Auto Subs when an operator or media agent needs local-first subtitle generation, editing, and handoff into DaVinci Resolve, Premiere Pro, After Effects, or a command-line video pipeline."
verification: "security_reviewed"
source: "https://github.com/tmoroney/auto-subs"
author: "Tom Moroney"
publisher_type: "individual"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tmoroney/auto-subs"
  github_stars: 3649
---

# Generate local subtitles for video editing workflows with Auto Subs

Use Auto Subs when an operator or media agent needs local-first subtitle generation, editing, and handoff into DaVinci Resolve, Premiere Pro, After Effects, or a command-line video pipeline.

## Prerequisites

Auto Subs desktop app or CLI, local media files, and optionally DaVinci Resolve, Adobe Premiere Pro, or Adobe After Effects for editor integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Auto Subs from the platform installer listed in the project README, or on macOS run brew install --cask auto-subs. For editor workflows, open DaVinci Resolve and launch Workspace -> Scripts -> AutoSubs, or open Premiere Pro / After Effects and use the bundled CEP extension. For automation, follow the repository's CLI guide to transcribe media and export subtitle assets from the command line.
```

## Documentation

- https://tom-moroney.com/auto-subs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-local-subtitles-for-video-editing-workflows-with-auto-subs/)
