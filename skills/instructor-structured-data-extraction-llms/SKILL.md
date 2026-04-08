---
title: Instructor Structured Data Extraction from LLMs
description: 'Instructor is an open-source library designed to solve one of the most
  common problems in LLM application development: getting reliable, structured data
  out of language model responses. Available on PyPI as instructor and on npm as @instructor-ai/instructor
  , the project has over 10,000 GitHub stars and is maintained by Jason Liu through
  the 567-labs organization. The core idea is simple but powerful. Instead of parsing
  raw text responses and hoping the LLM follows your format instructions, Instructor
  patches the client libraries of major LLM providers so they return validated data
  objects directly. In Python, you define a Pydantic model describing the schema you
  want, and Instructor handles the tool-calling, JSON parsing, validation, and retry
  logic automatically. If the LLM returns malformed data, Instructor feeds the validation
  errors back to the model and retries until it gets a conforming response. Instructor
  supports over 15 LLM providers out of the box: OpenAI, Anthropic, Google Gemini,
  Mistral, Cohere, Ollama, DeepSeek, Groq, Together AI, vLLM, llama-cpp-python, and
  more. It works with both hosted APIs and local models. The TypeScript version uses
  Zod schemas instead of Pydantic, providing the same type-safe extraction workflow
  for JavaScript developers. Key features include partial streaming (get structured
  data as it arrives from the model), multimodal extraction (images and documents),
  batch processing, LLM-based validation where the model itself checks extracted data
  quality, and comprehensive logging and observability hooks. The library also supports
  iterable extraction for pulling multiple structured objects from a single response.
  An agent skill built on Instructor enables automated data extraction pipelines,
  form parsing, document intelligence workflows, and any task where unstructured text
  needs to become typed, validated data. The skill can define extraction schemas,
  configure provider-specific settings, handle retries, and integrate with downstream
  data processing. Instructor is MIT-licensed and actively maintained with frequent
  releases.'
verification: security_reviewed
source: https://github.com/567-labs/instructor
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: 567-labs/instructor
  github_stars: 12666
---

# Instructor Structured Data Extraction from LLMs

Instructor is an open-source library designed to solve one of the most common problems in LLM application development: getting reliable, structured data out of language model responses. Available on PyPI as instructor and on npm as @instructor-ai/instructor , the project has over 10,000 GitHub stars and is maintained by Jason Liu through the 567-labs organization. The core idea is simple but powerful. Instead of parsing raw text responses and hoping the LLM follows your format instructions, Instructor patches the client libraries of major LLM providers so they return validated data objects directly. In Python, you define a Pydantic model describing the schema you want, and Instructor handles the tool-calling, JSON parsing, validation, and retry logic automatically. If the LLM returns malformed data, Instructor feeds the validation errors back to the model and retries until it gets a conforming response. Instructor supports over 15 LLM providers out of the box: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, Ollama, DeepSeek, Groq, Together AI, vLLM, llama-cpp-python, and more. It works with both hosted APIs and local models. The TypeScript version uses Zod schemas instead of Pydantic, providing the same type-safe extraction workflow for JavaScript developers. Key features include partial streaming (get structured data as it arrives from the model), multimodal extraction (images and documents), batch processing, LLM-based validation where the model itself checks extracted data quality, and comprehensive logging and observability hooks. The library also supports iterable extraction for pulling multiple structured objects from a single response. An agent skill built on Instructor enables automated data extraction pipelines, form parsing, document intelligence workflows, and any task where unstructured text needs to become typed, validated data. The skill can define extraction schemas, configure provider-specific settings, handle retries, and integrate with downstream data processing. Instructor is MIT-licensed and actively maintained with frequent releases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/instructor-structured-data-extraction-llms/)
