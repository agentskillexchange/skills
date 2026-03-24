---
name: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
category: "Media & Transcription"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Overview

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

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

- Marketplace: https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/
