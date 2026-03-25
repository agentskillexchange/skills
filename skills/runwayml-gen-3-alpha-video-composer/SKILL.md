---
name: "RunwayML Gen-3 Alpha Video Composer"
description: "Composes AI-generated video clips using the RunwayML Gen-3 Alpha API with text-to-video and image-to-video modes. Manages generation tasks, polling, and output stitching via FFmpeg."
category: "42"
framework: "33"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/runwayml-gen-3-alpha-video-composer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# RunwayML Gen-3 Alpha Video Composer

Composes AI-generated video clips using the RunwayML Gen-3 Alpha API with text-to-video and image-to-video modes. Manages generation tasks, polling, and output stitching via FFmpeg.

## Overview

The RunwayML Gen-3 Alpha Video Composer automates AI video generation by orchestrating the RunwayML API for Gen-3 Alpha model access. It submits generation tasks via the RunwayML REST API with configurable parameters including prompt text, seed image, motion amount, and duration settings. The skill manages the asynchronous generation workflow by polling task status endpoints until completion, handling rate limits and queue positions gracefully. Generated video clips are downloaded and can be sequenced into longer compositions using FFmpeg for concatenation, crossfade transitions, and audio track overlay. The skill supports image-to-video mode where a reference frame is uploaded via the RunwayML Assets API and used as the first frame for temporally consistent generation. Batch generation handles multiple scenes described in a shot list format, generating each scene independently and assembling them in order. Output videos are encoded with configurable codec settings including H.264 for web delivery and ProRes for editing workflows. The skill tracks generation credits and estimated costs per task.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill runwayml-gen-3-alpha-video-composer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill runwayml-gen-3-alpha-video-composer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill runwayml-gen-3-alpha-video-composer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill runwayml-gen-3-alpha-video-composer -a codex
```

### OpenClaw

```bash
clawhub install runwayml-gen-3-alpha-video-composer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/runwayml-gen-3-alpha-video-composer/
