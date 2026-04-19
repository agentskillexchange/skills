---
title: "Content Readability Analyzer"
description: "The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements."
source: "https://agentskillexchange.com/skills/content-readability-analyzer-agent/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# Content Readability Analyzer

The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-readability-analyzer-agent/)
