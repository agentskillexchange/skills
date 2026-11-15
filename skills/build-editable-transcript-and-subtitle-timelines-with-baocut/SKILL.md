---
name: "Build editable transcript and subtitle timelines with BaoCut"
slug: "build-editable-transcript-and-subtitle-timelines-with-baocut"
description: "Transcribe supplied media, polish timed text, add optional translated subtitles, and export deliverables while retaining a resumable, editable video project."
github_stars: 1010
verification: "security_reviewed"
source: "https://github.com/JimLiu/baocut"
author: "Jim Liu"
publisher_type: "community"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "JimLiu/baocut"
  github_stars: 1010
---

# Build editable transcript and subtitle timelines with BaoCut

Transcribe supplied media, polish timed text, add optional translated subtitles, and export deliverables while retaining a resumable, editable video project.

## Prerequisites

BaoCut packaged app and CLI; supported coding agent; ffmpeg and ffprobe; an available transcription model/provider; optional MCP-capable host; supplied media and sufficient local storage

## Installation

Install or set up from the source-backed instructions:

Download the appropriate packaged release from https://github.com/JimLiu/baocut/releases and follow its macOS or Windows setup instructions. Install ffmpeg and ffprobe separately. Install/sign in to the supported agent engine. Run baocut version and baocut status, then baocut help skill and baocut skill install following the installed version instructions. Optional MCP: after approval of the host configuration change, run baocut mcp install --agent codex --level ask (supported alternatives: claude-code, cursor, gemini), then restart the host. Configure a transcription capability in BaoCut; do not download models or enable remote providers implicitly. Load the baocut skill and subtitle-workflow craft before processing media.

- Source: https://github.com/JimLiu/baocut

## Documentation

- https://github.com/JimLiu/baocut/blob/main/skills/baocut/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-editable-transcript-and-subtitle-timelines-with-baocut/)
