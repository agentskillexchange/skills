---
title: "Video Subtitle Auto-Translator"
description: "Translates video subtitles across 100+ languages using DeepL API and Google Cloud Translation v3. Handles SRT/VTT timing preservation, character limit enforcement, and subtitle segmentation with Aegisub CLI."
slug: "video-subtitle-auto-translator-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/"
listed: true
---

# Video Subtitle Auto-Translator

Translates video subtitles across 100+ languages using DeepL API and Google Cloud Translation v3. Handles SRT/VTT timing preservation, character limit enforcement, and subtitle segmentation with Aegisub CLI.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install video-subtitle-auto-translator-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Video Subtitle Auto-Translator automates multilingual subtitle creation for video content. It ingests SRT, VTT, ASS, and SSA subtitle formats and translates them using the DeepL API for European languages (with formality control) and Google Cloud Translation v3 API for broader language coverage including CJK languages. The agent preserves precise timing codes during translation, automatically adjusting reading speed calculations based on target language character density. It enforces platform-specific character limits (Netflix 42 chars/line, YouTube 32 chars) using intelligent line-breaking algorithms. Subtitle segmentation and merge operations are performed using the Aegisub CLI (aegisub-cli) for complex formatting. The translator handles subtitle synchronization with FFmpeg subtitle filter for hardcoding and the MKVToolNix mkvmerge command for soft subtitle embedding. It integrates with Crowdin API for collaborative translation review workflows and supports translation memory via TMX file import/export. Quality assurance includes back-translation verification, reading speed validation (15-25 chars/second), and automated QC reports using Subtitle Edit CLI. Batch processing supports YouTube channels via the YouTube Data API v3 for automatic caption uploads.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/)
