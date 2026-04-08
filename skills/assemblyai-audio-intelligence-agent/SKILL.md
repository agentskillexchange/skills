---
title: AssemblyAI Audio Intelligence Agent
description: Analyze audio content using AssemblyAI’s Audio Intelligence models to
  extract structured data beyond basic transcription. This skill leverages the AssemblyAI
  API v2 for advanced audio analysis workflows. The transcription pipeline uploads
  audio via POST /v2/upload, creates transcript jobs with audio_intelligence features
  enabled, and polls for completion. Supported intelligence models include sentiment
  analysis per utterance, entity detection (PII, names, locations, monetary amounts),
  topic detection using the IAB taxonomy, and auto-chapter generation with summary
  headlines. Speaker diarization identifies individual speakers and labels utterances
  for meeting transcript formatting. Content safety detection flags sensitive topics
  across configurable severity thresholds. PII redaction can be applied to both text
  output and audio files with configurable entity types. The assemblyai Python SDK
  (v0.20+) provides high-level wrappers for the REST API with automatic polling and
  webhook support. Real-time transcription uses WebSocket streaming for live audio
  feeds with interim result callbacks. Batch processing handles multiple files with
  parallel job submission and result aggregation into structured JSON or SRT output
  formats. Rate limit management includes automatic throttling and retry logic for
  the 200 concurrent transcript limit.
verification: security_reviewed
source: https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/
category:
- Media &amp; Transcription
framework:
- MCP
---

# AssemblyAI Audio Intelligence Agent

Analyze audio content using AssemblyAI’s Audio Intelligence models to extract structured data beyond basic transcription. This skill leverages the AssemblyAI API v2 for advanced audio analysis workflows. The transcription pipeline uploads audio via POST /v2/upload, creates transcript jobs with audio_intelligence features enabled, and polls for completion. Supported intelligence models include sentiment analysis per utterance, entity detection (PII, names, locations, monetary amounts), topic detection using the IAB taxonomy, and auto-chapter generation with summary headlines. Speaker diarization identifies individual speakers and labels utterances for meeting transcript formatting. Content safety detection flags sensitive topics across configurable severity thresholds. PII redaction can be applied to both text output and audio files with configurable entity types. The assemblyai Python SDK (v0.20+) provides high-level wrappers for the REST API with automatic polling and webhook support. Real-time transcription uses WebSocket streaming for live audio feeds with interim result callbacks. Batch processing handles multiple files with parallel job submission and result aggregation into structured JSON or SRT output formats. Rate limit management includes automatic throttling and retry logic for the 200 concurrent transcript limit.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/)
