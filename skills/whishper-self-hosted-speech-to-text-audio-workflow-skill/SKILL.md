---
title: "Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill"
description: "Whishper is an open source self-hosted web app for speech-to-text, translation, and subtitle workflows built around Whisper models. This skill covers running Whishper with Docker, handling uploads and transcripts, and wiring the output into broader automation flows."
slug: "whishper-self-hosted-speech-to-text-audio-workflow-skill"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/pluja/whishper"
tool_ecosystem:
  github_repo: "pluja/whishper"
  github_stars: 2971
---

# Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill

Whishper is an open source self-hosted web app for speech-to-text, translation, and subtitle workflows built around Whisper models. This skill covers running Whishper with Docker, handling uploads and transcripts, and wiring the output into broader automation flows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install whishper-self-hosted-speech-to-text-audio-workflow-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Whishper is an open source, self-hosted transcription interface maintained by pluja. It packages Whisper-based speech-to-text, translation, subtitle generation, and media processing into a browser-accessible application that teams can run on their own infrastructure. The upstream project ships with Docker-based deployment, a dedicated installation guide, and a clear operational model for uploading audio or video, processing jobs, and exporting usable text artifacts.
This skill is useful when an agent or operator needs a reliable speech-to-text surface without relying on a hosted API. A typical workflow is to deploy Whishper with Docker, feed it recordings, interviews, meetings, or media files, and then use the generated transcript, subtitles, or translated text in downstream summarization, search, or archival workflows. Integration points are straightforward: the stack is self-hosted, the web UI is suitable for manual review, and the output can be copied into note systems, content pipelines, or further AI analysis steps.
From an implementation perspective, the important pieces are the Docker-based runtime, the installation script provided by the project, and the storage layout used by the service containers. This skill maps well to agent workflows that need private media transcription, transcript review, or repeatable subtitle generation on controlled infrastructure.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whishper-self-hosted-speech-to-text-audio-workflow-skill/)
