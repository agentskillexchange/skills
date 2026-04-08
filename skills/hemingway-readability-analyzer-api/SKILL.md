---
title: Hemingway Readability Analyzer API
description: 'The Hemingway Readability Analyzer provides automated content quality
  analysis for writers, editors, and content teams. It computes multiple readability
  metrics using the textstat Python library: Flesch-Kincaid Grade Level, Gunning Fog
  Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index, presenting
  both individual scores and a weighted composite. Beyond basic metrics, the skill
  performs deep linguistic analysis using spaCy’s dependency parser to identify passive
  voice constructions (nsubjpass dependency relations), flag sentences exceeding configurable
  complexity thresholds (based on clause count and subordination depth), and measure
  adverb density against target percentages. Sentence-level highlighting marks issues
  with severity ratings: hard-to-read (yellow) and very-hard-to-read (red) based on
  word count and syllable density. The tool generates actionable suggestions for simplification
  including sentence splitting recommendations, passive-to-active voice rewrites,
  and simpler synonym suggestions via WordNet through NLTK. Output formats include
  annotated HTML with inline highlights, JSON reports for CMS integration, and Markdown
  summaries. Batch mode processes multiple documents with comparative scoring and
  trend tracking across content revisions.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/
category:
- Content Writing &amp; SEO
framework:
- Cursor
---

# Hemingway Readability Analyzer API

The Hemingway Readability Analyzer provides automated content quality analysis for writers, editors, and content teams. It computes multiple readability metrics using the textstat Python library: Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index, presenting both individual scores and a weighted composite. Beyond basic metrics, the skill performs deep linguistic analysis using spaCy’s dependency parser to identify passive voice constructions (nsubjpass dependency relations), flag sentences exceeding configurable complexity thresholds (based on clause count and subordination depth), and measure adverb density against target percentages. Sentence-level highlighting marks issues with severity ratings: hard-to-read (yellow) and very-hard-to-read (red) based on word count and syllable density. The tool generates actionable suggestions for simplification including sentence splitting recommendations, passive-to-active voice rewrites, and simpler synonym suggestions via WordNet through NLTK. Output formats include annotated HTML with inline highlights, JSON reports for CMS integration, and Markdown summaries. Batch mode processes multiple documents with comparative scoring and trend tracking across content revisions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hemingway-readability-analyzer-api/)
