---
name: "Evaluate agent and model workflows with EvalScope"
slug: "evaluate-agent-and-model-workflows-with-evalscope"
description: "Run repeatable EvalScope benchmark suites for LLM, VLM, RAG, and agent workflows, then inspect traces and reports before changing models or prompts."
github_stars: 2953
verification: "security_reviewed"
source: "https://github.com/modelscope/evalscope"
author: "ModelScope Community"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "modelscope/evalscope"
  github_stars: 2953
---

# Evaluate agent and model workflows with EvalScope

Run repeatable EvalScope benchmark suites for LLM, VLM, RAG, and agent workflows, then inspect traces and reports before changing models or prompts.

## Prerequisites

Python 3.10+, pip, evalscope package, model endpoint or local model backend, API credentials when evaluating hosted models, selected benchmark datasets

## Installation

Use the upstream install or setup path that matches your environment:
- pip install evalscope
- pip install 'evalscope[service]'

Requirements and caveats from upstream:
- <img src="https://img.shields.io/badge/python-%E2%89%A53.10-5be.svg">
- **🤖 Agent Evaluation Mode**: Drives benchmarks (e.g. GSM8K, AIME, SWE-bench Agentic) inside a controlled multi-turn AgentLoop with pluggable strategies, tools and Docker sandbox; full per-sample Agent Trace is recorde...
- 🔥 **[2026.05.26]** Added the [GAIA](https://evalscope.readthedocs.io/en/latest/third_party/gaia.html) agent benchmark (multi-turn ReAct + bash in a Docker sandbox, official rule-based scorer) and generic [MCP server](...

Basic usage or getting-started notes:
- 🔥 **[2026.05.19]** Added support for [SWE-bench_Pro](https://evalscope.readthedocs.io/en/latest/third_party/swe_bench_pro.html) and [τ³-bench](https://evalscope.readthedocs.io/en/latest/third_party/tau3_bench.html): S...
- 🔥 **[2026.05.15]** Introduced **Agent Evaluation Mode**: any benchmark based on DefaultDataAdapter (GSM8K, AIME, IFEval, etc.) can now be driven through a multi-turn AgentLoop with pluggable strategies (function_calli...
- 🔥 **[2026.05.08]** Partnered with [LightSeek](https://lightseek.org/) to launch [TokenSpeed](https://lightseek.org/blog/lightseek-tokenspeed.html), a speed-of-light LLM inference engine for agentic workloads. EvalScop...

- Source: https://github.com/modelscope/evalscope
- Extracted from upstream docs: https://raw.githubusercontent.com/modelscope/evalscope/HEAD/README.md

## Documentation

- https://evalscope.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-agent-and-model-workflows-with-evalscope/)
