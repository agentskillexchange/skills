---
name: "YouTube Chapters Generator with Whisper"
description: "Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles."
category: "Media & Transcription"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96570  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# YouTube Chapters Generator with Whisper

Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles.

## Overview

The YouTube Chapters Generator automates the creation of chapter markers for video content by combining audio transcription with topic segmentation. It downloads audio tracks from YouTube (or local video files) using yt-dlp with format selection optimized for speech (lowest bitrate audio-only). Transcription runs through OpenAI Whisper (local model or API) producing word-level timestamps. The transcript is then segmented into topical sections using the TextTiling algorithm implemented via NLTK, which detects topic boundaries by analyzing vocabulary distribution shifts across text blocks. Each detected segment becomes a chapter with an auto-generated title derived from TF-IDF keyword extraction of that segment’s content. Timestamps are snapped to sentence boundaries for clean chapter transitions. The skill outputs chapters in YouTube description format (00:00 Title), JSON with full metadata, and SRT/VTT for subtitle integration. Manual override allows editing generated chapters before finalizing. Batch mode processes entire playlists via yt-dlp playlist extraction. Quality controls include minimum chapter duration thresholds, maximum chapter count limits, and confidence scoring for boundary detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill youtube-chapters-generator-whisper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill youtube-chapters-generator-whisper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill youtube-chapters-generator-whisper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill youtube-chapters-generator-whisper -a codex
```

### OpenClaw

```bash
clawhub install youtube-chapters-generator-whisper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/
