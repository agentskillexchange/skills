---
title: "AssemblyAI LeMUR Summarizer"
description: "AssemblyAI LeMUR Summarizer combines AssemblyAI&#8217;s speech-to-text pipeline with its LeMUR large language model for end-to-end audio understanding. It first submits audio to /v2/transcript with parameters like speaker_labels: true , auto_chapters: true , and entity_detection: true . Once transcription completes, the agent chains results to LeMUR via /lemur/v3/generate/summary for intelligent summarization that understands context, speaker intent, and discussion topics. It also uses /lemur/v3/generate/action-items for extracting actionable takeaways and /lemur/v3/generate/questions-answers for Q&#038;A extraction. Supports custom LeMUR prompts via the context and answer_format parameters for domain-specific summaries (legal depositions, medical consultations, earnings calls). Handles real-time streaming via WebSocket at wss://api.assemblyai.com/v2/realtime/ws with interim results. Outputs structured JSON with chapters, entities, sentiment analysis per utterance, and content safety labels."
source: "https://www.assemblyai.com/docs"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
---

# AssemblyAI LeMUR Summarizer

AssemblyAI LeMUR Summarizer combines AssemblyAI&#8217;s speech-to-text pipeline with its LeMUR large language model for end-to-end audio understanding. It first submits audio to /v2/transcript with parameters like speaker_labels: true , auto_chapters: true , and entity_detection: true . Once transcription completes, the agent chains results to LeMUR via /lemur/v3/generate/summary for intelligent summarization that understands context, speaker intent, and discussion topics. It also uses /lemur/v3/generate/action-items for extracting actionable takeaways and /lemur/v3/generate/questions-answers for Q&#038;A extraction. Supports custom LeMUR prompts via the context and answer_format parameters for domain-specific summaries (legal depositions, medical consultations, earnings calls). Handles real-time streaming via WebSocket at wss://api.assemblyai.com/v2/realtime/ws with interim results. Outputs structured JSON with chapters, entities, sentiment analysis per utterance, and content safety labels.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/)
