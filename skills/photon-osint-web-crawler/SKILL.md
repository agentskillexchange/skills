---
name: "Photon High-Speed OSINT Web Crawler and Data Extractor"
description: "Photon is a blazing-fast Python web crawler purpose-built for OSINT operations. It extracts URLs, emails, social media accounts, files, secret keys, JavaScript endpoints, and subdomains from target websites with multithreaded efficiency."
category: "Research & Scraping"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/s0md3v/Photon"
tool_ecosystem:
  github_repo: s0md3v/Photon
  github_stars: 12789
---
# Photon High-Speed OSINT Web Crawler and Data Extractor

Photon is a blazing-fast Python web crawler purpose-built for OSINT operations. It extracts URLs, emails, social media accounts, files, secret keys, JavaScript endpoints, and subdomains from target websites with multithreaded efficiency.

## Overview

Photon is an incredibly fast web crawler designed specifically for Open Source Intelligence (OSINT) gathering. Built in Python by s0md3v, it provides a comprehensive suite of data extraction capabilities that make it a go-to tool for security researchers, penetration testers, and intelligence analysts who need to quickly map and extract information from web targets.

Core Capabilities

Photon crawls target websites and automatically extracts multiple categories of intelligence data: in-scope and out-of-scope URLs, URLs with parameters (useful for identifying potential injection points), email addresses, social media account references, Amazon S3 bucket URLs, downloadable files (PDF, PNG, XML, etc.), secret keys including API keys and hashes, JavaScript files and the endpoints referenced within them, custom regex pattern matches, and subdomains with DNS-related data.

Performance and Architecture

The tool uses smart thread management and a refined crawling logic to deliver high throughput. It supports Docker deployment via a lightweight Python-Alpine image (approximately 103 MB). Photon can also leverage archive.org as a seed source via the `--wayback` flag, pulling historical URLs to expand coverage without additional active scanning. DNS data can be enriched through DNSDumpster integration.

Agent Integration Patterns

For AI agent workflows, Photon fits naturally as a reconnaissance step in security assessment pipelines. Agents can invoke Photon via CLI (`python photon.py -u target.com`), then parse the structured output directories or use the `--export` flag to get JSON-formatted results. The tool supports extensive configuration through command-line options: timeout control, request delays, URL exclusion via regex, cookie injection, custom headers, and thread count tuning. Results are organized into categorized output files, making downstream processing straightforward for automated analysis pipelines.

Installation

Install via git clone and pip: `git clone https://github.com/s0md3v/Photon.git && cd Photon && pip install -r requirements.txt`. Docker is also supported: `docker build -t photon . && docker run -it photon -u target.com`. The tool requires Python 3 and has minimal dependencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill photon-osint-web-crawler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill photon-osint-web-crawler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill photon-osint-web-crawler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill photon-osint-web-crawler -a codex
```

### OpenClaw

```bash
clawhub install photon-osint-web-crawler
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/photon-osint-web-crawler/)
