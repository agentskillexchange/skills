---
title: Tarsier Vision Utilities for Web Interaction Agents
description: 'Overview Tarsier is a perception system for web agents developed by
  Reworkd after iterating across tens of thousands of real web tasks. It solves three
  core problems that arise when using LLMs to automate web interactions: how to feed
  a webpage to an LLM, how to map LLM responses back to web elements, and how to inform
  text-only LLMs about visual page structure. How It Works Tarsier visually tags interactable
  elements on a page using brackets with an ID, such as [23] . This creates a mapping
  between page elements and numeric IDs that an LLM can reference to take actions
  like CLICK [23] or TYPE [15] hello . Different element types get different tag markers:
  [#ID] for text-insertable fields, [@ID] for hyperlinks, [$ID] for other interactable
  elements like buttons, and [ID] for plain text elements. OCR Text Representation
  Beyond visual tagging, Tarsier includes an OCR algorithm that converts page screenshots
  into whitespace-structured strings that resemble ASCII art. This structured text
  representation allows even text-only LLMs without vision capabilities to understand
  page layout and spatial relationships. On internal benchmarks, unimodal GPT-4 with
  Tarsier text representations outperformed GPT-4V with Tarsier screenshots by 10-20%.
  Integration Tarsier integrates with Playwright and Selenium for browser automation,
  and works with LangChain and LlamaIndex for building autonomous web agents. It supports
  Google Vision and Microsoft Azure as OCR backends. Install via pip install tarsier
  and use the async API to tag pages and extract text representations. Agent Skill
  Integration For AI coding agents, Tarsier enables building browser automation skills
  that can perceive and interact with web pages through structured element references
  rather than fragile CSS selectors or XPaths. The tagged element mapping provides
  a stable interface for LLM-driven web interactions across different page layouts.'
verification: security_reviewed
source: https://github.com/reworkd/tarsier
category:
- Browser Automation
framework:
- Custom Agents
---

# Tarsier Vision Utilities for Web Interaction Agents

Overview Tarsier is a perception system for web agents developed by Reworkd after iterating across tens of thousands of real web tasks. It solves three core problems that arise when using LLMs to automate web interactions: how to feed a webpage to an LLM, how to map LLM responses back to web elements, and how to inform text-only LLMs about visual page structure. How It Works Tarsier visually tags interactable elements on a page using brackets with an ID, such as [23] . This creates a mapping between page elements and numeric IDs that an LLM can reference to take actions like CLICK [23] or TYPE [15] hello . Different element types get different tag markers: [#ID] for text-insertable fields, [@ID] for hyperlinks, [$ID] for other interactable elements like buttons, and [ID] for plain text elements. OCR Text Representation Beyond visual tagging, Tarsier includes an OCR algorithm that converts page screenshots into whitespace-structured strings that resemble ASCII art. This structured text representation allows even text-only LLMs without vision capabilities to understand page layout and spatial relationships. On internal benchmarks, unimodal GPT-4 with Tarsier text representations outperformed GPT-4V with Tarsier screenshots by 10-20%. Integration Tarsier integrates with Playwright and Selenium for browser automation, and works with LangChain and LlamaIndex for building autonomous web agents. It supports Google Vision and Microsoft Azure as OCR backends. Install via pip install tarsier and use the async API to tag pages and extract text representations. Agent Skill Integration For AI coding agents, Tarsier enables building browser automation skills that can perceive and interact with web pages through structured element references rather than fragile CSS selectors or XPaths. The tagged element mapping provides a stable interface for LLM-driven web interactions across different page layouts.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tarsier-vision-utilities-web-interaction-agents/)
