---
title: "Instructor Structured Data Extraction from LLMs"
description: "Instructor is a multi-language library for extracting structured, validated data from LLM outputs. It patches LLM client libraries to return Pydantic models (Python) or Zod schemas (TypeScript) instead of raw text, supporting 15+ providers including OpenAI, Anthropic, and Google."
slug: "instructor-structured-data-extraction-llms"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/567-labs/instructor"
tool_ecosystem:
  github_repo: "567-labs/instructor"
  github_stars: 12666
listed: true
---

# Instructor Structured Data Extraction from LLMs

Instructor is a multi-language library for extracting structured, validated data from LLM outputs. It patches LLM client libraries to return Pydantic models (Python) or Zod schemas (TypeScript) instead of raw text, supporting 15+ providers including OpenAI, Anthropic, and Google.

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
clawhub install instructor-structured-data-extraction-llms
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Instructor is an open-source library designed to solve one of the most common problems in LLM application development: getting reliable, structured data out of language model responses. Available on PyPI as instructor and on npm as @instructor-ai/instructor, the project has over 10,000 GitHub stars and is maintained by Jason Liu through the 567-labs organization.
The core idea is simple but powerful. Instead of parsing raw text responses and hoping the LLM follows your format instructions, Instructor patches the client libraries of major LLM providers so they return validated data objects directly. In Python, you define a Pydantic model describing the schema you want, and Instructor handles the tool-calling, JSON parsing, validation, and retry logic automatically. If the LLM returns malformed data, Instructor feeds the validation errors back to the model and retries until it gets a conforming response.
Instructor supports over 15 LLM providers out of the box: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, Ollama, DeepSeek, Groq, Together AI, vLLM, llama-cpp-python, and more. It works with both hosted APIs and local models. The TypeScript version uses Zod schemas instead of Pydantic, providing the same type-safe extraction workflow for JavaScript developers.
Key features include partial streaming (get structured data as it arrives from the model), multimodal extraction (images and documents), batch processing, LLM-based validation where the model itself checks extracted data quality, and comprehensive logging and observability hooks. The library also supports iterable extraction for pulling multiple structured objects from a single response.
An agent skill built on Instructor enables automated data extraction pipelines, form parsing, document intelligence workflows, and any task where unstructured text needs to become typed, validated data. The skill can define extraction schemas, configure provider-specific settings, handle retries, and integrate with downstream data processing. Instructor is MIT-licensed and actively maintained with frequent releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/instructor-structured-data-extraction-llms/)
