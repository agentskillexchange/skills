---
name: "GStreamer Live Stream Transcoder"
description: "Builds GStreamer pipelines for real-time video transcoding with NVENC/VA-API hardware acceleration. Supports adaptive bitrate HLS/DASH output via GStreamer’s hlssink2 and dashsink elements."
category: "Media & Transcription"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/"
tool_ecosystem:
  tool: prometheus
  github_stars: 63289
  npm_weekly_downloads: 5319832
  github_repo: prometheus/prometheus
  license: Apache-2.0
  maintained: true
---

# GStreamer Live Stream Transcoder

Builds GStreamer pipelines for real-time video transcoding with NVENC/VA-API hardware acceleration. Supports adaptive bitrate HLS/DASH output via GStreamer’s hlssink2 and dashsink elements.

## Overview

This skill constructs and manages GStreamer pipelines for live video transcoding scenarios including streaming, surveillance, and broadcast workflows. It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate ladders for HLS output via hlssink2 with configurable segment duration, playlist depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation. Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources (ndisrc), and test patterns for validation. Audio processing handles AAC encoding via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and pipeline latency.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gstreamer-live-stream-transcoder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gstreamer-live-stream-transcoder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gstreamer-live-stream-transcoder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gstreamer-live-stream-transcoder -a codex
```

### OpenClaw

```bash
clawhub install gstreamer-live-stream-transcoder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/
