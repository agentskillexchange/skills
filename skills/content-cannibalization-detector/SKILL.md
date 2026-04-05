---
name: "Content Cannibalization Detector"
description: "Identifies keyword cannibalization across site pages by analyzing Google Search Console Performance API data, extracting query-page pairings, and detecting overlap using TF-IDF cosine similarity scoring. Generates merge recommendations and 301 redirect maps via Screaming Frog exports."
category: "Content Writing &amp; SEO"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/content-cannibalization-detector/"
---
# Content Cannibalization Detector

Identifies keyword cannibalization across site pages by analyzing Google Search Console Performance API data, extracting query-page pairings, and detecting overlap using TF-IDF cosine similarity scoring. Generates merge recommendations and 301 redirect maps via Screaming Frog exports.

Content Cannibalization Detector finds pages competing for the same search queries by cross-referencing Google Search Console Performance API data with on-page content analysis. It pulls query-level impressions and clicks per URL through the searchAnalytics.query method, grouping results by query to identify URLs sharing keyword targeting.

The detection algorithm computes TF-IDF vectors for page content and calculates cosine similarity between pages ranking for overlapping queries. Pages with similarity scores above 0.7 that share more than three ranking queries are flagged as cannibalization candidates. The tool also checks title tags, H1 headers, and meta descriptions for direct keyword overlap using fuzzy string matching via python-Levenshtein.

Output includes a prioritized list of cannibalization pairs with recommended actions: merge content into the stronger page, differentiate keyword targeting, or implement 301 redirects. Redirect maps are generated in CSV format compatible with Screaming Frog’s redirect chain validation. The tool integrates with Screaming Frog crawl exports to correlate internal link equity, showing which cannibalized page receives more internal authority signals to inform the consolidation decision.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill content-cannibalization-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill content-cannibalization-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill content-cannibalization-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill content-cannibalization-detector -a codex
```

### OpenClaw

```bash
clawhub install content-cannibalization-detector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-cannibalization-detector/)
