---
name: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
category: "Media & Transcription"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/"
tool_ecosystem:
  tool: "whisper"
  github_stars: 10761
  npm_weekly_downloads: 16275389
  github_repo: "openai/openai-node"
  license: "Apache-2.0"
  maintained: true
---

# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Media & Transcription |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | [whisper](https://github.com/openai/openai-node) — ⭐ 10.8k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
