---
name: Hemingway Readability Analyzer API
description: Scores content readability using textstat library metrics (Flesch-Kincaid,
  Gunning Fog, SMOG, Coleman-Liau). Highlights complex sentences, passive voice via
  spaCy dependency parsing, and adverb density.
verification: security_reviewed
source: https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/
category:
- Content Writing &amp; SEO
framework:
- Cursor
---
# Hemingway Readability Analyzer API

The Hemingway Readability Analyzer provides automated content quality analysis for writers, editors, and content teams. It computes multiple readability metrics using the textstat Python library: Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index, presenting both individual scores and a weighted composite. Beyond basic metrics, the skill performs deep linguistic analysis using spaCy's dependency parser to identify passive voice constructions (nsubjpass dependency relations), flag sentences exceeding configurable complexity thresholds (based on clause count and subordination depth), and measure adverb density against target percentages. Sentence-level highlighting marks issues with severity ratings: hard-to-read (yellow) and very-hard-to-read (red) based on word count and syllable density. The tool generates actionable suggestions for simplification including sentence splitting recommendations, passive-to-active voice rewrites, and simpler synonym suggestions via WordNet through NLTK. Output formats include annotated HTML with inline highlights, JSON reports for CMS integration, and Markdown summaries. Batch mode processes multiple documents with comparative scoring and trend tracking across content revisions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/)
