---
title: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
slug: "whisper-batch-transcription-pipeline"
verification: "security_reviewed"
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
1. Install from the Agent Skill Exchange website
2. Clone or download the upstream source repository
3. Install via npm if the project is published there
4. Use the tool's package manager or release binaries
5. Copy the skill files into your local skills directory manually

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
