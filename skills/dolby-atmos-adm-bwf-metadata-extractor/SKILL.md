---
title: "Dolby Atmos ADM-BWF Metadata Extractor"
description: "Extracts and validates Audio Definition Model (ADM) metadata from Broadcast Wave Format (BWF) files using the libadm C++ library and EBU Tech 3364 spec for Dolby Atmos immersive audio object positions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
---

# Dolby Atmos ADM-BWF Metadata Extractor

The Dolby Atmos ADM-BWF Metadata Extractor parses immersive audio files in Broadcast Wave Format containing Audio Definition Model (ADM) metadata per ITU-R BS.2076 and EBU Tech 3364 specifications. It reads the axml chunk from BWF files using libadm to extract audioProgramme, audioContent, audioObject, audioPackFormat, audioChannelFormat, and audioBlockFormat elements. The agent maps audioBlockFormat position data (azimuth, elevation, distance in spherical coordinates and X/Y/Z in Cartesian) to render-ready object positions for Dolby Atmos, Sony 360 Reality Audio, and MPEG-H 3D Audio renderers. It validates channel bed assignments against standard speaker layouts (2.0, 5.1, 7.1.4) and checks audioObject importance metadata for bandwidth-constrained delivery. Output includes a JSON scene description compatible with the Dolby Atmos Production Suite and a visual 3D plot of object trajectories using matplotlib. Supports S-ADM (serial ADM) for live broadcast workflows.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-atmos-adm-bwf-metadata-extractor/)
