---
name: "Audio Fingerprint Identifier"
description: "Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases."
category: "Media & Transcription"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# Audio Fingerprint Identifier

Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases.

## Overview

The Audio Fingerprint Identifier provides robust audio content recognition using multiple fingerprinting technologies. It generates acoustic fingerprints using the Chromaprint library (fpcalc CLI) and queries the AcoustID API for music identification with MusicBrainz metadata enrichment. For real-time audio recognition, it integrates with the Shazam API (RapidAPI endpoint) providing song title, artist, album, and ISRC codes. The agent also connects to ACRCloud for broadcast monitoring and custom fingerprint database matching. Audio preprocessing uses FFmpeg for sample rate normalization, channel mixing, and segment extraction. The identifier supports continuous monitoring mode for radio/TV streams, detecting music tracks, advertisements, and spoken word segments using energy-based voice activity detection (VAD) via WebRTC VAD. It builds local fingerprint databases using the Dejavu audio fingerprinting library for custom content catalogs. Metadata enrichment pulls from the Spotify Web API, Discogs API, and MusicBrainz API to provide comprehensive track information. Results are stored in PostgreSQL with PostGIS extensions for temporal indexing and exported via CSV or JSON-LD with Schema.org MusicRecording markup.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill audio-fingerprint-identifier-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill audio-fingerprint-identifier-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill audio-fingerprint-identifier-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill audio-fingerprint-identifier-agent -a codex
```

### OpenClaw

```bash
clawhub install audio-fingerprint-identifier-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/
