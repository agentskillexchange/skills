---
title: "Force-align narration and transcript text into subtitle or SMIL timing maps"
description: "This ASE entry is built around aeneas , the readbeyond/aeneas project for forced alignment between audio and text. The agent job-to-be-done is clear: take a narration file and its transcript or marked-up source text, align text fragments to the spoken audio, and emit a timing map that downstream systems can use for subtitles, WebVTT, SRT, TTML, JSON, SMIL, CSV, or EPUB media overlays. That is a bounded operational workflow for agents that prepare accessible media or synchronized reading experiences. Invoke this skill when the user already has both the words and the audio, but the missing piece is time alignment. It fits audiobook chapter prep, language-learning material, accessibility overlays, narrated documentation, podcast chapterization experiments, and subtitle generation pipelines where the transcript exists but timestamps do not. This is not the right tool when the user needs speech recognition from scratch, video editing, or a human subtitle editing workstation. It is specifically for forced alignment, where the text is known and the agent must compute the timing map automatically. The scope boundary is what keeps the entry skill-shaped. aeneas is not a generic audio platform, CMS, or desktop editor listing. The workflow starts with source audio plus source text and ends with synchronized timing artifacts that another tool can package, render, or review. Integration points include Python scripts, FFmpeg-based preprocessing, eSpeak-backed alignment setups, EPUB production pipelines, subtitle QA loops, and localization workflows that need machine-generated first-pass timings before manual polish. Because the upstream project publishes a real repository, docs, license, release tags, and installation guidance, it clears the evidence gate comfortably."
source: "https://github.com/readbeyond/aeneas"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "readbeyond/aeneas"
  github_stars: 2820
---

# Force-align narration and transcript text into subtitle or SMIL timing maps

This ASE entry is built around aeneas , the readbeyond/aeneas project for forced alignment between audio and text. The agent job-to-be-done is clear: take a narration file and its transcript or marked-up source text, align text fragments to the spoken audio, and emit a timing map that downstream systems can use for subtitles, WebVTT, SRT, TTML, JSON, SMIL, CSV, or EPUB media overlays. That is a bounded operational workflow for agents that prepare accessible media or synchronized reading experiences. Invoke this skill when the user already has both the words and the audio, but the missing piece is time alignment. It fits audiobook chapter prep, language-learning material, accessibility overlays, narrated documentation, podcast chapterization experiments, and subtitle generation pipelines where the transcript exists but timestamps do not. This is not the right tool when the user needs speech recognition from scratch, video editing, or a human subtitle editing workstation. It is specifically for forced alignment, where the text is known and the agent must compute the timing map automatically. The scope boundary is what keeps the entry skill-shaped. aeneas is not a generic audio platform, CMS, or desktop editor listing. The workflow starts with source audio plus source text and ends with synchronized timing artifacts that another tool can package, render, or review. Integration points include Python scripts, FFmpeg-based preprocessing, eSpeak-backed alignment setups, EPUB production pipelines, subtitle QA loops, and localization workflows that need machine-generated first-pass timings before manual polish. Because the upstream project publishes a real repository, docs, license, release tags, and installation guidance, it clears the evidence gate comfortably.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/force-align-narration-and-transcript-text-into-subtitle-or-smil-timing-maps/)
