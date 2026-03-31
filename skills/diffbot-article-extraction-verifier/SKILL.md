---
name: "Diffbot Article Extraction Verifier"
description: "Validates article extraction quality using the Diffbot Article API and Analyze API, checking fields like `title`, `author`, `tags`, and `text`. Useful for verifying whether an extraction pipeline is capturing real editorial structure instead of noisy page chrome."
category: "Research &amp; Scraping"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/diffbot-article-extraction-verifier/"
---
# Diffbot Article Extraction Verifier

Validates article extraction quality using the Diffbot Article API and Analyze API, checking fields like `title`, `author`, `tags`, and `text`. Useful for verifying whether an extraction pipeline is capturing real editorial structure instead of noisy page chrome.

## Overview

Diffbot Article Extraction Verifier is for workflows that depend on machine-readable article data and need confidence that extraction quality is actually good. The skill uses the Diffbot Article API and Analyze API to inspect fields such as title, author, date, text, tags, and page type classification. Rather than assuming a response is correct because the request succeeded, it evaluates whether the extracted content looks like a real article or a thin mixture of headers, nav labels, and unrelated sidebar text.

This matters when teams are building research datasets, editorial monitoring systems, or intelligence pipelines that rely on article metadata for clustering and summarization. The skill can compare extracted structure across multiple URLs, flag missing or suspicious fields, and identify recurring site templates that need different handling. That makes it easier to distinguish genuine extraction failures from odd source formatting.

Use this skill to quality-check Diffbot output, verify article parsing at scale, and keep downstream analysis grounded in clean document structure rather than optimistic API assumptions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-extraction-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-extraction-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-extraction-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-extraction-verifier -a codex
```

### OpenClaw

```bash
clawhub install diffbot-article-extraction-verifier
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-article-extraction-verifier/)
