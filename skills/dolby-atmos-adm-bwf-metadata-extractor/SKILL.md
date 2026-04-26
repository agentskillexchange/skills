---
title: "Dolby Atmos ADM-BWF Metadata Extractor"
description: "Extracts and validates Audio Definition Model (ADM) metadata from Broadcast Wave Format (BWF) files using the libadm C++ library and EBU Tech 3364 spec for Dolby Atmos immersive audio object positions."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/"
category:
  - "Media & Transcription"
framework:
  - "Gemini"
---

# Dolby Atmos ADM-BWF Metadata Extractor

The Dolby Atmos ADM-BWF Metadata Extractor parses immersive audio files in Broadcast Wave Format containing Audio Definition Model (ADM) metadata per ITU-R BS.2076 and EBU Tech 3364 specifications. It reads the axml chunk from BWF files using libadm to extract audioProgramme, audioContent, audioObject, audioPackFormat, audioChannelFormat, and audioBlockFormat elements. The agent maps audioBlockFormat position data (azimuth, elevation, distance in spherical coordinates and X/Y/Z in Cartesian) to render-ready object positions for Dolby Atmos, Sony 360 Reality Audio, and MPEG-H 3D Audio renderers. It validates channel bed assignments against standard speaker layouts (2.0, 5.1, 7.1.4) and checks audioObject importance metadata for bandwidth-constrained delivery. Output includes a JSON scene description compatible with the Dolby Atmos Production Suite and a visual 3D plot of object trajectories using matplotlib. Supports S-ADM (serial ADM) for live broadcast workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dolby-atmos-adm-bwf-metadata-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dolby-atmos-adm-bwf-metadata-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/)
