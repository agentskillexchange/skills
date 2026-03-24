---
name: "GStreamer Live Stream Transcoder"
description: "Builds GStreamer pipelines for real-time video transcoding with NVENC/VA-API hardware acceleration. Supports adaptive bitrate HLS/DASH output via GStreamer’s hlssink2 and dashsink elements."
category: "Media & Transcription"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63278  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
