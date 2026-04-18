---
title: "YouTube Chapter Generator from Transcripts"
description: "Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# YouTube Chapter Generator from Transcripts

Overview The YouTube Chapter Generator analyzes video transcripts to automatically create semantically meaningful chapter markers that enhance viewer navigation and SEO discoverability. It uses natural language processing to identify topic boundaries within long-form video content.

Key Capabilities This skill extracts transcripts using the youtube-transcript-api Python library, supporting both auto-generated and manual captions across multiple languages. It applies sentence-transformers models for computing semantic similarity between transcript segments, identifying natural topic transition points through embedding cosine distance analysis.

Chapter Generation Segments are clustered using a sliding window approach with configurable minimum chapter duration and similarity thresholds. Each chapter receives an auto-generated title based on extractive summarization of the segment content. Output is formatted as YouTube-compatible chapter timestamps (00:00 format) with titles that comply with YouTube’s description metadata requirements and character limits for optimal search result display.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/youtube-chapter-generator-transcripts
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/youtube-chapter-generator-transcripts` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/)
