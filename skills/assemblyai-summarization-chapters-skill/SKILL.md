---
title: AssemblyAI Summarization & Chapters Skill
description: 'This skill integrates with AssemblyAI’s transcription and audio intelligence
  API to provide comprehensive audio analysis beyond basic transcription. It uses
  the AssemblyAI Python SDK: client = assemblyai.Client(api_key=key) and initiates
  transcription via transcript = client.transcribe(audio_url, config=TranscriptionConfig(auto_chapters=True,
  sentiment_analysis=True, content_safety=True, entity_detection=True)). The auto_chapters
  feature automatically segments audio into topical chapters with gist, headline,
  and summary for each segment, along with start/end timestamps. Sentiment analysis
  provides per-sentence sentiment labels (POSITIVE, NEGATIVE, NEUTRAL) with confidence
  scores. Content safety detection flags sensitive content categories (profanity,
  violence, drugs, etc.) with severity scores and timestamp ranges. Entity detection
  identifies and categorizes PII including names, locations, organizations, dates,
  and phone numbers using the entity_detection parameter. The skill supports webhook
  callbacks via webhook_url parameter for async processing of long recordings. It
  handles file uploads using client.upload(local_path) for local files and accepts
  direct URLs for cloud-hosted audio. Rate limiting is managed with exponential backoff
  on 429 responses. Output is structured as JSON with sections for full transcript,
  chapters array, sentiment timeline, detected entities, and content safety report.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/
category:
- Media &amp; Transcription
framework:
- Claude Agents
---

# AssemblyAI Summarization & Chapters Skill

This skill integrates with AssemblyAI’s transcription and audio intelligence API to provide comprehensive audio analysis beyond basic transcription. It uses the AssemblyAI Python SDK: client = assemblyai.Client(api_key=key) and initiates transcription via transcript = client.transcribe(audio_url, config=TranscriptionConfig(auto_chapters=True, sentiment_analysis=True, content_safety=True, entity_detection=True)). The auto_chapters feature automatically segments audio into topical chapters with gist, headline, and summary for each segment, along with start/end timestamps. Sentiment analysis provides per-sentence sentiment labels (POSITIVE, NEGATIVE, NEUTRAL) with confidence scores. Content safety detection flags sensitive content categories (profanity, violence, drugs, etc.) with severity scores and timestamp ranges. Entity detection identifies and categorizes PII including names, locations, organizations, dates, and phone numbers using the entity_detection parameter. The skill supports webhook callbacks via webhook_url parameter for async processing of long recordings. It handles file uploads using client.upload(local_path) for local files and accepts direct URLs for cloud-hosted audio. Rate limiting is managed with exponential backoff on 429 responses. Output is structured as JSON with sections for full transcript, chapters array, sentiment timeline, detected entities, and content safety report.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/)
