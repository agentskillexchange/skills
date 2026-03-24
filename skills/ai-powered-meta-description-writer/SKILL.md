---
name: "AI-Powered Meta Description Writer"
description: "Generates optimized meta descriptions using OpenAI Chat Completions API with token-aware truncation. Integrates with Yoast SEO REST API fields and Google SERP Preview validation for CTR optimization."
category: "Content Writing & SEO"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ai-powered-meta-description-writer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AI-Powered Meta Description Writer

Generates optimized meta descriptions using OpenAI Chat Completions API with token-aware truncation. Integrates with Yoast SEO REST API fields and Google SERP Preview validation for CTR optimization.

## Overview

This skill automates meta description generation for large-scale websites using the OpenAI Chat Completions API with gpt-4o-mini for cost efficiency. It fetches existing page content through the WordPress REST API, extracts key themes using TF-IDF scoring, and generates compelling meta descriptions within the 155-character SERP display limit. The agent integrates directly with Yoast SEO plugin REST fields (yoast_head_json.description) for seamless WordPress updates. Each generated description includes the primary target keyword within the first 70 characters, a clear value proposition, and a call-to-action phrase. Google SERP Preview validation checks pixel width rendering using a canvas measureText approximation to ensure descriptions display without truncation on desktop and mobile. The skill processes pages in batches of 50, using wp_remote_post() for OpenAI API calls with configurable temperature settings. A/B testing support generates multiple variants per page with confidence interval tracking. Performance tracking integrates with Google Search Console API to measure CTR changes post-update.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ai-powered-meta-description-writer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ai-powered-meta-description-writer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ai-powered-meta-description-writer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ai-powered-meta-description-writer -a codex
```

### OpenClaw

```bash
clawhub install ai-powered-meta-description-writer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ai-powered-meta-description-writer/
