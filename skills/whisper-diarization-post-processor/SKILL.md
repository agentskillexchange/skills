---
title: "Whisper Diarization Post-Processor"
description: "Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
---

# Whisper Diarization Post-Processor

Overview
The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts.

Key Capabilities
This skill processes Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained speaker embedding models from speechbrain for voice characterization. It aligns word-level timestamps from whisper-timestamped with speaker segments using an optimal assignment algorithm that handles overlapping speech regions.

Output Formats
Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-diarization-post-processor/)
