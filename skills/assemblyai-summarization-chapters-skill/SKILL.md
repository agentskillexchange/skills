---
title: "AssemblyAI Summarization & Chapters Skill"
description: "Transcribes audio and generates auto-chapters with summaries using AssemblyAI’s /v2/transcript endpoint with auto_chapters=true. Extracts key topics, sentiment analysis, and content safety labels via AssemblyAI SDK."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Agents"
---

# AssemblyAI Summarization & Chapters Skill

This skill integrates with AssemblyAI’s transcription and audio intelligence API to provide comprehensive audio analysis beyond basic transcription. It uses the AssemblyAI Python SDK: client = assemblyai.Client(api_key=key) and initiates transcription via transcript = client.transcribe(audio_url, config=TranscriptionConfig(auto_chapters=True, sentiment_analysis=True, content_safety=True, entity_detection=True)). The auto_chapters feature automatically segments audio into topical chapters with gist, headline, and summary for each segment, along with start/end timestamps. Sentiment analysis provides per-sentence sentiment labels (POSITIVE, NEGATIVE, NEUTRAL) with confidence scores. Content safety detection flags sensitive content categories (profanity, violence, drugs, etc.) with severity scores and timestamp ranges. Entity detection identifies and categorizes PII including names, locations, organizations, dates, and phone numbers using the entity_detection parameter. The skill supports webhook callbacks via webhook_url parameter for async processing of long recordings. It handles file uploads using client.upload(local_path) for local files and accepts direct URLs for cloud-hosted audio. Rate limiting is managed with exponential backoff on 429 responses. Output is structured as JSON with sections for full transcript, chapters array, sentiment timeline, detected entities, and content safety report.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/)
