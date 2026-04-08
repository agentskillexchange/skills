---
title: Hacker News Deep Thread Analyzer
description: 'The Hacker News Deep Thread Analyzer skill provides rich analysis of
  Hacker News discussion threads using the official Algolia HN API and Firebase real-time
  API for comprehensive data retrieval. Given a story URL or HN item ID, it fetches
  the complete comment tree including deleted and dead comments (when accessible),
  reconstructing the full conversation topology. Sentiment analysis via TextBlob and
  VADER classifiers identifies emotional tone shifts throughout the thread, detecting
  where discussions become heated, where consensus emerges, and where productive technical
  debate occurs. Expertise signals are extracted by analyzing commenter history —
  accounts with high karma, longtime membership, and domain-relevant past comments
  are weighted higher in summary generation. The structured output maps key arguments
  and counterarguments into a debate tree, identifying the strongest points on each
  side of contentious topics. Link extraction and classification categorizes referenced
  URLs by type (documentation, blog posts, academic papers, code repositories), creating
  a curated resource list from the collective intelligence of the thread. The tool
  generates executive summaries at configurable detail levels: one-paragraph TL;DR,
  bullet-point key takeaways, or full argument mapping with attributed quotes. Batch
  mode processes multiple related threads to identify recurring themes across discussions.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/hacker-news-deep-thread-analyzer/
category:
- Research &amp; Scraping
framework:
- Custom Agents
---

# Hacker News Deep Thread Analyzer

The Hacker News Deep Thread Analyzer skill provides rich analysis of Hacker News discussion threads using the official Algolia HN API and Firebase real-time API for comprehensive data retrieval. Given a story URL or HN item ID, it fetches the complete comment tree including deleted and dead comments (when accessible), reconstructing the full conversation topology. Sentiment analysis via TextBlob and VADER classifiers identifies emotional tone shifts throughout the thread, detecting where discussions become heated, where consensus emerges, and where productive technical debate occurs. Expertise signals are extracted by analyzing commenter history — accounts with high karma, longtime membership, and domain-relevant past comments are weighted higher in summary generation. The structured output maps key arguments and counterarguments into a debate tree, identifying the strongest points on each side of contentious topics. Link extraction and classification categorizes referenced URLs by type (documentation, blog posts, academic papers, code repositories), creating a curated resource list from the collective intelligence of the thread. The tool generates executive summaries at configurable detail levels: one-paragraph TL;DR, bullet-point key takeaways, or full argument mapping with attributed quotes. Batch mode processes multiple related threads to identify recurring themes across discussions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hacker-news-deep-thread-analyzer/)
