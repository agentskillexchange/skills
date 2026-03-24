---
name: "OpenAI Whisper Transcription"
description: "Local speech-to-text transcription without relying on an API."
category: "Media & Transcription"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openai-whisper-transcription/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96530  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAI Whisper Transcription

Local speech-to-text transcription without relying on an API.

## Overview

Wraps the Whisper CLI for local transcription workflows, making it useful where users want privacy-friendly or offline-oriented speech-to-text processing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-transcription
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-transcription -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-transcription -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-transcription -a codex
```

### OpenClaw

```bash
clawhub install openai-whisper-transcription
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openai-whisper-transcription/
