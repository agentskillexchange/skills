---
name: "Hemingway Readability Analyzer API"
description: "Scores content readability using textstat library metrics (Flesch-Kincaid, Gunning Fog, SMOG, Coleman-Liau). Highlights complex sentences, passive voice via spaCy dependency parsing, and adverb density."
category: "Content Writing & SEO"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/"
---

# Hemingway Readability Analyzer API

Scores content readability using textstat library metrics (Flesch-Kincaid, Gunning Fog, SMOG, Coleman-Liau). Highlights complex sentences, passive voice via spaCy dependency parsing, and adverb density.

## Overview

The Hemingway Readability Analyzer provides automated content quality analysis for writers, editors, and content teams. It computes multiple readability metrics using the textstat Python library: Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index, presenting both individual scores and a weighted composite. Beyond basic metrics, the skill performs deep linguistic analysis using spaCy’s dependency parser to identify passive voice constructions (nsubjpass dependency relations), flag sentences exceeding configurable complexity thresholds (based on clause count and subordination depth), and measure adverb density against target percentages. Sentence-level highlighting marks issues with severity ratings: hard-to-read (yellow) and very-hard-to-read (red) based on word count and syllable density. The tool generates actionable suggestions for simplification including sentence splitting recommendations, passive-to-active voice rewrites, and simpler synonym suggestions via WordNet through NLTK. Output formats include annotated HTML with inline highlights, JSON reports for CMS integration, and Markdown summaries. Batch mode processes multiple documents with comparative scoring and trend tracking across content revisions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hemingway-readability-analyzer-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hemingway-readability-analyzer-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hemingway-readability-analyzer-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hemingway-readability-analyzer-api -a codex
```

### OpenClaw

```bash
clawhub install hemingway-readability-analyzer-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/
