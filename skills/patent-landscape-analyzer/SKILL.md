---
name: "Patent Landscape Analyzer"
description: "Searches the USPTO PatentsView API and European Patent Office OPS (Open Patent Services) API for patent grants, applications, and family relationships. Generates technology landscape maps with IPC classification clustering."
category: "Research & Scraping"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/patent-landscape-analyzer/"
---

# Patent Landscape Analyzer

Searches the USPTO PatentsView API and European Patent Office OPS (Open Patent Services) API for patent grants, applications, and family relationships. Generates technology landscape maps with IPC classification clustering.

## Overview

The Patent Landscape Analyzer provides comprehensive intellectual property research capabilities through integration with major patent office APIs. The USPTO PatentsView API enables full-text search across US patent grants and applications with filters for assignee, inventor, CPC classification, and date ranges. European Patent Office Open Patent Services provides worldwide patent family data, connecting related filings across jurisdictions to map global IP strategies. IPC and CPC classification analysis clusters patents into technology domains, revealing innovation concentration areas and white space opportunities where patent activity is sparse. Citation network analysis identifies foundational patents and tracks technology evolution through forward citation chains. The analyzer extracts structured claim text and identifies key claim limitations for freedom-to-operate assessments. Assignee portfolio analysis compares patent holdings across competitors within specific technology domains, tracking filing velocity and geographic coverage strategies. Patent family expansion timelines show how inventions propagate across international jurisdictions through PCT, Paris Convention, and direct filing routes. Automated landscape reports combine quantitative filing statistics with technology categorization for strategic IP planning and due diligence workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-analyzer -a codex
```

### OpenClaw

```bash
clawhub install patent-landscape-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/patent-landscape-analyzer/
