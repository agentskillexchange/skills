---
name: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
category: "Media &amp; Transcription"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/"
---
# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

OpenAI Whisper Batch Transcription Pipeline is built around OpenAI Whisper speech recognition model. The underlying ecosystem is represented by openai/whisper (96,530+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like local transcription, language detection, timestamps, subtitle formats, model sizes and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to whisper so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English. The implementation typically relies on local transcription, language detection, timestamps, subtitle formats, model sizes, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses local transcription, language detection, timestamps, subtitle formats, model sizes instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as audio transcription, subtitle generation, and speech pipelines.

Key integration points include audio transcription, subtitle generation, and speech pipelines. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline -a codex
```

### OpenClaw

```bash
clawhub install whisper-batch-transcription-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
