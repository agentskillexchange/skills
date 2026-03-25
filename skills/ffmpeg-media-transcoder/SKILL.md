---
name: "FFmpeg Media Transcoder"
description: "Automated video and audio transcoding using FFmpeg with hardware-accelerated encoding via NVENC/VAAPI, HLS adaptive streaming output, and MediaInfo-based quality validation."
category: "Image & Creative Automation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ffmpeg-media-transcoder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58283  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# FFmpeg Media Transcoder

Automated video and audio transcoding using FFmpeg with hardware-accelerated encoding via NVENC/VAAPI, HLS adaptive streaming output, and MediaInfo-based quality validation.

## Overview

The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox.

HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple’s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters.

Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg’s progress protocol, and webhook notifications on job completion or failure.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-media-transcoder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-media-transcoder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-media-transcoder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-media-transcoder -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-media-transcoder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ffmpeg-media-transcoder/
