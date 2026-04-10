---
title: "YouTube Chapters Generator with Whisper"
description: "Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles."
slug: "youtube-chapters-generator-whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/"
listed: true
---

# YouTube Chapters Generator with Whisper

Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles.

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
clawhub install youtube-chapters-generator-whisper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The YouTube Chapters Generator automates the creation of chapter markers for video content by combining audio transcription with topic segmentation. It downloads audio tracks from YouTube (or local video files) using yt-dlp with format selection optimized for speech (lowest bitrate audio-only). Transcription runs through OpenAI Whisper (local model or API) producing word-level timestamps. The transcript is then segmented into topical sections using the TextTiling algorithm implemented via NLTK, which detects topic boundaries by analyzing vocabulary distribution shifts across text blocks. Each detected segment becomes a chapter with an auto-generated title derived from TF-IDF keyword extraction of that segment’s content. Timestamps are snapped to sentence boundaries for clean chapter transitions. The skill outputs chapters in YouTube description format (00:00 Title), JSON with full metadata, and SRT/VTT for subtitle integration. Manual override allows editing generated chapters before finalizing. Batch mode processes entire playlists via yt-dlp playlist extraction. Quality controls include minimum chapter duration thresholds, maximum chapter count limits, and confidence scoring for boundary detection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/)
