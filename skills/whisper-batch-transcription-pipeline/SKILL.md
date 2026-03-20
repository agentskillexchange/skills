---
name: OpenAI Whisper Batch Transcription Pipeline
description: Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.
category: Media &amp; Transcription
framework: Any Agent
verification: security_reviewed
rating: 4.1
reviews: 3
source: https://agentskillexchange.com/skill/whisper-batch-transcription-pipeline/
---

# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Overview

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline
```

### OpenClaw

```bash
clawhub install whisper-batch-transcription-pipeline
```

### Claude Code

```bash
claude mcp add whisper-batch-transcription-pipeline
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/whisper-batch-transcription-pipeline/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Media &amp; Transcription
- **Framework**: Any Agent
- **Rating**: 4.1/5 (3 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/whisper-batch-transcription-pipeline/)
