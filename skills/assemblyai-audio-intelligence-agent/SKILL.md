---
name: "AssemblyAI Audio Intelligence Agent"
description: "Extract structured intelligence from audio using the AssemblyAI API with sentiment analysis, entity detection, topic modeling, and auto-chapter generation. Uses the assemblyai Python SDK for transcript processing pipelines."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
---

# AssemblyAI Audio Intelligence Agent

Analyze audio content using AssemblyAI's Audio Intelligence models to extract structured data beyond basic transcription. This skill leverages the AssemblyAI API v2 for advanced audio analysis workflows.
The transcription pipeline uploads audio via POST /v2/upload, creates transcript jobs with audio_intelligence features enabled, and polls for completion. Supported intelligence models include sentiment analysis per utterance, entity detection (PII, names, locations, monetary amounts), topic detection using the IAB taxonomy, and auto-chapter generation with summary headlines.
Speaker diarization identifies individual speakers and labels utterances for meeting transcript formatting. Content safety detection flags sensitive topics across configurable severity thresholds. PII redaction can be applied to both text output and audio files with configurable entity types.
The assemblyai Python SDK (v0.20+) provides high-level wrappers for the REST API with automatic polling and webhook support. Real-time transcription uses WebSocket streaming for live audio feeds with interim result callbacks.
Batch processing handles multiple files with parallel job submission and result aggregation into structured JSON or SRT output formats. Rate limit management includes automatic throttling and retry logic for the 200 concurrent transcript limit.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/)
