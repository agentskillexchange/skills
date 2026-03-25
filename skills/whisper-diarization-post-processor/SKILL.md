---
name: "Whisper Diarization Post-Processor"
description: "Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation."
category: "Media & Transcription"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/whisper-diarization-post-processor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96570  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Whisper Diarization Post-Processor

Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation.

## Overview

Overview

The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts.

Key Capabilities

This skill processes Whisper output through the `pyannote.audio` speaker diarization pipeline, using pre-trained speaker embedding models from `speechbrain` for voice characterization. It aligns word-level timestamps from `whisper-timestamped` with speaker segments using an optimal assignment algorithm that handles overlapping speech regions.

Output Formats

Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-diarization-post-processor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-diarization-post-processor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-diarization-post-processor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-diarization-post-processor -a codex
```

### OpenClaw

```bash
clawhub install whisper-diarization-post-processor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/whisper-diarization-post-processor/
