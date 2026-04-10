---
title: "Content Readability Analyzer"
description: "Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API."
slug: "content-readability-analyzer-agent"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/content-readability-analyzer-agent/"
---

# Content Readability Analyzer

Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API.

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
clawhub install content-readability-analyzer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-readability-analyzer-agent/)
