---
name: "Learn and reuse route-specific extraction selectors with Crawlee Python"
slug: "learn-and-reuse-route-specific-extraction-selectors-with-crawlee-python"
description: "Learn CSS selectors once per page route, persist them across Crawlee Python runs, and extract validated records with controlled LLM fallback and usage checks."
verification: "security_reviewed"
source: "https://github.com/apify/crawlee-python/blob/v1.11.2/docs/03_concepts/08_pydantic_ai_crawler.mdx"
author: "Apify"
publisher_type: "organization"
category: "Research & Scraping"
framework: "Multi-Framework"
---

# Learn and reuse route-specific extraction selectors with Crawlee Python

Learn CSS selectors once per page route, persist them across Crawlee Python runs, and extract validated records with controlled LLM fallback and usage checks.

## Prerequisites

Python 3.10+; crawlee[pydantic-ai] 1.11.2; supported model provider credentials; persistent Crawlee storage

## Installation

Install or set up from the source-backed instructions:

Use Python 3.10+ in a project virtual environment. Install the verified release with python -m pip install 'crawlee[pydantic-ai]==1.11.2'. Configure a supported model provider credential through its environment variable, such as OPENAI_API_KEY. Start from the upstream v1.11.2 selector_extractor_example.py, set the authorized seed URLs, allowed URL patterns, request limit and Pydantic schema, and use an environment-backed model configuration instead of the example's literal key placeholder. Add the documented UsageLimits and cumulative usage checks to both extractor paths. Run the resulting project script with python extract_routes.py; retain its Crawlee storage between runs to reuse cached selectors. This HTTP-only workflow needs no browser installation, MCP server or Apify account.

- Source: https://github.com/apify/crawlee-python/blob/v1.11.2/docs/03_concepts/08_pydantic_ai_crawler.mdx

## Documentation

- https://crawlee.dev/python/docs/concepts/pydantic-ai-crawler

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/learn-and-reuse-route-specific-extraction-selectors-with-crawlee-python/)
