---
title: Jina Reader URL-to-Markdown Converter and Web Search API
description: 'Jina Reader is an open-source tool and free hosted API by Jina AI that
  converts any web page into clean, LLM-friendly markdown content. By simply prepending
  https://r.jina.ai/ to any URL, you get a markdown version of that page optimized
  for language model consumption. The project also includes a search endpoint at https://s.jina.ai/
  that performs web searches and returns results in markdown format. Read Mode — URL
  to Markdown The primary use case is converting web pages to structured markdown
  for LLM input. Send any URL to https://r.jina.ai/https://example.com and get back
  clean text with images captioned, navigation stripped, and content extracted. This
  works with standard HTML pages, PDF documents, and dynamically rendered JavaScript
  sites. The API handles cookie consent dialogs, paywalls (where possible), and complex
  page layouts automatically. Search Mode — Web Search for Agents The search endpoint
  at https://s.jina.ai/your+query performs web searches and returns the top 5 results,
  each converted to LLM-friendly markdown. This provides grounding data for agents
  and RAG systems that need current web knowledge. You can restrict results to specific
  domains using the site= parameter for in-site search. Request Headers for Fine-grained
  Control Reader supports request headers for advanced configuration: forward cookies
  with x-with-cookie , use HTTP proxies with x-with-proxy , enable image captioning
  with x-with-generated-alt: true , set target selectors with x-target-selector ,
  and control output format. These headers give agents precise control over content
  extraction behavior. Image Understanding Reader captions images found on pages and
  includes them as alt text in the markdown output. This enables downstream LLMs to
  reason about visual content without needing vision capabilities. Image captioning
  is opt-in via the x-with-generated-alt header to keep default latency low. Self-hosting
  and Architecture The Reader source code is available on GitHub under the Apache-2.0
  license, with over 10,000 stars. While the hosted API at r.jina.ai is free and rate-limited
  for production use, you can self-host the entire stack for unlimited usage. The
  backend uses a headless browser farm for JavaScript rendering and a content extraction
  pipeline. Agent Integration Jina Reader is purpose-built for AI agent and RAG workflows.
  It eliminates the need for agents to run their own browser automation for content
  extraction. Simply call the Reader API as a preprocessing step before feeding web
  content to an LLM. The search endpoint enables agents to access current web knowledge
  for fact-checking, research, and grounding without managing search API keys.'
verification: security_reviewed
source: https://github.com/jina-ai/reader
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
---

# Jina Reader URL-to-Markdown Converter and Web Search API

Jina Reader is an open-source tool and free hosted API by Jina AI that converts any web page into clean, LLM-friendly markdown content. By simply prepending https://r.jina.ai/ to any URL, you get a markdown version of that page optimized for language model consumption. The project also includes a search endpoint at https://s.jina.ai/ that performs web searches and returns results in markdown format. Read Mode — URL to Markdown The primary use case is converting web pages to structured markdown for LLM input. Send any URL to https://r.jina.ai/https://example.com and get back clean text with images captioned, navigation stripped, and content extracted. This works with standard HTML pages, PDF documents, and dynamically rendered JavaScript sites. The API handles cookie consent dialogs, paywalls (where possible), and complex page layouts automatically. Search Mode — Web Search for Agents The search endpoint at https://s.jina.ai/your+query performs web searches and returns the top 5 results, each converted to LLM-friendly markdown. This provides grounding data for agents and RAG systems that need current web knowledge. You can restrict results to specific domains using the site= parameter for in-site search. Request Headers for Fine-grained Control Reader supports request headers for advanced configuration: forward cookies with x-with-cookie , use HTTP proxies with x-with-proxy , enable image captioning with x-with-generated-alt: true , set target selectors with x-target-selector , and control output format. These headers give agents precise control over content extraction behavior. Image Understanding Reader captions images found on pages and includes them as alt text in the markdown output. This enables downstream LLMs to reason about visual content without needing vision capabilities. Image captioning is opt-in via the x-with-generated-alt header to keep default latency low. Self-hosting and Architecture The Reader source code is available on GitHub under the Apache-2.0 license, with over 10,000 stars. While the hosted API at r.jina.ai is free and rate-limited for production use, you can self-host the entire stack for unlimited usage. The backend uses a headless browser farm for JavaScript rendering and a content extraction pipeline. Agent Integration Jina Reader is purpose-built for AI agent and RAG workflows. It eliminates the need for agents to run their own browser automation for content extraction. Simply call the Reader API as a preprocessing step before feeding web content to an LLM. The search endpoint enables agents to access current web knowledge for fact-checking, research, and grounding without managing search API keys.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-url-to-markdown-web-search/)
