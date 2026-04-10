---
name: AssemblyAI LeMUR Summarizer
description: Summarizes audio content using AssemblyAI&#8217;s LeMUR (Large Language
  Model for Audio Understanding) API. Chains the /v2/transcript endpoint with /lemur/v3/generate/summary
  for contextual audio intelligence.
verification: security_reviewed
source: https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/
category:
- Media &amp; Transcription
framework:
- Gemini
---
# AssemblyAI LeMUR Summarizer

AssemblyAI LeMUR Summarizer combines AssemblyAI's speech-to-text pipeline with its LeMUR large language model for end-to-end audio understanding. It first submits audio to /v2/transcript with parameters like speaker_labels: true, auto_chapters: true, and entity_detection: true.
Once transcription completes, the agent chains results to LeMUR via /lemur/v3/generate/summary for intelligent summarization that understands context, speaker intent, and discussion topics. It also uses /lemur/v3/generate/action-items for extracting actionable takeaways and /lemur/v3/generate/questions-answers for Q&A extraction.
Supports custom LeMUR prompts via the context and answer_format parameters for domain-specific summaries (legal depositions, medical consultations, earnings calls). Handles real-time streaming via WebSocket at wss://api.assemblyai.com/v2/realtime/ws with interim results. Outputs structured JSON with chapters, entities, sentiment analysis per utterance, and content safety labels.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/)
