---
name: Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill
description: Whishper is an open source self-hosted web app for speech-to-text, translation,
  and subtitle workflows built around Whisper models. This skill covers running Whishper
  with Docker, handling uploads and transcripts, and wiring the output into broader
  automation flows.
category: "Media &amp; Transcription"
framework: Multi-Framework
verification: listed
source: "https://github.com/pluja/whishper"
---
# Whishper Self-Hosted Speech-to-Text and Audio Workflow Skill

Whishper is an open source self-hosted web app for speech-to-text, translation, and subtitle workflows built around Whisper models. This skill covers running Whishper with Docker, handling uploads and transcripts, and wiring the output into broader automation flows.

Whishper is an open source, self-hosted transcription interface maintained by pluja. It packages Whisper-based speech-to-text, translation, subtitle generation, and media processing into a browser-accessible application that teams can run on their own infrastructure. The upstream project ships with Docker-based deployment, a dedicated installation guide, and a clear operational model for uploading audio or video, processing jobs, and exporting usable text artifacts.

This skill is useful when an agent or operator needs a reliable speech-to-text surface without relying on a hosted API. A typical workflow is to deploy Whishper with Docker, feed it recordings, interviews, meetings, or media files, and then use the generated transcript, subtitles, or translated text in downstream summarization, search, or archival workflows. Integration points are straightforward: the stack is self-hosted, the web UI is suitable for manual review, and the output can be copied into note systems, content pipelines, or further AI analysis steps.

From an implementation perspective, the important pieces are the Docker-based runtime, the installation script provided by the project, and the storage layout used by the service containers. This skill maps well to agent workflows that need private media transcription, transcript review, or repeatable subtitle generation on controlled infrastructure.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whishper-self-hosted-speech-to-text-audio-workflow-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whishper-self-hosted-speech-to-text-audio-workflow-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whishper-self-hosted-speech-to-text-audio-workflow-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whishper-self-hosted-speech-to-text-audio-workflow-skill -a codex
```

### OpenClaw

```bash
clawhub install whishper-self-hosted-speech-to-text-audio-workflow-skill
```


## Source

- [GitHub](https://github.com/pluja/whishper)
