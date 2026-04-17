---
title: "RunwayML Gen-3 Alpha Video Composer"
description: "The RunwayML Gen-3 Alpha Video Composer automates AI video generation by orchestrating the RunwayML API for Gen-3 Alpha model access. It submits generation tasks via the RunwayML REST API with configurable parameters including prompt text, seed image, motion amount, and duration settings. The skill manages the asynchronous generation workflow by polling task status endpoints until completion, handling rate limits and queue positions gracefully. Generated video clips are downloaded and can be sequenced into longer compositions using FFmpeg for concatenation, crossfade transitions, and audio track overlay. The skill supports image-to-video mode where a reference frame is uploaded via the RunwayML Assets API and used as the first frame for temporally consistent generation. Batch generation handles multiple scenes described in a shot list format, generating each scene independently and assembling them in order. Output videos are encoded with configurable codec settings including H.264 for web delivery and ProRes for editing workflows. The skill tracks generation credits and estimated costs per task."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# RunwayML Gen-3 Alpha Video Composer

The RunwayML Gen-3 Alpha Video Composer automates AI video generation by orchestrating the RunwayML API for Gen-3 Alpha model access. It submits generation tasks via the RunwayML REST API with configurable parameters including prompt text, seed image, motion amount, and duration settings. The skill manages the asynchronous generation workflow by polling task status endpoints until completion, handling rate limits and queue positions gracefully. Generated video clips are downloaded and can be sequenced into longer compositions using FFmpeg for concatenation, crossfade transitions, and audio track overlay. The skill supports image-to-video mode where a reference frame is uploaded via the RunwayML Assets API and used as the first frame for temporally consistent generation. Batch generation handles multiple scenes described in a shot list format, generating each scene independently and assembling them in order. Output videos are encoded with configurable codec settings including H.264 for web delivery and ProRes for editing workflows. The skill tracks generation credits and estimated costs per task.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/runwayml-gen-3-alpha-video-composer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/runwayml-gen-3-alpha-video-composer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runwayml-gen-3-alpha-video-composer/)
