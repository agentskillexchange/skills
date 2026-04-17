---
title: "GStreamer Live Stream Transcoder"
description: "This skill constructs and manages GStreamer pipelines for live video transcoding scenarios including streaming, surveillance, and broadcast workflows. It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate ladders for HLS output via hlssink2 with configurable segment duration, playlist depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation. Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources (ndisrc), and test patterns for validation. Audio processing handles AAC encoding via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and pipeline latency."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/"
framework:
  - "Gemini"
---

# GStreamer Live Stream Transcoder

This skill constructs and manages GStreamer pipelines for live video transcoding scenarios including streaming, surveillance, and broadcast workflows. It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate ladders for HLS output via hlssink2 with configurable segment duration, playlist depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation. Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources (ndisrc), and test patterns for validation. Audio processing handles AAC encoding via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and pipeline latency.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gstreamer-live-stream-transcoder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gstreamer-live-stream-transcoder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/)
