---
title: "AssemblyAI LeMUR Summarizer"
description: "Summarizes audio content using AssemblyAI’s LeMUR (Large Language Model for Audio Understanding) API. Chains the /v2/transcript endpoint with /lemur/v3/generate/summary for contextual audio intelligence."
slug: "assemblyai-lemur-summarizer-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/"
---

# AssemblyAI LeMUR Summarizer

Summarizes audio content using AssemblyAI’s LeMUR (Large Language Model for Audio Understanding) API. Chains the /v2/transcript endpoint with /lemur/v3/generate/summary for contextual audio intelligence.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install assemblyai-lemur-summarizer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AssemblyAI LeMUR Summarizer combines AssemblyAI’s speech-to-text pipeline with its LeMUR large language model for end-to-end audio understanding. It first submits audio to /v2/transcript with parameters like speaker_labels: true, auto_chapters: true, and entity_detection: true.
Once transcription completes, the agent chains results to LeMUR via /lemur/v3/generate/summary for intelligent summarization that understands context, speaker intent, and discussion topics. It also uses /lemur/v3/generate/action-items for extracting actionable takeaways and /lemur/v3/generate/questions-answers for Q&A extraction.
Supports custom LeMUR prompts via the context and answer_format parameters for domain-specific summaries (legal depositions, medical consultations, earnings calls). Handles real-time streaming via WebSocket at wss://api.assemblyai.com/v2/realtime/ws with interim results. Outputs structured JSON with chapters, entities, sentiment analysis per utterance, and content safety labels.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/)
