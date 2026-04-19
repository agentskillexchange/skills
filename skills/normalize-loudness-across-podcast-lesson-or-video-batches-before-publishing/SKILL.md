---
title: "Normalize loudness across podcast, lesson, or video batches before publishing"
description: "This ASE entry is built around ffmpeg-normalize , the open source utility maintained at slhck/ffmpeg-normalize . The agent behavior is narrow and concrete: take one or more audio or video files, analyze their loudness, and produce normalized output that meets a chosen target before publication or review. That is useful for podcast batches, course recordings, webinar exports, internal training videos, and any queue where inconsistent source volume creates a rough handoff for listeners or downstream editors. Use this when the task is loudness normalization as a repeatable pipeline step . An agent can run it before sending content for approval, before uploading to a CMS, or after collecting mixed recordings from different contributors. It is a better fit than using ffmpeg manually when the need is specifically consistent loudness handling with clear targets such as EBU R128, RMS, or peak normalization, plus predictable batch behavior. It is also a better fit than opening a full editing suite when the job is not creative sound design, but clean leveling across many files. The boundary keeps this skill from turning into a generic media-tool card. This is not a full nonlinear editor, not a general transcoding catalog entry, and not a catch-all ffmpeg listing. The scope is loudness analysis and normalization only. Integration points include ffmpeg-based media pipelines, Python automation, shell jobs, scheduled ingest workflows, podcast publishing systems, and review queues that need output files with stable perceived volume before the next step."
source: "https://github.com/slhck/ffmpeg-normalize"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1500
---

# Normalize loudness across podcast, lesson, or video batches before publishing

This ASE entry is built around ffmpeg-normalize , the open source utility maintained at slhck/ffmpeg-normalize . The agent behavior is narrow and concrete: take one or more audio or video files, analyze their loudness, and produce normalized output that meets a chosen target before publication or review. That is useful for podcast batches, course recordings, webinar exports, internal training videos, and any queue where inconsistent source volume creates a rough handoff for listeners or downstream editors. Use this when the task is loudness normalization as a repeatable pipeline step . An agent can run it before sending content for approval, before uploading to a CMS, or after collecting mixed recordings from different contributors. It is a better fit than using ffmpeg manually when the need is specifically consistent loudness handling with clear targets such as EBU R128, RMS, or peak normalization, plus predictable batch behavior. It is also a better fit than opening a full editing suite when the job is not creative sound design, but clean leveling across many files. The boundary keeps this skill from turning into a generic media-tool card. This is not a full nonlinear editor, not a general transcoding catalog entry, and not a catch-all ffmpeg listing. The scope is loudness analysis and normalization only. Integration points include ffmpeg-based media pipelines, Python automation, shell jobs, scheduled ingest workflows, podcast publishing systems, and review queues that need output files with stable perceived volume before the next step.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
