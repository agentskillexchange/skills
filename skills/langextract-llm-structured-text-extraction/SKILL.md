---
name: "LangExtract LLM-Powered Structured Text Extraction"
description: "LangExtract by Google is a Python library for extracting structured information from unstructured text using LLMs with precise source grounding. With 35,000+ GitHub stars, it handles everything from clinical notes to literary analysis, producing verified extraction results with exact source text mappings and interactive visualizations."
category: "Data Extraction &amp; Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/google/langextract"
---
# LangExtract LLM-Powered Structured Text Extraction

LangExtract by Google is a Python library for extracting structured information from unstructured text using LLMs with precise source grounding. With 35,000+ GitHub stars, it handles everything from clinical notes to literary analysis, producing verified extraction results with exact source text mappings and interactive visualizations.

## Overview

LangExtract is a Python library developed by Google for extracting structured information from unstructured text documents using large language models. It processes materials such as clinical notes, reports, legal documents, or literary texts, identifying and organizing key details while ensuring every extracted fact traces back to its exact location in the source text.

How It Works
LangExtract operates on a few-shot learning approach: you define a prompt describing what to extract and provide one or more high-quality examples showing the expected output format. The library then applies the LLM to process entire documents, extracting entities, relationships, attributes, and classifications according to your specification. Each extraction includes the exact source text span, enabling visual highlighting and verification. The library uses an optimized strategy of text chunking, parallel processing, and multiple passes to handle long documents and overcome the needle-in-a-haystack problem that plagues standard LLM extraction approaches.

Key Capabilities
Precise Source Grounding maps every extraction to its exact position in the source text, making results verifiable and auditable. Reliable Structured Outputs enforce a consistent output schema based on few-shot examples, leveraging controlled generation in supported models like Gemini to guarantee robust results. The Interactive Visualization feature generates self-contained HTML files where users can review thousands of extracted entities highlighted in their original document context. The library supports cloud-based LLMs (Google Gemini family), OpenAI models, and local open-source models via the built-in Ollama interface.

Domain Adaptability
LangExtract adapts to any domain through prompt engineering and example definition, without requiring model fine-tuning. The repository includes ready-to-use examples for medication extraction from clinical notes, character and emotion extraction from literary texts (including a full Romeo and Juliet extraction pipeline), and RadExtract for structuring radiology reports. The library can leverage LLM world knowledge for inference tasks where appropriate, with accuracy dependent on the selected model, task complexity, and prompt clarity.

Output and Integration
Results are returned as structured Python objects containing the extraction class, extracted text span, source position, and arbitrary attributes. The library produces JSON-serializable output suitable for downstream processing, database ingestion, or API responses. The PyPI package installs via pip and requires only a few lines of code to define an extraction pipeline. It is published on Zenodo with a citable DOI for academic use.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill langextract-llm-structured-text-extraction
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill langextract-llm-structured-text-extraction -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill langextract-llm-structured-text-extraction -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill langextract-llm-structured-text-extraction -a codex
```

### OpenClaw

```bash
clawhub install langextract-llm-structured-text-extraction
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langextract-llm-structured-text-extraction/)
