---
name: "AI Content Readability Optimizer"
description: "Analyzes and optimizes content readability using Flesch-Kincaid scoring, Hemingway Editor API integration, and Grammarly Text API. Generates SEO-optimized rewrites targeting specific grade levels."
category: "Content Writing & SEO"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ai-content-readability-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AI Content Readability Optimizer

Analyzes and optimizes content readability using Flesch-Kincaid scoring, Hemingway Editor API integration, and Grammarly Text API. Generates SEO-optimized rewrites targeting specific grade levels.

## Overview

The AI Content Readability Optimizer performs deep analysis of written content to improve clarity and SEO performance. It calculates Flesch-Kincaid Grade Level and Reading Ease scores, Gunning Fog Index, and Coleman-Liau Index to provide comprehensive readability metrics. The agent integrates with the Hemingway Editor API for sentence complexity detection, identifying adverb overuse, passive voice, and hard-to-read passages. It connects to the Grammarly Text API for grammar and style checking, and uses the LanguageTool API for multilingual support across 30+ languages. The optimizer generates targeted rewrites at specified grade levels while preserving keyword density and SEO intent. It analyzes content against competing SERP results using the DataForSEO API to identify content gaps and semantic opportunities. The agent handles bulk optimization of existing content libraries, processing WordPress posts via WP REST API with progress tracking. Includes readability trend reporting over time using Chart.js visualization and exports to Google Sheets via the Sheets API v4.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ai-content-readability-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ai-content-readability-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ai-content-readability-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ai-content-readability-optimizer -a codex
```

### OpenClaw

```bash
clawhub install ai-content-readability-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ai-content-readability-optimizer/
