---
name: "Live Stream Clip Extractor"
description: "Extracts highlight clips from live streams using Twitch Helix API, YouTube Live Streaming API, and FFmpeg segment detection. Identifies peak moments via chat velocity analysis and audio energy spikes."
category: "Media &amp; Transcription"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/"
---
# Live Stream Clip Extractor

Extracts highlight clips from live streams using Twitch Helix API, YouTube Live Streaming API, and FFmpeg segment detection. Identifies peak moments via chat velocity analysis and audio energy spikes.

## Overview

The Live Stream Clip Extractor automatically identifies and extracts highlight moments from live streaming content. It monitors live streams via the Twitch Helix API clips endpoint and YouTube Live Streaming API liveBroadcasts resource. The agent detects peak moments using multiple signals: chat message velocity analysis via Twitch IRC (TMI.js), audio energy spike detection using FFmpeg loudnorm filter and ebur128 measurement, and scene change detection via FFmpeg scene filter with configurable thresholds. Clip extraction uses FFmpeg segment muxer for frame-accurate cutting without re-encoding, and the agent generates multiple output formats (MP4, WebM, GIF) with automatic thumbnail generation at the highest-energy frame. It integrates with Streamlink for reliable stream capture across platforms and uses yt-dlp for VOD segment downloading. The extractor supports automated posting to social media via the Twitter API v2 media upload endpoint and Instagram Graph API for Reels. Clip metadata includes timestamp, duration, chat context, and engagement metrics. Batch processing handles full VOD analysis with configurable highlight density and minimum clip duration settings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill live-stream-clip-extractor-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill live-stream-clip-extractor-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill live-stream-clip-extractor-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill live-stream-clip-extractor-agent -a codex
```

### OpenClaw

```bash
clawhub install live-stream-clip-extractor-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/)
