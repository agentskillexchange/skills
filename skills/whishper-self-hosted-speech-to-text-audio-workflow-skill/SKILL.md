---
name: Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill
description: Whishper is an open source self-hosted web app for speech-to-text, translation,
  and subtitle workflows built around Whisper models. This skill covers running Whishper
  with Docker, handling uploads and transcripts, and wiring the output into broader
  automation flows.
verification: security_reviewed
source: https://github.com/pluja/whishper
category:
- Media &amp; Transcription
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: pluja/whishper
  github_stars: 2971
---
# Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill

Whishper is an open source, self-hosted transcription interface maintained by pluja. It packages Whisper-based speech-to-text, translation, subtitle generation, and media processing into a browser-accessible application that teams can run on their own infrastructure. The upstream project ships with Docker-based deployment, a dedicated installation guide, and a clear operational model for uploading audio or video, processing jobs, and exporting usable text artifacts.
This skill is useful when an agent or operator needs a reliable speech-to-text surface without relying on a hosted API. A typical workflow is to deploy Whishper with Docker, feed it recordings, interviews, meetings, or media files, and then use the generated transcript, subtitles, or translated text in downstream summarization, search, or archival workflows. Integration points are straightforward: the stack is self-hosted, the web UI is suitable for manual review, and the output can be copied into note systems, content pipelines, or further AI analysis steps.
From an implementation perspective, the important pieces are the Docker-based runtime, the installation script provided by the project, and the storage layout used by the service containers. This skill maps well to agent workflows that need private media transcription, transcript review, or repeatable subtitle generation on controlled infrastructure.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whishper-self-hosted-speech-to-text-audio-workflow-skill/)
