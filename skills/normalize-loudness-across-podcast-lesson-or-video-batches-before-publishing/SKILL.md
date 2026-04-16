---
title: "Normalize loudness across podcast, lesson, or video batches before publishing"
description: "Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery."
verification: "security_reviewed"
source: "https://github.com/slhck/ffmpeg-normalize"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1500
---

# Normalize loudness across podcast, lesson, or video batches before publishing

This ASE entry is built around ffmpeg-normalize, the open source utility maintained at slhck/ffmpeg-normalize. The agent behavior is narrow and concrete: take one or more audio or video files, analyze their loudness, and produce normalized output that meets a chosen target before publication or review. That is useful for podcast batches, course recordings, webinar exports, internal training videos, and any queue where inconsistent source volume creates a rough handoff for listeners or downstream editors.


Use this when the task is loudness normalization as a repeatable pipeline step. An agent can run it before sending content for approval, before uploading to a CMS, or after collecting mixed recordings from different contributors. It is a better fit than using ffmpeg manually when the need is specifically consistent loudness handling with clear targets such as EBU R128, RMS, or peak normalization, plus predictable batch behavior. It is also a better fit than opening a full editing suite when the job is not creative sound design, but clean leveling across many files.


The boundary keeps this skill from turning into a generic media-tool card. This is not a full nonlinear editor, not a general transcoding catalog entry, and not a catch-all ffmpeg listing. The scope is loudness analysis and normalization only. Integration points include ffmpeg-based media pipelines, Python automation, shell jobs, scheduled ingest workflows, podcast publishing systems, and review queues that need output files with stable perceived volume before the next step.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
