---
title: "Video Subtitle Translator Agent"
description: "Video Subtitle Translator Agent handles the complete subtitle localization workflow from extraction through translation to re-embedding. It uses FFmpeg&#8217;s -map 0:s:0 flag to extract subtitle streams from MKV, MP4, and other containers, detecting the subtitle codec (SRT, ASS, WebVTT) and converting to a normalized SRT format for processing. Translation routes through either the DeepL API for European languages with superior fluency or Google Cloud Translation v3 for broader language coverage including CJK and Indic scripts. Source language is auto-detected using the langdetect Python library when not specified. The translator preserves SRT timing codes and handles multi-line subtitle blocks by joining them for translation context, then re-splitting to match the original line structure. For RTL languages like Arabic and Hebrew, the agent inserts proper Unicode bidirectional marks and validates rendering through a test frame extraction with FFmpeg&#8217;s subtitles filter. Re-embedding uses FFmpeg&#8217;s -c:s mov_text for MP4 containers or -c:s srt for MKV, with proper language metadata tags set via -metadata:s:s:0 language=ara. Batch processing handles entire video libraries by scanning directories, detecting existing subtitle tracks, and generating missing translations based on a target language configuration list."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Video Subtitle Translator Agent

Video Subtitle Translator Agent handles the complete subtitle localization workflow from extraction through translation to re-embedding. It uses FFmpeg&#8217;s -map 0:s:0 flag to extract subtitle streams from MKV, MP4, and other containers, detecting the subtitle codec (SRT, ASS, WebVTT) and converting to a normalized SRT format for processing. Translation routes through either the DeepL API for European languages with superior fluency or Google Cloud Translation v3 for broader language coverage including CJK and Indic scripts. Source language is auto-detected using the langdetect Python library when not specified. The translator preserves SRT timing codes and handles multi-line subtitle blocks by joining them for translation context, then re-splitting to match the original line structure. For RTL languages like Arabic and Hebrew, the agent inserts proper Unicode bidirectional marks and validates rendering through a test frame extraction with FFmpeg&#8217;s subtitles filter. Re-embedding uses FFmpeg&#8217;s -c:s mov_text for MP4 containers or -c:s srt for MKV, with proper language metadata tags set via -metadata:s:s:0 language=ara. Batch processing handles entire video libraries by scanning directories, detecting existing subtitle tracks, and generating missing translations based on a target language configuration list.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
