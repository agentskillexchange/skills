---
name: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
category: "Media & Transcription"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.1
reviews: 3
creator: "Elena Kowalski"
creator_handle: "@ekowalski"
creator_verified: true
source: "https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/"
---
# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install whisper-batch-transcription-pipeline
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-batch-transcription-pipeline -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Media & Transcription |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.1/5 (3 reviews) |

## Creator

**Elena Kowalski** (Verified Creator ✓)
- Profile: [@ekowalski](https://agentskillexchange.com/browse-skills/?creator=ekowalski)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
