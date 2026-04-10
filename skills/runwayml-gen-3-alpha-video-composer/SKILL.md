---
name: RunwayML Gen-3 Alpha Video Composer
description: Composes AI-generated video clips using the RunwayML Gen-3 Alpha API
  with text-to-video and image-to-video modes. Manages generation tasks, polling,
  and output stitching via FFmpeg.
verification: security_reviewed
source: https://github.com/FFmpeg/FFmpeg
category:
- Image &amp; Creative Automation
framework:
- Claude Code
tool_ecosystem:
  github_repo: FFmpeg/FFmpeg
  github_stars: 58548
---
# RunwayML Gen-3 Alpha Video Composer

The RunwayML Gen-3 Alpha Video Composer automates AI video generation by orchestrating the RunwayML API for Gen-3 Alpha model access. It submits generation tasks via the RunwayML REST API with configurable parameters including prompt text, seed image, motion amount, and duration settings. The skill manages the asynchronous generation workflow by polling task status endpoints until completion, handling rate limits and queue positions gracefully. Generated video clips are downloaded and can be sequenced into longer compositions using FFmpeg for concatenation, crossfade transitions, and audio track overlay. The skill supports image-to-video mode where a reference frame is uploaded via the RunwayML Assets API and used as the first frame for temporally consistent generation. Batch generation handles multiple scenes described in a shot list format, generating each scene independently and assembling them in order. Output videos are encoded with configurable codec settings including H.264 for web delivery and ProRes for editing workflows. The skill tracks generation credits and estimated costs per task.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runwayml-gen-3-alpha-video-composer/)
