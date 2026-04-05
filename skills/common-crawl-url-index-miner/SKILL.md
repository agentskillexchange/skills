---
name: "Common Crawl URL Index Miner"
description: "Queries the Common Crawl Index API and CC-MAIN collections to surface historical URL coverage, MIME types, and crawl snapshots at scale. Handy for research workflows that need broad web recall without building a full crawler from scratch."
category: "Research &amp; Scraping"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/commoncrawl/cc-index-table"
tool_ecosystem:
  github_repo: "commoncrawl/cc-index-table"
  github_stars: 127
---
# Common Crawl URL Index Miner

Queries the Common Crawl Index API and CC-MAIN collections to surface historical URL coverage, MIME types, and crawl snapshots at scale. Handy for research workflows that need broad web recall without building a full crawler from scratch.

Common Crawl URL Index Miner is built for large-scale web research where the goal is not just to scrape one page, but to discover what the public web has looked like across repeated crawl snapshots. The skill works with the Common Crawl Index API, CC-MAIN datasets, and URL-level metadata such as crawl date, status, digest, and MIME type to identify where specific domains, paths, or content patterns appear in archived crawl history. That gives researchers fast access to historical coverage without launching their own distributed spidering job.

The skill is especially useful for domain discovery, historical footprint analysis, and broad competitor research. It can isolate URLs by host, prefix, or file type, then help decide which records are worth sending to a downstream extraction step. Because Common Crawl separates discovery from content retrieval, this workflow reduces wasted fetches and gives a more systematic starting point for web-scale investigations.

Use this skill when you need archive-backed URL intelligence, dataset-driven discovery, or a reliable way to mine old crawl snapshots before spending resources on deeper parsing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill common-crawl-url-index-miner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill common-crawl-url-index-miner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill common-crawl-url-index-miner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill common-crawl-url-index-miner -a codex
```

### OpenClaw

```bash
clawhub install common-crawl-url-index-miner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/common-crawl-url-index-miner/)
