---
name: "Audit AI search citation readiness with GEO Optimizer"
slug: "audit-ai-search-citation-readiness-with-geo-optimizer"
description: "Use GEO Optimizer from the CLI or MCP so agents can audit a site for AI search visibility, generate llms.txt/schema fixes, check bot access, and track citation readiness."
github_stars: 611
verification: "security_reviewed"
source: "https://github.com/Auriti-Labs/geo-optimizer-skill"
author: "Juan Camilo Auriti / Auriti Labs"
publisher_type: "organization"
category: "Content Writing & SEO"
framework: "MCP"
tool_ecosystem:
  github_repo: "Auriti-Labs/geo-optimizer-skill"
  github_stars: 611
---

# Audit AI search citation readiness with GEO Optimizer

Use GEO Optimizer from the CLI or MCP so agents can audit a site for AI search visibility, generate llms.txt/schema fixes, check bot access, and track citation readiness.

## Prerequisites

Python 3.9+; geo-optimizer-skill package; optional MCP client such as Claude Code, Cursor, Windsurf, or another MCP-capable runtime; optional Perplexity/OpenAI/Anthropic keys for live citation checks

## Installation

Install the CLI package:

- pip install geo-optimizer-skill

Prerequisite: Python 3.9 or newer. To run one audit without installing into the current environment:

- uvx --from geo-optimizer-skill geo audit --url https://yoursite.com

After installation, run a basic audit:

- geo audit --url https://yoursite.com

- Source: https://github.com/Auriti-Labs/geo-optimizer-skill
- Extracted from upstream docs: https://raw.githubusercontent.com/Auriti-Labs/geo-optimizer-skill/HEAD/README.md

## Documentation

- https://auriti-labs.github.io/geo-optimizer-skill/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-ai-search-citation-readiness-with-geo-optimizer/)
