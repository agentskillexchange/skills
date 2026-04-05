---
name: "Video Subtitle Auto-Translator"
description: "Translates video subtitles across 100+ languages using DeepL API and Google Cloud Translation v3. Handles SRT/VTT timing preservation, character limit enforcement, and subtitle segmentation with Aegisub CLI."
category: "Media &amp; Transcription"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/"
---
# Video Subtitle Auto-Translator

Translates video subtitles across 100+ languages using DeepL API and Google Cloud Translation v3. Handles SRT/VTT timing preservation, character limit enforcement, and subtitle segmentation with Aegisub CLI.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-auto-translator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-auto-translator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-auto-translator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill video-subtitle-auto-translator-agent -a codex
```

### OpenClaw

```bash
clawhub install video-subtitle-auto-translator-agent
```

## Details

The Video Subtitle Auto-Translator automates multilingual subtitle creation for video content. It ingests SRT, VTT, ASS, and SSA subtitle formats and translates them using the DeepL API for European languages (with formality control) and Google Cloud Translation v3 API for broader language coverage including CJK languages. The agent preserves precise timing codes during translation, automatically adjusting reading speed calculations based on target language character density. It enforces platform-specific character limits (Netflix 42 chars/line, YouTube 32 chars) using intelligent line-breaking algorithms. Subtitle segmentation and merge operations are performed using the Aegisub CLI (aegisub-cli) for complex formatting. The translator handles subtitle synchronization with FFmpeg subtitle filter for hardcoding and the MKVToolNix mkvmerge command for soft subtitle embedding. It integrates with Crowdin API for collaborative translation review workflows and supports translation memory via TMX file import/export. Quality assurance includes back-translation verification, reading speed validation (15-25 chars/second), and automated QC reports using Subtitle Edit CLI. Batch processing supports YouTube channels via the YouTube Data API v3 for automatic caption uploads.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-auto-translator-agent/)
