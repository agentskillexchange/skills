---
title: "YouTube Chapter Generator from Transcripts"
description: "Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance."
slug: "youtube-chapter-generator-transcripts"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/"
listed: true
---

# YouTube Chapter Generator from Transcripts

Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance.

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
clawhub install youtube-chapter-generator-transcripts
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The YouTube Chapter Generator analyzes video transcripts to automatically create semantically meaningful chapter markers that enhance viewer navigation and SEO discoverability. It uses natural language processing to identify topic boundaries within long-form video content.
Key Capabilities
This skill extracts transcripts using the youtube-transcript-api Python library, supporting both auto-generated and manual captions across multiple languages. It applies sentence-transformers models for computing semantic similarity between transcript segments, identifying natural topic transition points through embedding cosine distance analysis.
Chapter Generation
Segments are clustered using a sliding window approach with configurable minimum chapter duration and similarity thresholds. Each chapter receives an auto-generated title based on extractive summarization of the segment content. Output is formatted as YouTube-compatible chapter timestamps (00:00 format) with titles that comply with YouTube’s description metadata requirements and character limits for optimal search result display.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/)
