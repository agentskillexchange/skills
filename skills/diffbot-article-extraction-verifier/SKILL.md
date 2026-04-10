---
title: "Diffbot Article Extraction Verifier"
description: "Validates article extraction quality using the Diffbot Article API and Analyze API, checking fields like `title`, `author`, `tags`, and `text`. Useful for verifying whether an extraction pipeline is capturing real editorial structure instead of noisy page chrome."
slug: "diffbot-article-extraction-verifier"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://www.diffbot.com/dev/docs/"
---

# Diffbot Article Extraction Verifier

Validates article extraction quality using the Diffbot Article API and Analyze API, checking fields like `title`, `author`, `tags`, and `text`. Useful for verifying whether an extraction pipeline is capturing real editorial structure instead of noisy page chrome.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install diffbot-article-extraction-verifier
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Diffbot Article Extraction Verifier is for workflows that depend on machine-readable article data and need confidence that extraction quality is actually good. The skill uses the Diffbot Article API and Analyze API to inspect fields such as title, author, date, text, tags, and page type classification. Rather than assuming a response is correct because the request succeeded, it evaluates whether the extracted content looks like a real article or a thin mixture of headers, nav labels, and unrelated sidebar text.
This matters when teams are building research datasets, editorial monitoring systems, or intelligence pipelines that rely on article metadata for clustering and summarization. The skill can compare extracted structure across multiple URLs, flag missing or suspicious fields, and identify recurring site templates that need different handling. That makes it easier to distinguish genuine extraction failures from odd source formatting.
Use this skill to quality-check Diffbot output, verify article parsing at scale, and keep downstream analysis grounded in clean document structure rather than optimistic API assumptions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-article-extraction-verifier/)
