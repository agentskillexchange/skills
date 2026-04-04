---
name: "Podcast RSS Feed Transcriber"
category: "Media & Transcription"
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97065
---

# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install podcast-rss-feed-transcriber

# OpenClaw CLI
openclaw skills install podcast-rss-feed-transcriber

# Chat command
/skill install podcast-rss-feed-transcriber

# Direct download
curl -L https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/download -o podcast-rss-feed-transcriber.zip

# Git clone this repo and copy the skill folder
cp -r skills/podcast-rss-feed-transcriber ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
