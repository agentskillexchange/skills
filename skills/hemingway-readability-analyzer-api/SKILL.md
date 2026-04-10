---
title: "Hemingway Readability Analyzer API"
description: "Scores content readability using textstat library metrics (Flesch-Kincaid, Gunning Fog, SMOG, Coleman-Liau). Highlights complex sentences, passive voice via spaCy dependency parsing, and adverb density."
slug: "hemingway-readability-analyzer-api"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/"
---

# Hemingway Readability Analyzer API

Scores content readability using textstat library metrics (Flesch-Kincaid, Gunning Fog, SMOG, Coleman-Liau). Highlights complex sentences, passive voice via spaCy dependency parsing, and adverb density.

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
clawhub install hemingway-readability-analyzer-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Hemingway Readability Analyzer provides automated content quality analysis for writers, editors, and content teams. It computes multiple readability metrics using the textstat Python library: Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index, presenting both individual scores and a weighted composite. Beyond basic metrics, the skill performs deep linguistic analysis using spaCy’s dependency parser to identify passive voice constructions (nsubjpass dependency relations), flag sentences exceeding configurable complexity thresholds (based on clause count and subordination depth), and measure adverb density against target percentages. Sentence-level highlighting marks issues with severity ratings: hard-to-read (yellow) and very-hard-to-read (red) based on word count and syllable density. The tool generates actionable suggestions for simplification including sentence splitting recommendations, passive-to-active voice rewrites, and simpler synonym suggestions via WordNet through NLTK. Output formats include annotated HTML with inline highlights, JSON reports for CMS integration, and Markdown summaries. Batch mode processes multiple documents with comparative scoring and trend tracking across content revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/)
