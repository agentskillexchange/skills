---
name: "MediaInfo Metadata Extractor"
description: "Extracts comprehensive media metadata using the MediaInfo library and pymediainfo Python bindings. Analyzes video/audio codec parameters, container formats, and HDR metadata for media asset management."
category: "Media & Transcription"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mediainfo-metadata-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  github_stars: 7043  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
  github_repo: "WiseLibs/better-sqlite3"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# MediaInfo Metadata Extractor

Extracts comprehensive media metadata using the MediaInfo library and pymediainfo Python bindings. Analyzes video/audio codec parameters, container formats, and HDR metadata for media asset management.

## Overview

The MediaInfo Metadata Extractor skill leverages the MediaInfo library through its pymediainfo Python bindings to provide detailed technical analysis of media files. It extracts codec information, bitrate statistics, resolution details, and container-level metadata from virtually any audio or video format.

The skill parses MediaInfo output across all track types — General, Video, Audio, Text, and Menu — providing structured data about encoding parameters like codec profile and level, bit depth, chroma subsampling, and color space information. For HDR content, it extracts SMPTE ST 2086 mastering display metadata, MaxCLL/MaxFALL values, and Dolby Vision configuration records essential for proper HDR10/HDR10+/Dolby Vision identification.

Batch analysis processes entire media libraries with results exported to JSON, CSV, or SQLite databases for asset management systems. The skill integrates with the MediaInfo CLI for environments where Python bindings are unavailable, parsing both XML and JSON output formats. Quality validation checks include bitrate compliance against delivery specifications (Netflix, Apple, YouTube upload requirements), audio channel layout verification, and subtitle track language tagging validation against BCP 47 standards. It supports reading metadata from streaming containers including MPEG-TS, HLS segments, and DASH manifests.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mediainfo-metadata-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mediainfo-metadata-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mediainfo-metadata-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mediainfo-metadata-extractor -a codex
```

### OpenClaw

```bash
clawhub install mediainfo-metadata-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mediainfo-metadata-extractor/
