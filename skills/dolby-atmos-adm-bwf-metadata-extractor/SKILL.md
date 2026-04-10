---
title: "Dolby Atmos ADM-BWF Metadata Extractor"
description: "Extracts and validates Audio Definition Model (ADM) metadata from Broadcast Wave Format (BWF) files using the libadm C++ library and EBU Tech 3364 spec for Dolby Atmos immersive audio object positions."
slug: "dolby-atmos-adm-bwf-metadata-extractor"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/"
---

# Dolby Atmos ADM-BWF Metadata Extractor

Extracts and validates Audio Definition Model (ADM) metadata from Broadcast Wave Format (BWF) files using the libadm C++ library and EBU Tech 3364 spec for Dolby Atmos immersive audio object positions.

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
clawhub install dolby-atmos-adm-bwf-metadata-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Dolby Atmos ADM-BWF Metadata Extractor parses immersive audio files in Broadcast Wave Format containing Audio Definition Model (ADM) metadata per ITU-R BS.2076 and EBU Tech 3364 specifications. It reads the axml chunk from BWF files using libadm to extract audioProgramme, audioContent, audioObject, audioPackFormat, audioChannelFormat, and audioBlockFormat elements. The agent maps audioBlockFormat position data (azimuth, elevation, distance in spherical coordinates and X/Y/Z in Cartesian) to render-ready object positions for Dolby Atmos, Sony 360 Reality Audio, and MPEG-H 3D Audio renderers. It validates channel bed assignments against standard speaker layouts (2.0, 5.1, 7.1.4) and checks audioObject importance metadata for bandwidth-constrained delivery. Output includes a JSON scene description compatible with the Dolby Atmos Production Suite and a visual 3D plot of object trajectories using matplotlib. Supports S-ADM (serial ADM) for live broadcast workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/)
