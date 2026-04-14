---
title: "Podcast RSS Feed Transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media &amp; Transcription"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
