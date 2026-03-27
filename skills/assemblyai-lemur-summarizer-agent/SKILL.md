---
name: "AssemblyAI LeMUR Summarizer"
description: "Summarizes audio content using AssemblyAI’s LeMUR (Large Language Model for Audio Understanding) API. Chains the /v2/transcript endpoint with /lemur/v3/generate/summary for contextual audio intelligence."
category: "Media & Transcription"
framework: "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/"
---

# AssemblyAI LeMUR Summarizer

Summarizes audio content using AssemblyAI’s LeMUR (Large Language Model for Audio Understanding) API. Chains the /v2/transcript endpoint with /lemur/v3/generate/summary for contextual audio intelligence.

## Overview

AssemblyAI LeMUR Summarizer combines AssemblyAI’s speech-to-text pipeline with its LeMUR large language model for end-to-end audio understanding. It first submits audio to `/v2/transcript` with parameters like `speaker_labels: true`, `auto_chapters: true`, and `entity_detection: true`.

Once transcription completes, the agent chains results to LeMUR via `/lemur/v3/generate/summary` for intelligent summarization that understands context, speaker intent, and discussion topics. It also uses `/lemur/v3/generate/action-items` for extracting actionable takeaways and `/lemur/v3/generate/questions-answers` for Q&A extraction.

Supports custom LeMUR prompts via the `context` and `answer_format` parameters for domain-specific summaries (legal depositions, medical consultations, earnings calls). Handles real-time streaming via WebSocket at `wss://api.assemblyai.com/v2/realtime/ws` with interim results. Outputs structured JSON with chapters, entities, sentiment analysis per utterance, and content safety labels.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill assemblyai-lemur-summarizer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill assemblyai-lemur-summarizer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill assemblyai-lemur-summarizer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill assemblyai-lemur-summarizer-agent -a codex
```

### OpenClaw

```bash
clawhub install assemblyai-lemur-summarizer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/assemblyai-lemur-summarizer-agent/
