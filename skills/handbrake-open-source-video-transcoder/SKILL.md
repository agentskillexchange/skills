---
name: "HandBrake Open-Source Video Transcoder"
description: "HandBrake is a widely-used open-source video transcoder that converts video files between formats for playback on phones, tablets, TVs, game consoles, and web browsers. It supports most common input formats and leverages FFmpeg, x264, x265, and SVT-AV1 for encoding."
verification: security_reviewed
source: "https://github.com/HandBrake/HandBrake"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "handbrake/handbrake"
  github_stars: 22806
---

# HandBrake Open-Source Video Transcoder

Overview
HandBrake is one of the most established open-source video transcoding tools available, supporting Linux, macOS, and Windows. It converts videos you already have into new files that work on virtually any modern device — mobile phones, tablets, TV media players, game consoles, computers, and web browsers.
How It Works
HandBrake accepts input from most common video files and formats, including those from consumer and professional video cameras, mobile devices, screen recordings, DVDs, and Blu-ray discs. It uses industry-standard libraries including FFmpeg for demuxing and decoding, x264 and x265 for H.264/H.265 encoding, and SVT-AV1 for AV1 encoding. Output formats include MP4 (M4V), MKV, and WebM containers.
Key Capabilities
HandBrake provides both a GUI and a full-featured CLI (HandBrakeCLI) suitable for scripting and automation. It includes built-in device presets for common targets (Apple, Android, Chromecast, PlayStation, Xbox, web), chapter markers support, subtitle import and passthrough (VobSub, SRT, SSA, CEA-608), audio track selection with passthrough or re-encoding, video filters (deinterlacing, decomb, detelecine, deblock, grayscale, cropping, scaling), and batch scanning of multiple files.
Integration Points
The HandBrakeCLI executable enables integration into automated workflows and agent pipelines. Agents can invoke it with specific presets (--preset), output formats, quality targets (--quality for constant quality or --vb for average bitrate), and filter chains. It can scan media files to report track information before encoding, making it suitable for intelligent media processing workflows.
Technical Details
HandBrake has been actively developed since 2003 and has 23,000+ GitHub stars. It is licensed under GNU General Public License v2. The project maintains regular releases with pre-built binaries for all major platforms. Hardware acceleration is supported via Intel QSV, AMD VCE, Nvidia NVENC, Apple VideoToolbox, and MediaFoundation, enabling high-performance batch transcoding on modern hardware.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/handbrake-open-source-video-transcoder/)
