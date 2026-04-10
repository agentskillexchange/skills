---
name: "SerpAPI Research Pipeline"
description: "Builds structured research datasets by querying SerpAPI Google Search, Google Scholar, and Google News endpoints. Extracts entities via spaCy NER and stores results in SQLite with full-text search."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-research-pipeline/"
category:
  - "Research &amp; Scraping"
framework:
  - "Codex"
---

# SerpAPI Research Pipeline

The SerpAPI Research Pipeline automates multi-source research by orchestrating queries across SerpAPI Google Search, Google Scholar, and Google News JSON endpoints. For each research topic, it generates query variations using synonym expansion and boolean operators to maximize coverage. Search results are parsed and deduplicated using URL normalization and content fingerprinting. The pipeline extracts named entities from result snippets using spaCy NER models, identifying people, organizations, locations, and technical terms relevant to the research domain. All results are stored in a SQLite database with FTS5 full-text search indexes for rapid retrieval. The agent supports iterative deepening where initial results inform follow-up queries for comprehensive topic coverage. Citation graphs are built by cross-referencing Google Scholar results. Export formats include CSV, JSON, and formatted Markdown research briefs with source attribution and confidence scoring.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-research-pipeline/)
