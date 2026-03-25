---
name: "Content Readability Analyzer"
description: "Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API."
category: "Content Writing & SEO"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/content-readability-analyzer-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Content Readability Analyzer

Scores content using Flesch-Kincaid, Gunning Fog, and SMOG readability indices via textstat Python library. Provides sentence-level rewrite suggestions using OpenAI GPT-4o API.

## Overview

The Content Readability Analyzer evaluates written content across multiple readability metrics to ensure optimal audience comprehension. It uses the textstat Python library to compute Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index simultaneously. Each paragraph receives a composite readability score with visual highlighting for sentences that exceed target complexity thresholds. The skill identifies passive voice constructions using spaCy dependency parsing and suggests active voice alternatives. Long sentences over 25 words are flagged with specific split points identified via syntactic analysis. Technical jargon detection uses a custom dictionary augmented by the WordNet lexical database for domain-specific terminology. When rewriting is needed, the skill calls the OpenAI GPT-4o API with constrained generation parameters to produce simplified alternatives that preserve meaning. Output includes a detailed report with before/after comparisons and readability score improvements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill content-readability-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill content-readability-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill content-readability-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill content-readability-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install content-readability-analyzer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/content-readability-analyzer-agent/
