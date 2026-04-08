---
title: Video Subtitle Translator Agent
description: Video Subtitle Translator Agent handles the complete subtitle localization
  workflow from extraction through translation to re-embedding. It uses FFmpeg’s -map
  0:s:0 flag to extract subtitle streams from MKV, MP4, and other containers, detecting
  the subtitle codec (SRT, ASS, WebVTT) and converting to a normalized SRT format
  for processing. Translation routes through either the DeepL API for European languages
  with superior fluency or Google Cloud Translation v3 for broader language coverage
  including CJK and Indic scripts. Source language is auto-detected using the langdetect
  Python library when not specified. The translator preserves SRT timing codes and
  handles multi-line subtitle blocks by joining them for translation context, then
  re-splitting to match the original line structure. For RTL languages like Arabic
  and Hebrew, the agent inserts proper Unicode bidirectional marks and validates rendering
  through a test frame extraction with FFmpeg’s subtitles filter. Re-embedding uses
  FFmpeg’s -c:s mov_text for MP4 containers or -c:s srt for MKV, with proper language
  metadata tags set via -metadata:s:s:0 language=ara. Batch processing handles entire
  video libraries by scanning directories, detecting existing subtitle tracks, and
  generating missing translations based on a target language configuration list.
verification: security_reviewed
source: https://github.com/FFmpeg/FFmpeg
category:
- Media &amp; Transcription
framework:
- Gemini
tool_ecosystem:
  github_repo: FFmpeg/FFmpeg
  github_stars: 58548
---

# Video Subtitle Translator Agent

Video Subtitle Translator Agent handles the complete subtitle localization workflow from extraction through translation to re-embedding. It uses FFmpeg’s -map 0:s:0 flag to extract subtitle streams from MKV, MP4, and other containers, detecting the subtitle codec (SRT, ASS, WebVTT) and converting to a normalized SRT format for processing. Translation routes through either the DeepL API for European languages with superior fluency or Google Cloud Translation v3 for broader language coverage including CJK and Indic scripts. Source language is auto-detected using the langdetect Python library when not specified. The translator preserves SRT timing codes and handles multi-line subtitle blocks by joining them for translation context, then re-splitting to match the original line structure. For RTL languages like Arabic and Hebrew, the agent inserts proper Unicode bidirectional marks and validates rendering through a test frame extraction with FFmpeg’s subtitles filter. Re-embedding uses FFmpeg’s -c:s mov_text for MP4 containers or -c:s srt for MKV, with proper language metadata tags set via -metadata:s:s:0 language=ara. Batch processing handles entire video libraries by scanning directories, detecting existing subtitle tracks, and generating missing translations based on a target language configuration list.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
