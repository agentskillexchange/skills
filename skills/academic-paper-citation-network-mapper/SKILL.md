---
name: "Academic Paper Citation Network Mapper"
description: "Builds citation networks from Semantic Scholar API and CrossRef DOI metadata. Visualizes paper influence graphs using NetworkX, identifies seminal works, and tracks research lineage across fields."
category: "Research & Scraping"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/academic-paper-citation-network-mapper/"
---

# Academic Paper Citation Network Mapper

Builds citation networks from Semantic Scholar API and CrossRef DOI metadata. Visualizes paper influence graphs using NetworkX, identifies seminal works, and tracks research lineage across fields.

## Overview

The Academic Paper Citation Network Mapper skill constructs and visualizes citation networks for academic research using the Semantic Scholar API for citation data and CrossRef for DOI resolution and metadata enrichment. Given a seed paper (by DOI, arXiv ID, or title search), it recursively fetches citing and cited papers to a configurable depth, building a comprehensive NetworkX directed graph of the citation landscape. Each node contains rich metadata: title, authors, year, venue, abstract, field of study classifications, and citation counts. The influence analysis engine computes PageRank, betweenness centrality, and hub/authority scores to identify seminal papers that shaped a field, bridge papers connecting disparate research areas, and emerging influential works with high recent citation velocity. Research lineage tracking follows citation chains to reveal how ideas evolved, forked, and merged across decades and disciplines. The visualization layer produces interactive HTML graphs using pyvis with configurable layouts (force-directed, chronological, cluster-by-field), color coding by research area or publication decade, and node sizing by influence score. Export formats include BibTeX for the entire network, CSV of ranked papers by influence, and Obsidian-compatible markdown with bidirectional links for building personal research knowledge bases. Rate limiting and caching ensure responsible API usage across large network explorations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill academic-paper-citation-network-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill academic-paper-citation-network-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill academic-paper-citation-network-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill academic-paper-citation-network-mapper -a codex
```

### OpenClaw

```bash
clawhub install academic-paper-citation-network-mapper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/academic-paper-citation-network-mapper/
