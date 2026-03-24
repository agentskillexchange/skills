---
name: "ElevenLabs Voiceover Generator for Long-Form Content"
description: "Splits blog posts or scripts into optimal chunks under ElevenLabs character limits, synthesizes each chunk using the v2 Multilingual model, and stitches MP3 segments together with pydub. Supports custom voice cloning via stored Voice IDs with per-segment stability and similarity tuning. Final audio is uploaded to Cloudflare R2 and a signed URL is returned."
category: "Media & Transcription"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elevenlabs-voiceover-longform/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cloudflare"  # from ase_tool_match
  github_stars: 1946  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1035304  # from ase_npm_downloads
  github_repo: "cloudflare/cloudflare-go"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ElevenLabs Voiceover Generator for Long-Form Content

Splits blog posts or scripts into optimal chunks under ElevenLabs character limits, synthesizes each chunk using the v2 Multilingual model, and stitches MP3 segments together with pydub. Supports custom voice cloning via stored Voice IDs with per-segment stability and similarity tuning. Final audio is uploaded to Cloudflare R2 and a signed URL is returned.

## Overview

Splits blog posts or scripts into optimal chunks under ElevenLabs character limits, synthesizes each chunk using the v2 Multilingual model, and stitches MP3 segments together with pydub. Supports custom voice cloning via stored Voice IDs with per-segment stability and similarity tuning. Final audio is uploaded to Cloudflare R2 and a signed URL is returned.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a codex
```

### OpenClaw

```bash
clawhub install elevenlabs-voiceover-longform
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elevenlabs-voiceover-longform/
