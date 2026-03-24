---
name: "SoX Audio Processing Toolkit"
description: "Applies audio effects chains using SoX (Sound eXchange) CLI including noise reduction, normalization, tempo adjustment, and format conversion. Supports batch processing with GNU Parallel."
category: "Media & Transcription"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sox-audio-processing-toolkit/"
---

# SoX Audio Processing Toolkit

Applies audio effects chains using SoX (Sound eXchange) CLI including noise reduction, normalization, tempo adjustment, and format conversion. Supports batch processing with GNU Parallel.

## Overview

This skill wraps the SoX command-line audio processor for automated audio manipulation tasks including podcast post-production, audiobook preparation, and dataset preprocessing for ML training. It constructs SoX effect chains programmatically, combining operations like noise profiling and reduction (noisered), loudness normalization to target LUFS via the gain and loudness effects, tempo/pitch adjustment without artifacts using the tempo and pitch effects, and silence trimming from beginning and end of tracks. Format conversion handles WAV, FLAC, MP3 (via libmad/lame), OGG Vorbis, and Opus with configurable bitrate and sample rate. The skill supports multi-file batch processing using GNU Parallel for CPU-efficient throughput on large audio libraries. Advanced features include spectogram generation via SoX’s spectrogram effect for visual audio analysis, channel mixing (stereo to mono, 5.1 downmix), sample rate conversion with dither, and audio concatenation with crossfade. Integration with ffprobe provides detailed input analysis before processing. Error handling validates codec availability and reports unsupported format combinations clearly.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sox-audio-processing-toolkit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sox-audio-processing-toolkit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sox-audio-processing-toolkit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sox-audio-processing-toolkit -a codex
```

### OpenClaw

```bash
clawhub install sox-audio-processing-toolkit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sox-audio-processing-toolkit/
