---
title: Live Stream Clip Extractor
description: 'The Live Stream Clip Extractor automatically identifies and extracts
  highlight moments from live streaming content. It monitors live streams via the
  Twitch Helix API clips endpoint and YouTube Live Streaming API liveBroadcasts resource.
  The agent detects peak moments using multiple signals: chat message velocity analysis
  via Twitch IRC (TMI.js), audio energy spike detection using FFmpeg loudnorm filter
  and ebur128 measurement, and scene change detection via FFmpeg scene filter with
  configurable thresholds. Clip extraction uses FFmpeg segment muxer for frame-accurate
  cutting without re-encoding, and the agent generates multiple output formats (MP4,
  WebM, GIF) with automatic thumbnail generation at the highest-energy frame. It integrates
  with Streamlink for reliable stream capture across platforms and uses yt-dlp for
  VOD segment downloading. The extractor supports automated posting to social media
  via the Twitter API v2 media upload endpoint and Instagram Graph API for Reels.
  Clip metadata includes timestamp, duration, chat context, and engagement metrics.
  Batch processing handles full VOD analysis with configurable highlight density and
  minimum clip duration settings.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/
category:
- Media &amp; Transcription
framework:
- ChatGPT Agents
---

# Live Stream Clip Extractor

The Live Stream Clip Extractor automatically identifies and extracts highlight moments from live streaming content. It monitors live streams via the Twitch Helix API clips endpoint and YouTube Live Streaming API liveBroadcasts resource. The agent detects peak moments using multiple signals: chat message velocity analysis via Twitch IRC (TMI.js), audio energy spike detection using FFmpeg loudnorm filter and ebur128 measurement, and scene change detection via FFmpeg scene filter with configurable thresholds. Clip extraction uses FFmpeg segment muxer for frame-accurate cutting without re-encoding, and the agent generates multiple output formats (MP4, WebM, GIF) with automatic thumbnail generation at the highest-energy frame. It integrates with Streamlink for reliable stream capture across platforms and uses yt-dlp for VOD segment downloading. The extractor supports automated posting to social media via the Twitter API v2 media upload endpoint and Instagram Graph API for Reels. Clip metadata includes timestamp, duration, chat context, and engagement metrics. Batch processing handles full VOD analysis with configurable highlight density and minimum clip duration settings.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-clip-extractor-agent/)
