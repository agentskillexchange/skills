---
title: MediaInfo Metadata Extractor
description: The MediaInfo Metadata Extractor skill leverages the MediaInfo library
  through its pymediainfo Python bindings to provide detailed technical analysis of
  media files. It extracts codec information, bitrate statistics, resolution details,
  and container-level metadata from virtually any audio or video format. The skill
  parses MediaInfo output across all track types — General, Video, Audio, Text, and
  Menu — providing structured data about encoding parameters like codec profile and
  level, bit depth, chroma subsampling, and color space information. For HDR content,
  it extracts SMPTE ST 2086 mastering display metadata, MaxCLL/MaxFALL values, and
  Dolby Vision configuration records essential for proper HDR10/HDR10+/Dolby Vision
  identification. Batch analysis processes entire media libraries with results exported
  to JSON, CSV, or SQLite databases for asset management systems. The skill integrates
  with the MediaInfo CLI for environments where Python bindings are unavailable, parsing
  both XML and JSON output formats. Quality validation checks include bitrate compliance
  against delivery specifications (Netflix, Apple, YouTube upload requirements), audio
  channel layout verification, and subtitle track language tagging validation against
  BCP 47 standards. It supports reading metadata from streaming containers including
  MPEG-TS, HLS segments, and DASH manifests.
verification: security_reviewed
source: https://agentskillexchange.com/skills/mediainfo-metadata-extractor/
category:
- Media &amp; Transcription
framework:
- Custom Agents
---

# MediaInfo Metadata Extractor

The MediaInfo Metadata Extractor skill leverages the MediaInfo library through its pymediainfo Python bindings to provide detailed technical analysis of media files. It extracts codec information, bitrate statistics, resolution details, and container-level metadata from virtually any audio or video format. The skill parses MediaInfo output across all track types — General, Video, Audio, Text, and Menu — providing structured data about encoding parameters like codec profile and level, bit depth, chroma subsampling, and color space information. For HDR content, it extracts SMPTE ST 2086 mastering display metadata, MaxCLL/MaxFALL values, and Dolby Vision configuration records essential for proper HDR10/HDR10+/Dolby Vision identification. Batch analysis processes entire media libraries with results exported to JSON, CSV, or SQLite databases for asset management systems. The skill integrates with the MediaInfo CLI for environments where Python bindings are unavailable, parsing both XML and JSON output formats. Quality validation checks include bitrate compliance against delivery specifications (Netflix, Apple, YouTube upload requirements), audio channel layout verification, and subtitle track language tagging validation against BCP 47 standards. It supports reading metadata from streaming containers including MPEG-TS, HLS segments, and DASH manifests.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mediainfo-metadata-extractor/)
