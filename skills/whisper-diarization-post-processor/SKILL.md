---
title: "Whisper Diarization Post-Processor"
description: "Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation."
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
category:
  - "Media & Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
  license: "MIT"
---

# Whisper Diarization Post-Processor

Overview
The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts.


Key Capabilities
This skill processes Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained speaker embedding models from speechbrain for voice characterization. It aligns word-level timestamps from whisper-timestamped with speaker segments using an optimal assignment algorithm that handles overlapping speech regions.


Output Formats
Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-diarization-post-processor/)
