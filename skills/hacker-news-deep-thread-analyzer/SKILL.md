---
name: "Hacker News Deep Thread Analyzer"
description: "Scrapes and analyzes Hacker News threads using the official HN Firebase API and BeautifulSoup. Extracts sentiment trends, expertise signals, and generates structured summaries with key arguments mapped."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/hacker-news-deep-thread-analyzer/"
tool_ecosystem:
  tool: "firebase"
  github_stars: 1726
  npm_weekly_downloads: 4837581
  github_repo: "firebase/firebase-admin-node"
  license: "Apache-2.0"
  maintained: true
---

# Hacker News Deep Thread Analyzer

Scrapes and analyzes Hacker News threads using the official HN Firebase API and BeautifulSoup. Extracts sentiment trends, expertise signals, and generates structured summaries with key arguments mapped.

## Overview

The Hacker News Deep Thread Analyzer skill provides rich analysis of Hacker News discussion threads using the official Algolia HN API and Firebase real-time API for comprehensive data retrieval. Given a story URL or HN item ID, it fetches the complete comment tree including deleted and dead comments (when accessible), reconstructing the full conversation topology. Sentiment analysis via TextBlob and VADER classifiers identifies emotional tone shifts throughout the thread, detecting where discussions become heated, where consensus emerges, and where productive technical debate occurs. Expertise signals are extracted by analyzing commenter history — accounts with high karma, longtime membership, and domain-relevant past comments are weighted higher in summary generation. The structured output maps key arguments and counterarguments into a debate tree, identifying the strongest points on each side of contentious topics. Link extraction and classification categorizes referenced URLs by type (documentation, blog posts, academic papers, code repositories), creating a curated resource list from the collective intelligence of the thread. The tool generates executive summaries at configurable detail levels: one-paragraph TL;DR, bullet-point key takeaways, or full argument mapping with attributed quotes. Batch mode processes multiple related threads to identify recurring themes across discussions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hacker-news-deep-thread-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hacker-news-deep-thread-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hacker-news-deep-thread-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hacker-news-deep-thread-analyzer -a codex
```

### OpenClaw

```bash
clawhub install hacker-news-deep-thread-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hacker-news-deep-thread-analyzer/
