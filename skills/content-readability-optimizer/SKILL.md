---
name: "Content Readability Optimizer"
description: "Analyzes and optimizes content readability using textstat Python library and Hemingway API patterns. Computes Flesch-Kincaid, Gunning Fog, and SMOG indices with automated rewriting suggestions."
category: "Content Writing & SEO"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/content-readability-optimizer/"
---

# Content Readability Optimizer

Analyzes and optimizes content readability using textstat Python library and Hemingway API patterns. Computes Flesch-Kincaid, Gunning Fog, and SMOG indices with automated rewriting suggestions.

## Overview

The Content Readability Optimizer provides comprehensive text analysis and improvement recommendations using the textstat Python library for readability scoring and NLP-based rewriting suggestions. It evaluates content across multiple readability indices simultaneously.

Core metrics include Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index. The agent identifies specific passages that reduce readability scores, highlighting complex sentences, passive voice usage, adverb density, and jargon patterns that impede comprehension.

Advanced features include audience-targeted optimization where content is adjusted to match specific grade levels, A/B variant generation for different audience segments, and batch processing for large content libraries. The agent integrates with CMS APIs to pull content directly, analyze it, and push optimized versions back. It also generates readability trend reports over time and supports custom vocabulary allowlists for technical domains.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill content-readability-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill content-readability-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill content-readability-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill content-readability-optimizer -a codex
```

### OpenClaw

```bash
clawhub install content-readability-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/content-readability-optimizer/
