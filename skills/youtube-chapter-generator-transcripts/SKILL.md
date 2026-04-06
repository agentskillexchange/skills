---
name: "YouTube Chapter Generator from Transcripts"
description: "Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance."
category: "Media &amp; Transcription"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/"
---
# YouTube Chapter Generator from Transcripts

Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance.

Overview

The YouTube Chapter Generator analyzes video transcripts to automatically create semantically meaningful chapter markers that enhance viewer navigation and SEO discoverability. It uses natural language processing to identify topic boundaries within long-form video content.

Key Capabilities

This skill extracts transcripts using the youtube-transcript-api Python library, supporting both auto-generated and manual captions across multiple languages. It applies sentence-transformers models for computing semantic similarity between transcript segments, identifying natural topic transition points through embedding cosine distance analysis.

Chapter Generation

Segments are clustered using a sliding window approach with configurable minimum chapter duration and similarity thresholds. Each chapter receives an auto-generated title based on extractive summarization of the segment content. Output is formatted as YouTube-compatible chapter timestamps (00:00 format) with titles that comply with YouTube’s description metadata requirements and character limits for optimal search result display.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill youtube-chapter-generator-transcripts
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill youtube-chapter-generator-transcripts -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill youtube-chapter-generator-transcripts -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill youtube-chapter-generator-transcripts -a codex
```

### OpenClaw

```bash
clawhub install youtube-chapter-generator-transcripts
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/)
