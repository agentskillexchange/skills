---
title: "OpenAI Whisper Batch Transcription Pipeline"
slug: "whisper-batch-transcription-pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
verification: verified
source: "https://github.com/openai/whisper"
category: "Media & Transcription"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97803
---
# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
