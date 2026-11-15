---
name: "Analyze videos with frame extraction and audio context in Claude Code"
slug: "analyze-videos-with-frame-extraction-and-audio-context-in-claude-code"
description: "Give Claude Code a video perception layer that extracts frames, transcribes audio, and lets Claude answer questions about local videos or YouTube URLs."
github_stars: 698
verification: "security_reviewed"
source: "https://github.com/jordanrendric/claude-video-vision"
author: "Jordan Rendric"
publisher_type: "individual"
category: "Media & Transcription"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "jordanrendric/claude-video-vision"
  github_stars: 698
  npm_package: "claude-video-vision"
  npm_weekly_downloads: 802
---

# Analyze videos with frame extraction and audio context in Claude Code

Give Claude Code a video perception layer that extracts frames, transcribes audio, and lets Claude answer questions about local videos or YouTube URLs.

## Prerequisites

Claude Code, Node.js 20+, ffmpeg, optional yt-dlp, Gemini API or Whisper/OpenAI audio backend

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/jordanrendric/claude-video-vision.git

Requirements and caveats from upstream:
- | **Local (Whisper)** | whisper.cpp or Python openai-whisper | Free, fully offline | brew install whisper-cpp + auto model download |
- │ MCP Server (Node.js) │
- **Node.js 20+** (for the MCP server)

Basic usage or getting-started notes:
- ### 1. Install the plugin
- Inside Claude Code, run these commands **one at a time**:
- /plugin marketplace add https://github.com/jordanrendric/claude-video-vision

- Source: https://github.com/jordanrendric/claude-video-vision
- Extracted from upstream docs: https://raw.githubusercontent.com/jordanrendric/claude-video-vision/HEAD/README.md

## Documentation

- https://github.com/jordanrendric/claude-video-vision

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/analyze-videos-with-frame-extraction-and-audio-context-in-claude-code/)
