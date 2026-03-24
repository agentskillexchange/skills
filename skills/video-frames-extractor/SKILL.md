---
name: "Video Frames Extractor"
description: "Extract frames and short clips from videos."
category: "Media & Transcription"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/video-frames-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Video Frames Extractor

Extract frames and short clips from videos.

## Overview

Video Frames Extractor makes ffmpeg-backed frame extraction and short clip generation easier to run from agent workflows for review, content prep, and analysis.

Best for

pulling frames from videos

creating short clips

preparing media for review or analysis

Install notes

Install from the OpenClaw skills set and ensure ffmpeg is available on the host machine.

**Source:** OpenClaw official skills.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill video-frames-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill video-frames-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill video-frames-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill video-frames-extractor -a codex
```

### OpenClaw

```bash
clawhub install video-frames-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/video-frames-extractor/
