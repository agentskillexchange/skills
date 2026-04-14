---
title: "OpenAI Whisper Batch Transcription Pipeline"
slug: "whisper-batch-transcription-pipeline"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
---
# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
