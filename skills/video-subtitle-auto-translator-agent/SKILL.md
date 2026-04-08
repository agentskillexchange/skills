---
title: Video Subtitle Auto-Translator
description: The Video Subtitle Auto-Translator automates multilingual subtitle creation
  for video content. It ingests SRT, VTT, ASS, and SSA subtitle formats and translates
  them using the DeepL API for European languages (with formality control) and Google
  Cloud Translation v3 API for broader language coverage including CJK languages.
  The agent preserves precise timing codes during translation, automatically adjusting
  reading speed calculations based on target language character density. It enforces
  platform-specific character limits (Netflix 42 chars/line, YouTube 32 chars) using
  intelligent line-breaking algorithms. Subtitle segmentation and merge operations
  are performed using the Aegisub CLI (aegisub-cli) for complex formatting. The translator
  handles subtitle synchronization with FFmpeg subtitle filter for hardcoding and
  the MKVToolNix mkvmerge command for soft subtitle embedding. It integrates with
  Crowdin API for collaborative translation review workflows and supports translation
  memory via TMX file import/export. Quality assurance includes back-translation verification,
  reading speed validation (15-25 chars/second), and automated QC reports using Subtitle
  Edit CLI. Batch processing supports YouTube channels via the YouTube Data API v3
  for automatic caption uploads.
verification: security_reviewed
source: https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/
category:
- Media &amp; Transcription
framework:
- Cursor
---

# Video Subtitle Auto-Translator

The Video Subtitle Auto-Translator automates multilingual subtitle creation for video content. It ingests SRT, VTT, ASS, and SSA subtitle formats and translates them using the DeepL API for European languages (with formality control) and Google Cloud Translation v3 API for broader language coverage including CJK languages. The agent preserves precise timing codes during translation, automatically adjusting reading speed calculations based on target language character density. It enforces platform-specific character limits (Netflix 42 chars/line, YouTube 32 chars) using intelligent line-breaking algorithms. Subtitle segmentation and merge operations are performed using the Aegisub CLI (aegisub-cli) for complex formatting. The translator handles subtitle synchronization with FFmpeg subtitle filter for hardcoding and the MKVToolNix mkvmerge command for soft subtitle embedding. It integrates with Crowdin API for collaborative translation review workflows and supports translation memory via TMX file import/export. Quality assurance includes back-translation verification, reading speed validation (15-25 chars/second), and automated QC reports using Subtitle Edit CLI. Batch processing supports YouTube channels via the YouTube Data API v3 for automatic caption uploads.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/)
