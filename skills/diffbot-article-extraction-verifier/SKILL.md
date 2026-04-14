---
title: "Diffbot Article Extraction Verifier"
description: "Validates article extraction quality using the Diffbot Article API and Analyze API, checking fields like `title`, `author`, `tags`, and `text`. Useful for verifying whether an extraction pipeline is capturing real editorial structure instead of noisy page chrome."
verification: security_reviewed
source: "https://www.diffbot.com/dev/docs/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
---

# Diffbot Article Extraction Verifier

Diffbot Article Extraction Verifier is for workflows that depend on machine-readable article data and need confidence that extraction quality is actually good. The skill uses the Diffbot Article API and Analyze API to inspect fields such as title, author, date, text, tags, and page type classification. Rather than assuming a response is correct because the request succeeded, it evaluates whether the extracted content looks like a real article or a thin mixture of headers, nav labels, and unrelated sidebar text.

This matters when teams are building research datasets, editorial monitoring systems, or intelligence pipelines that rely on article metadata for clustering and summarization. The skill can compare extracted structure across multiple URLs, flag missing or suspicious fields, and identify recurring site templates that need different handling. That makes it easier to distinguish genuine extraction failures from odd source formatting.

Use this skill to quality-check Diffbot output, verify article parsing at scale, and keep downstream analysis grounded in clean document structure rather than optimistic API assumptions.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-article-extraction-verifier/)
