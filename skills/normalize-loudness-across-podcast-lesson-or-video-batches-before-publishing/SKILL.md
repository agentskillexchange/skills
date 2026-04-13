---
title: "Normalize loudness across podcast, lesson, or video batches before publishing"
description: "Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery."
verification: "security_reviewed"
source: "https://github.com/slhck/ffmpeg-normalize"
category: ["Media &amp; Transcription"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1500
---

# Normalize loudness across podcast, lesson, or video batches before publishing

Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
