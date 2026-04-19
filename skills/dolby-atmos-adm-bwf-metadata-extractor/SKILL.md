---
title: "Dolby Atmos ADM-BWF Metadata Extractor"
description: "The Dolby Atmos ADM-BWF Metadata Extractor parses immersive audio files in Broadcast Wave Format containing Audio Definition Model (ADM) metadata per ITU-R BS.2076 and EBU Tech 3364 specifications. It reads the axml chunk from BWF files using libadm to extract audioProgramme, audioContent, audioObject, audioPackFormat, audioChannelFormat, and audioBlockFormat elements. The agent maps audioBlockFormat position data (azimuth, elevation, distance in spherical coordinates and X/Y/Z in Cartesian) to render-ready object positions for Dolby Atmos, Sony 360 Reality Audio, and MPEG-H 3D Audio renderers. It validates channel bed assignments against standard speaker layouts (2.0, 5.1, 7.1.4) and checks audioObject importance metadata for bandwidth-constrained delivery. Output includes a JSON scene description compatible with the Dolby Atmos Production Suite and a visual 3D plot of object trajectories using matplotlib. Supports S-ADM (serial ADM) for live broadcast workflows."
source: "https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
---

# Dolby Atmos ADM-BWF Metadata Extractor

The Dolby Atmos ADM-BWF Metadata Extractor parses immersive audio files in Broadcast Wave Format containing Audio Definition Model (ADM) metadata per ITU-R BS.2076 and EBU Tech 3364 specifications. It reads the axml chunk from BWF files using libadm to extract audioProgramme, audioContent, audioObject, audioPackFormat, audioChannelFormat, and audioBlockFormat elements. The agent maps audioBlockFormat position data (azimuth, elevation, distance in spherical coordinates and X/Y/Z in Cartesian) to render-ready object positions for Dolby Atmos, Sony 360 Reality Audio, and MPEG-H 3D Audio renderers. It validates channel bed assignments against standard speaker layouts (2.0, 5.1, 7.1.4) and checks audioObject importance metadata for bandwidth-constrained delivery. Output includes a JSON scene description compatible with the Dolby Atmos Production Suite and a visual 3D plot of object trajectories using matplotlib. Supports S-ADM (serial ADM) for live broadcast workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/)
