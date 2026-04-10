---
name: FFmpeg Audio Transcoder
description: Transcodes and processes audio files using the FFmpeg CLI and libavcodec
  library. Supports batch format conversion, loudness normalization via EBU R128,
  and metadata extraction with ffprobe.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/
category:
- Media &amp; Transcription
framework:
- Cursor
---
# FFmpeg Audio Transcoder

FFmpeg Audio Transcoder is built around FFmpeg media processing toolkit. The underlying ecosystem is represented by FFmpeg/FFmpeg (58,257+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to ffmpeg so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe. The implementation typically relies on ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as audio/video pipelines, thumbnails, HLS, normalization, and format conversion.

 Key integration points include audio/video pipelines, thumbnails, HLS, normalization, and format conversion. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/)
