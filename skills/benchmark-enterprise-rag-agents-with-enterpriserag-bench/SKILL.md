---
name: "Benchmark enterprise RAG agents with EnterpriseRAG-Bench"
slug: "benchmark-enterprise-rag-agents-with-enterpriserag-bench"
description: "Use EnterpriseRAG-Bench to evaluate an enterprise RAG or knowledge-agent system against a realistic synthetic company corpus with answer, recall, and comparative scoring."
github_stars: 562
verification: "security_reviewed"
source: "https://github.com/onyx-dot-app/EnterpriseRAG-Bench"
author: "Onyx"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "onyx-dot-app/EnterpriseRAG-Bench"
  github_stars: 562
---

# Benchmark enterprise RAG agents with EnterpriseRAG-Bench

Use EnterpriseRAG-Bench to evaluate an enterprise RAG or knowledge-agent system against a realistic synthetic company corpus with answer, recall, and comparative scoring.

## Prerequisites

Python 3.10+, EnterpriseRAG-Bench dataset and questions, a RAG or knowledge-agent system under test, OpenAI or Anthropic compatible LLM credentials for evaluation

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/onyx-dot-app/EnterpriseRAG-Bench, install Python dependencies with pip install -r requirements.txt, set LLM_PROVIDER and LLM_API_KEY, download the benchmark dataset from the latest GitHub release or Hugging Face, write system outputs to answer_evaluation/answers.jsonl, then run python -m src.scripts.answer_evaluation.metrics_based_eval --answers-file answer_evaluation/answers.jsonl.

- Source: https://github.com/onyx-dot-app/EnterpriseRAG-Bench

## Documentation

- https://github.com/onyx-dot-app/EnterpriseRAG-Bench/blob/main/quickstart.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-enterprise-rag-agents-with-enterpriserag-bench/)
