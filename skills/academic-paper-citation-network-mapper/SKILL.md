---
title: "Academic Paper Citation Network Mapper"
description: "The Academic Paper Citation Network Mapper skill constructs and visualizes citation networks for academic research using the Semantic Scholar API for citation data and CrossRef for DOI resolution and metadata enrichment. Given a seed paper (by DOI, arXiv ID, or title search), it recursively fetches citing and cited papers to a configurable depth, building a comprehensive NetworkX directed graph of the citation landscape. Each node contains rich metadata: title, authors, year, venue, abstract, field of study classifications, and citation counts. The influence analysis engine computes PageRank, betweenness centrality, and hub/authority scores to identify seminal papers that shaped a field, bridge papers connecting disparate research areas, and emerging influential works with high recent citation velocity. Research lineage tracking follows citation chains to reveal how ideas evolved, forked, and merged across decades and disciplines. The visualization layer produces interactive HTML graphs using pyvis with configurable layouts (force-directed, chronological, cluster-by-field), color coding by research area or publication decade, and node sizing by influence score. Export formats include BibTeX for the entire network, CSV of ranked papers by influence, and Obsidian-compatible markdown with bidirectional links for building personal research knowledge bases. Rate limiting and caching ensure responsible API usage across large network explorations."
source: "https://agentskillexchange.com/skills/academic-paper-citation-network-mapper/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# Academic Paper Citation Network Mapper

The Academic Paper Citation Network Mapper skill constructs and visualizes citation networks for academic research using the Semantic Scholar API for citation data and CrossRef for DOI resolution and metadata enrichment. Given a seed paper (by DOI, arXiv ID, or title search), it recursively fetches citing and cited papers to a configurable depth, building a comprehensive NetworkX directed graph of the citation landscape. Each node contains rich metadata: title, authors, year, venue, abstract, field of study classifications, and citation counts. The influence analysis engine computes PageRank, betweenness centrality, and hub/authority scores to identify seminal papers that shaped a field, bridge papers connecting disparate research areas, and emerging influential works with high recent citation velocity. Research lineage tracking follows citation chains to reveal how ideas evolved, forked, and merged across decades and disciplines. The visualization layer produces interactive HTML graphs using pyvis with configurable layouts (force-directed, chronological, cluster-by-field), color coding by research area or publication decade, and node sizing by influence score. Export formats include BibTeX for the entire network, CSV of ranked papers by influence, and Obsidian-compatible markdown with bidirectional links for building personal research knowledge bases. Rate limiting and caching ensure responsible API usage across large network explorations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/academic-paper-citation-network-mapper/)
