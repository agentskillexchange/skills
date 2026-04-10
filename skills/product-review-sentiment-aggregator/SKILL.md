---
name: "Product Review Sentiment Aggregator"
description: "Collects and analyzes product reviews from Amazon Product API and Google Shopping via SerpAPI. Uses spaCy NER and aspect-based sentiment analysis to extract feature-level opinions and competitive comparisons."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/product-review-sentiment-aggregator/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
---

# Product Review Sentiment Aggregator

The Product Review Sentiment Aggregator skill provides comprehensive product review analysis by collecting reviews from multiple sources and applying advanced NLP techniques to extract actionable insights. Using the Amazon Product Advertising API for Amazon reviews and SerpAPI for Google Shopping review data, it aggregates reviews across marketplaces for the same product. The spaCy NLP pipeline performs named entity recognition to identify product features, competitor mentions, and use-case descriptions within review text. Aspect-based sentiment analysis goes beyond overall star ratings to determine sentiment for specific product attributes — battery life, build quality, ease of setup, customer support — providing a nuanced feature-level satisfaction breakdown. The competitive analysis module identifies reviews that mention competitor products, extracting comparative statements and organizing them into a competitive positioning matrix. Temporal analysis tracks sentiment trends over time, detecting quality changes after product updates or manufacturing shifts. The deception detection component flags potentially fake reviews using linguistic pattern analysis, reviewer profile signals, and statistical distribution anomalies in rating patterns. Output formats include executive summary dashboards with radar charts of feature sentiment, detailed aspect tables with representative quotes, trend graphs, and competitive comparison matrices. The tool supports monitoring mode with periodic re-analysis and alerting on significant sentiment shifts.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/product-review-sentiment-aggregator/)
