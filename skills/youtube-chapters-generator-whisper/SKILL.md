---
title: YouTube Chapters Generator with Whisper
description: The YouTube Chapters Generator automates the creation of chapter markers
  for video content by combining audio transcription with topic segmentation. It downloads
  audio tracks from YouTube (or local video files) using yt-dlp with format selection
  optimized for speech (lowest bitrate audio-only). Transcription runs through OpenAI
  Whisper (local model or API) producing word-level timestamps. The transcript is
  then segmented into topical sections using the TextTiling algorithm implemented
  via NLTK, which detects topic boundaries by analyzing vocabulary distribution shifts
  across text blocks. Each detected segment becomes a chapter with an auto-generated
  title derived from TF-IDF keyword extraction of that segment’s content. Timestamps
  are snapped to sentence boundaries for clean chapter transitions. The skill outputs
  chapters in YouTube description format (00:00 Title), JSON with full metadata, and
  SRT/VTT for subtitle integration. Manual override allows editing generated chapters
  before finalizing. Batch mode processes entire playlists via yt-dlp playlist extraction.
  Quality controls include minimum chapter duration thresholds, maximum chapter count
  limits, and confidence scoring for boundary detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/
category:
- Media &amp; Transcription
framework:
- Claude Code
---

# YouTube Chapters Generator with Whisper

The YouTube Chapters Generator automates the creation of chapter markers for video content by combining audio transcription with topic segmentation. It downloads audio tracks from YouTube (or local video files) using yt-dlp with format selection optimized for speech (lowest bitrate audio-only). Transcription runs through OpenAI Whisper (local model or API) producing word-level timestamps. The transcript is then segmented into topical sections using the TextTiling algorithm implemented via NLTK, which detects topic boundaries by analyzing vocabulary distribution shifts across text blocks. Each detected segment becomes a chapter with an auto-generated title derived from TF-IDF keyword extraction of that segment’s content. Timestamps are snapped to sentence boundaries for clean chapter transitions. The skill outputs chapters in YouTube description format (00:00 Title), JSON with full metadata, and SRT/VTT for subtitle integration. Manual override allows editing generated chapters before finalizing. Batch mode processes entire playlists via yt-dlp playlist extraction. Quality controls include minimum chapter duration thresholds, maximum chapter count limits, and confidence scoring for boundary detection.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/)
