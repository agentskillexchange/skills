---
name: "Liquidsoap Audio and Video Streaming Language"
description: "Build audio and video streaming pipelines with Liquidsoap, a statically typed scripting language purpose-built for media automation. Create internet radio stations, live stream processors, and automated playout systems with a composable operator model."
category: "Media &amp; Transcription"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/savonet/liquidsoap"
tool_ecosystem:
  github_repo: "savonet/liquidsoap"
  github_stars: 1638
  license: "GPL-2.0"
---
# Liquidsoap Audio and Video Streaming Language

Build audio and video streaming pipelines with Liquidsoap, a statically typed scripting language purpose-built for media automation. Create internet radio stations, live stream processors, and automated playout systems with a composable operator model.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill liquidsoap-audio-video-streaming-language
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill liquidsoap-audio-video-streaming-language -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill liquidsoap-audio-video-streaming-language -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill liquidsoap-audio-video-streaming-language -a codex
```

### OpenClaw

```bash
clawhub install liquidsoap-audio-video-streaming-language
```

## Details

Liquidsoap is a statically typed, domain-specific programming language designed for audio and video stream manipulation. Developed by the Savonet project, it provides a declarative way to define media processing pipelines that handle live input, file playout, stream encoding, and output to Icecast, Shoutcast, HLS, and other streaming targets.

At its core, Liquidsoap models audio and video as composable stream operators. A basic internet radio station can be defined in just a few lines: read a playlist, apply crossfading between tracks, add jingles at intervals, and output to an Icecast server. More complex setups chain operators for silence detection, volume normalization, live DJ input switching, scheduled programming, and multi-format encoding (MP3, Opus, FLAC, AAC, HLS/DASH for video).

The language supports both audio and video streams natively. Video capabilities include overlaying text, images, and graphics onto live streams, compositing multiple video sources, and applying real-time filters. The HLS output operator generates adaptive bitrate streams with multiple quality levels, suitable for production web streaming.

Liquidsoap provides built-in support for external integrations: HTTP requests for dynamic metadata, JSON parsing for API-driven playlist updates, Telnet and Unix socket control interfaces for runtime manipulation, and harbor HTTP input for receiving live audio from external encoders like BUTT or source clients. The input.ffmpeg operator leverages FFmpeg for broad codec support.

For AI agent workflows, Liquidsoap serves as the execution engine for automated media streaming operations. An agent can generate Liquidsoap scripts to set up radio stations, configure playout schedules, manage failover chains (live source → scheduled content → emergency playlist), and control running instances via the Telnet interface. The scripting language is expressive enough to encode complex scheduling logic, conditional stream routing, and dynamic content insertion.

Installation is available through package managers (apt, opam, Homebrew) and Docker images. Configuration is done through .liq script files that define the complete streaming pipeline, making setups reproducible and version-controllable.

Source: github.com/savonet/liquidsoap | Website: liquidsoap.info — GPL-2.0 licensed, 1,600+ GitHub stars, actively maintained with frequent releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/liquidsoap-audio-video-streaming-language/)
