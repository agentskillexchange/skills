---
title: "MediaInfo Metadata Extractor"
description: "Extracts comprehensive media metadata using the MediaInfo library and pymediainfo Python bindings. Analyzes video/audio codec parameters, container formats, and HDR metadata for media asset management."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mediainfo-metadata-extractor/"
category:
  - "Media & Transcription"
framework:
  - "Custom Agents"
---

# MediaInfo Metadata Extractor

The MediaInfo Metadata Extractor skill leverages the MediaInfo library through its pymediainfo Python bindings to provide detailed technical analysis of media files. It extracts codec information, bitrate statistics, resolution details, and container-level metadata from virtually any audio or video format.

The skill parses MediaInfo output across all track types — General, Video, Audio, Text, and Menu — providing structured data about encoding parameters like codec profile and level, bit depth, chroma subsampling, and color space information. For HDR content, it extracts SMPTE ST 2086 mastering display metadata, MaxCLL/MaxFALL values, and Dolby Vision configuration records essential for proper HDR10/HDR10+/Dolby Vision identification.

Batch analysis processes entire media libraries with results exported to JSON, CSV, or SQLite databases for asset management systems. The skill integrates with the MediaInfo CLI for environments where Python bindings are unavailable, parsing both XML and JSON output formats. Quality validation checks include bitrate compliance against delivery specifications (Netflix, Apple, YouTube upload requirements), audio channel layout verification, and subtitle track language tagging validation against BCP 47 standards. It supports reading metadata from streaming containers including MPEG-TS, HLS segments, and DASH manifests.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mediainfo-metadata-extractor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/mediainfo-metadata-extractor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mediainfo-metadata-extractor/)
