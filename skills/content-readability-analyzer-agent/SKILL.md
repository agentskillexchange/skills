---
title: "Content Readability Analyzer"
description: "Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API."
verification: "security_reviewed"
source: "https://github.com/textstat/textstat"
category:
  - "Content Writing & SEO"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "textstat/textstat"
  github_stars: 1366
---

# Content Readability Analyzer

The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/content-readability-analyzer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/content-readability-analyzer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/content-readability-analyzer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-readability-analyzer-agent/)
