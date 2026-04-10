---
title: "RunwayML Gen-3 Alpha Video Composer"
description: "Composes AI-generated video clips using the RunwayML Gen-3 Alpha API with text-to-video and image-to-video modes. Manages generation tasks, polling, and output stitching via FFmpeg."
slug: "runwayml-gen-3-alpha-video-composer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# RunwayML Gen-3 Alpha Video Composer

Composes AI-generated video clips using the RunwayML Gen-3 Alpha API with text-to-video and image-to-video modes. Manages generation tasks, polling, and output stitching via FFmpeg.

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
clawhub install runwayml-gen-3-alpha-video-composer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The RunwayML Gen-3 Alpha Video Composer automates AI video generation by orchestrating the RunwayML API for Gen-3 Alpha model access. It submits generation tasks via the RunwayML REST API with configurable parameters including prompt text, seed image, motion amount, and duration settings. The skill manages the asynchronous generation workflow by polling task status endpoints until completion, handling rate limits and queue positions gracefully. Generated video clips are downloaded and can be sequenced into longer compositions using FFmpeg for concatenation, crossfade transitions, and audio track overlay. The skill supports image-to-video mode where a reference frame is uploaded via the RunwayML Assets API and used as the first frame for temporally consistent generation. Batch generation handles multiple scenes described in a shot list format, generating each scene independently and assembling them in order. Output videos are encoded with configurable codec settings including H.264 for web delivery and ProRes for editing workflows. The skill tracks generation credits and estimated costs per task.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runwayml-gen-3-alpha-video-composer/)
