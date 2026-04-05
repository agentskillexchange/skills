---
name: "Video Subtitle Translator Agent"
description: "Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages."
category: "Media & Transcription"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---
# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

Video Subtitle Translator Agent handles the complete subtitle localization workflow from extraction through translation to re-embedding. It uses FFmpeg’s -map 0:s:0 flag to extract subtitle streams from MKV, MP4, and other containers, detecting the subtitle codec (SRT, ASS, WebVTT) and converting to a normalized SRT format for processing.



Translation routes through either the DeepL API for European languages with superior fluency or Google Cloud Translation v3 for broader language coverage including CJK and Indic scripts. Source language is auto-detected using the langdetect Python library when not specified. The translator preserves SRT timing codes and handles multi-line subtitle blocks by joining them for translation context, then re-splitting to match the original line structure.



For RTL languages like Arabic and Hebrew, the agent inserts proper Unicode bidirectional marks and validates rendering through a test frame extraction with FFmpeg’s subtitles filter. Re-embedding uses FFmpeg’s -c:s mov_text for MP4 containers or -c:s srt for MKV, with proper language metadata tags set via -metadata:s:s:0 language=ara. Batch processing handles entire video libraries by scanning directories, detecting existing subtitle tracks, and generating missing translations based on a target language configuration list.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-translator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-translator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-translator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-translator-agent -a codex
```

### OpenClaw

```bash
clawhub install video-subtitle-translator-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
