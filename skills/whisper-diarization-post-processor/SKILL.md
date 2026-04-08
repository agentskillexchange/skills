---
title: Whisper Diarization Post-Processor
description: Overview The Whisper Diarization Post-Processor enhances raw OpenAI Whisper
  transcription output by adding speaker identification and precise timestamp alignment.
  It combines state-of-the-art speech recognition with neural speaker diarization
  for production-quality meeting transcripts. Key Capabilities This skill processes
  Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained
  speaker embedding models from speechbrain for voice characterization. It aligns
  word-level timestamps from whisper-timestamped with speaker segments using an optimal
  assignment algorithm that handles overlapping speech regions. Output Formats Generates
  formatted transcripts with speaker labels, timestamps, and confidence scores in
  multiple output formats including SRT, VTT, and structured JSON. Supports custom
  speaker name mapping through voice enrollment, handles multi-language transcription
  with automatic language detection, and produces analytics summaries including per-speaker
  talk time ratios, interruption counts, and topic transition markers for meeting
  intelligence dashboards.
verification: security_reviewed
source: https://agentskillexchange.com/skills/whisper-diarization-post-processor/
category:
- Media &amp; Transcription
framework:
- Claude Code
---

# Whisper Diarization Post-Processor

Overview The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts. Key Capabilities This skill processes Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained speaker embedding models from speechbrain for voice characterization. It aligns word-level timestamps from whisper-timestamped with speaker segments using an optimal assignment algorithm that handles overlapping speech regions. Output Formats Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-diarization-post-processor/)
