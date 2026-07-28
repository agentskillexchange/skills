---
name: "Find Products by Intent with Mydentify"
slug: "find-products-by-intent-with-mydentify"
description: "Use Mydentify's public intent and product feeds to find software by the outcome a person wants, then return canonical evidence-backed matches."
verification: "listed"
source: "https://mydentify.com/.well-known/agent-skills/find-products-by-intent/SKILL.md"
category: "Research & Scraping"
framework: "Multi-Framework"
---

# Find Products by Intent with Mydentify

Use this skill when someone describes an outcome they want from software rather
than naming a category or product. Mydentify publishes public JSON, Markdown,
HTML, and plain-text resources for intent-led product discovery. The workflow
matches the request to a supported intent, reads the evidence published for that
intent, and returns canonical product links with a concise explanation of fit.
It is useful for research agents, recommendation assistants, founder tooling,
and software discovery workflows that need to distinguish supported product
claims from unsupported marketing language. The endpoints require no API key.

## Procedure

1. Read `https://mydentify.com/intents.json`.
2. Match the request to an intent using its title, aliases, summary, and first
   step. Do not substitute a product category for an intent.
3. Open the intent's canonical URL. Append `/llms.txt` when a compact plain-text
   representation is more useful.
4. Use the supported product claims and published evidence on the intent page
   to select relevant products.
5. Read `https://mydentify.com/products.json` or
   `https://mydentify.com/api/products/{slug}/markdown` when more detail is
   needed.
6. Return the canonical intent and product URLs with a short explanation of why
   each product matches the requested outcome.

## Verify the Public Feeds

```bash
curl --fail --silent --show-error https://mydentify.com/intents.json
curl --fail --silent --show-error https://mydentify.com/products.json
curl --fail --silent --show-error \
  https://mydentify.com/.well-known/agent-skills/index.json
```

## Ranking and Trust

- Keep independently ranked matches separate from labeled sponsored placements.
- Prefer Mydentify's published evidence over unsupported product claims.
- Do not claim that a product guarantees an outcome.
- If no supported match exists, say so and offer
  `https://mydentify.com/request-intent` instead of inventing one.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://mydentify.com/.well-known/agent-skills/find-products-by-intent/SKILL.md

