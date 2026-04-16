---
title: "Audio Fingerprint Identifier"
description: "Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# Audio Fingerprint Identifier

The Audio Fingerprint Identifier provides robust audio content recognition using multiple fingerprinting technologies. It generates acoustic fingerprints using the Chromaprint library (fpcalc CLI) and queries the AcoustID API for music identification with MusicBrainz metadata enrichment. For real-time audio recognition, it integrates with the Shazam API (RapidAPI endpoint) providing song title, artist, album, and ISRC codes. The agent also connects to ACRCloud for broadcast monitoring and custom fingerprint database matching. Audio preprocessing uses FFmpeg for sample rate normalization, channel mixing, and segment extraction. The identifier supports continuous monitoring mode for radio/TV streams, detecting music tracks, advertisements, and spoken word segments using energy-based voice activity detection (VAD) via WebRTC VAD. It builds local fingerprint databases using the Dejavu audio fingerprinting library for custom content catalogs. Metadata enrichment pulls from the Spotify Web API, Discogs API, and MusicBrainz API to provide comprehensive track information. Results are stored in PostgreSQL with PostGIS extensions for temporal indexing and exported via CSV or JSON-LD with Schema.org MusicRecording markup.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/)
