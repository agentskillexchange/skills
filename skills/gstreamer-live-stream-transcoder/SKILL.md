---
title: GStreamer Live Stream Transcoder
description: 'This skill constructs and manages GStreamer pipelines for live video
  transcoding scenarios including streaming, surveillance, and broadcast workflows.
  It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer
  Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration
  is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc
  via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate
  ladders for HLS output via hlssink2 with configurable segment duration, playlist
  depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation.
  Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources
  (ndisrc), and test patterns for validation. Audio processing handles AAC encoding
  via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring
  uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration
  with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and
  pipeline latency.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/
category:
- Media &amp; Transcription
framework:
- Gemini
---

# GStreamer Live Stream Transcoder

This skill constructs and manages GStreamer pipelines for live video transcoding scenarios including streaming, surveillance, and broadcast workflows. It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate ladders for HLS output via hlssink2 with configurable segment duration, playlist depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation. Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources (ndisrc), and test patterns for validation. Audio processing handles AAC encoding via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and pipeline latency.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/)
