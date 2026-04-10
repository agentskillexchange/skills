---
title: "MediaInfo Metadata Extractor"
description: "Extracts comprehensive media metadata using the MediaInfo library and pymediainfo Python bindings. Analyzes video/audio codec parameters, container formats, and HDR metadata for media asset management."
slug: "mediainfo-metadata-extractor"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/mediainfo-metadata-extractor/"
---

# MediaInfo Metadata Extractor

Extracts comprehensive media metadata using the MediaInfo library and pymediainfo Python bindings. Analyzes video/audio codec parameters, container formats, and HDR metadata for media asset management.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install mediainfo-metadata-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The MediaInfo Metadata Extractor skill leverages the MediaInfo library through its pymediainfo Python bindings to provide detailed technical analysis of media files. It extracts codec information, bitrate statistics, resolution details, and container-level metadata from virtually any audio or video format.
The skill parses MediaInfo output across all track types — General, Video, Audio, Text, and Menu — providing structured data about encoding parameters like codec profile and level, bit depth, chroma subsampling, and color space information. For HDR content, it extracts SMPTE ST 2086 mastering display metadata, MaxCLL/MaxFALL values, and Dolby Vision configuration records essential for proper HDR10/HDR10+/Dolby Vision identification.
Batch analysis processes entire media libraries with results exported to JSON, CSV, or SQLite databases for asset management systems. The skill integrates with the MediaInfo CLI for environments where Python bindings are unavailable, parsing both XML and JSON output formats. Quality validation checks include bitrate compliance against delivery specifications (Netflix, Apple, YouTube upload requirements), audio channel layout verification, and subtitle track language tagging validation against BCP 47 standards. It supports reading metadata from streaming containers including MPEG-TS, HLS segments, and DASH manifests.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mediainfo-metadata-extractor/)
