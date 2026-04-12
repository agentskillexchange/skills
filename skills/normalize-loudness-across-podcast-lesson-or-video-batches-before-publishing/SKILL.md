---
title: "Normalize loudness across podcast, lesson, or video batches before publishing"
slug: "normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
source: "https://github.com/slhck/ffmpeg-normalize"
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1499
---

# Normalize loudness across podcast, lesson, or video batches before publishing

Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
