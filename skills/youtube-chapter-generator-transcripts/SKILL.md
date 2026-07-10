---
title: "YouTube Chapter Generator from Transcripts"
description: "Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance."
verification: "security_reviewed"
source: "https://developers.google.com/youtube/v3"
author: "Google"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# YouTube Chapter Generator from Transcripts

Extracts YouTube video transcripts via the youtube-transcript-api Python library and generates semantic chapter markers. Uses sentence-transformers for topic segmentation and formats chapter timestamps for YouTube description metadata compliance.

## Prerequisites

Google account, Google Cloud project, YouTube Data API v3 enabled, and OAuth 2.0 credentials or an API key as supported

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a Google Cloud project, enable the YouTube Data API v3, configure credentials, then call the API endpoints documented at the source URL.
```

## Documentation

- https://developers.google.com/youtube/v3

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapter-generator-transcripts/)
