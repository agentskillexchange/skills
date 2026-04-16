---
title: "GStreamer Live Stream Transcoder"
description: "Builds GStreamer pipelines for real-time video transcoding with NVENC/VA-API hardware acceleration. Supports adaptive bitrate HLS/DASH output via GStreamer’s hlssink2 and dashsink elements."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/"
category:
  - "Media & Transcription"
framework:
  - "Gemini"
---

# GStreamer Live Stream Transcoder

This skill constructs and manages GStreamer pipelines for live video transcoding scenarios including streaming, surveillance, and broadcast workflows. It dynamically assembles pipeline graphs using gst-launch syntax or the GStreamer Python bindings (gi.repository.Gst) based on available hardware. Hardware acceleration is auto-detected: NVIDIA GPUs use nvh264enc/nvh265enc via NVENC, Intel/AMD use vaapih264enc via VA-API, and software fallback uses x264enc. The skill generates adaptive bitrate ladders for HLS output via hlssink2 with configurable segment duration, playlist depth, and encryption (AES-128). DASH output uses dashsink with MPD manifest generation. Input sources include RTSP streams (rtspsrc), V4L2 cameras (v4l2src), NDI sources (ndisrc), and test patterns for validation. Audio processing handles AAC encoding via fdkaacenc with loudness normalization per EBU R128. Pipeline health monitoring uses GStreamer bus messages and watchdog timers to auto-restart on errors. Integration with Prometheus via a custom metrics exporter tracks frame rates, bitrates, and pipeline latency.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gstreamer-live-stream-transcoder/)
