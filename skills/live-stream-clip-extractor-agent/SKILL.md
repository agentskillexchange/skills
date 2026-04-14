---
title: "Live Stream Clip Extractor"
description: "Extracts highlight clips from live streams using Twitch Helix API, YouTube Live Streaming API, and FFmpeg segment detection. Identifies peak moments via chat velocity analysis and audio energy spikes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/"
category:
  - "Media &amp; Transcription"
framework:
  - "ChatGPT Agents"
---

# Live Stream Clip Extractor

The Live Stream Clip Extractor automatically identifies and extracts highlight moments from live streaming content. It monitors live streams via the Twitch Helix API clips endpoint and YouTube Live Streaming API liveBroadcasts resource. The agent detects peak moments using multiple signals: chat message velocity analysis via Twitch IRC (TMI.js), audio energy spike detection using FFmpeg loudnorm filter and ebur128 measurement, and scene change detection via FFmpeg scene filter with configurable thresholds. Clip extraction uses FFmpeg segment muxer for frame-accurate cutting without re-encoding, and the agent generates multiple output formats (MP4, WebM, GIF) with automatic thumbnail generation at the highest-energy frame. It integrates with Streamlink for reliable stream capture across platforms and uses yt-dlp for VOD segment downloading. The extractor supports automated posting to social media via the Twitter API v2 media upload endpoint and Instagram Graph API for Reels. Clip metadata includes timestamp, duration, chat context, and engagement metrics. Batch processing handles full VOD analysis with configurable highlight density and minimum clip duration settings.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/)
