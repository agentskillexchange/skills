---
title: "Force-align narration and transcript text into subtitle or SMIL timing maps"
description: "Use aeneas when an agent already has audio and text, but still needs timing. The workflow aligns spoken narration against fragments of plain text or XML and emits sync maps that can be turned into subtitles, EPUB 3 media overlays, JSON timing data, or other downstream caption assets."
verification: "security_reviewed"
source: "https://github.com/readbeyond/aeneas"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "readbeyond/aeneas"
  github_stars: 2820
---

# Force-align narration and transcript text into subtitle or SMIL timing maps

This ASE entry is built around aeneas, the readbeyond/aeneas project for forced alignment between audio and text. The agent job-to-be-done is clear: take a narration file and its transcript or marked-up source text, align text fragments to the spoken audio, and emit a timing map that downstream systems can use for subtitles, WebVTT, SRT, TTML, JSON, SMIL, CSV, or EPUB media overlays. That is a bounded operational workflow for agents that prepare accessible media or synchronized reading experiences.

Invoke this skill when the user already has both the words and the audio, but the missing piece is time alignment. It fits audiobook chapter prep, language-learning material, accessibility overlays, narrated documentation, podcast chapterization experiments, and subtitle generation pipelines where the transcript exists but timestamps do not. This is not the right tool when the user needs speech recognition from scratch, video editing, or a human subtitle editing workstation. It is specifically for forced alignment, where the text is known and the agent must compute the timing map automatically.

The scope boundary is what keeps the entry skill-shaped. aeneas is not a generic audio platform, CMS, or desktop editor listing. The workflow starts with source audio plus source text and ends with synchronized timing artifacts that another tool can package, render, or review. Integration points include Python scripts, FFmpeg-based preprocessing, eSpeak-backed alignment setups, EPUB production pipelines, subtitle QA loops, and localization workflows that need machine-generated first-pass timings before manual polish. Because the upstream project publishes a real repository, docs, license, release tags, and installation guidance, it clears the evidence gate comfortably.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/force-align-narration-and-transcript-text-into-subtitle-or-smil-timing-maps/)
