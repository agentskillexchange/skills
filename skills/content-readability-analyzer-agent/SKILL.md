---
title: "Content Readability Analyzer"
description: "Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/content-readability-analyzer-agent/"
category:
  - "Content Writing & SEO"
framework:
  - "Gemini"
---

# Content Readability Analyzer

The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-readability-analyzer-agent/)
