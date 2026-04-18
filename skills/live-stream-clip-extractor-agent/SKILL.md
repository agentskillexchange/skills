---
title: "Live Stream Clip Extractor"
description: "Extracts highlight clips from live streams using Twitch Helix API, YouTube Live Streaming API, and FFmpeg segment detection. Identifies peak moments via chat velocity analysis and audio energy spikes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/"
category:
  - "Media & Transcription"
framework:
  - "ChatGPT Agents"
---

# Live Stream Clip Extractor

The Live Stream Clip Extractor automatically identifies and extracts highlight moments from live streaming content. It monitors live streams via the Twitch Helix API clips endpoint and YouTube Live Streaming API liveBroadcasts resource. The agent detects peak moments using multiple signals: chat message velocity analysis via Twitch IRC (TMI.js), audio energy spike detection using FFmpeg loudnorm filter and ebur128 measurement, and scene change detection via FFmpeg scene filter with configurable thresholds. Clip extraction uses FFmpeg segment muxer for frame-accurate cutting without re-encoding, and the agent generates multiple output formats (MP4, WebM, GIF) with automatic thumbnail generation at the highest-energy frame. It integrates with Streamlink for reliable stream capture across platforms and uses yt-dlp for VOD segment downloading. The extractor supports automated posting to social media via the Twitter API v2 media upload endpoint and Instagram Graph API for Reels. Clip metadata includes timestamp, duration, chat context, and engagement metrics. Batch processing handles full VOD analysis with configurable highlight density and minimum clip duration settings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/live-stream-clip-extractor-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/live-stream-clip-extractor-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/)
