---
name: "smolagents Code-First AI Agent Library"
description: "smolagents is HuggingFace's barebones Python library for building AI agents that think in code rather than JSON. Agents write and execute Python code as their action space, enabling more flexible reasoning and tool use with support for sandboxed execution via E2B, Docker, or WebAssembly."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/huggingface/smolagents"
---
# smolagents Code-First AI Agent Library

smolagents is HuggingFace's barebones Python library for building AI agents that think in code rather than JSON. Agents write and execute Python code as their action space, enabling more flexible reasoning and tool use with support for sandboxed execution via E2B, Docker, or WebAssembly.

## Overview

Overview
smolagents is an open-source Python library from HuggingFace designed to make building AI agents simple and transparent. The entire agent logic fits in roughly 1,000 lines of code, keeping abstractions minimal while providing powerful capabilities for code-generating agents.

How It Works
The core concept is the CodeAgent, which generates Python code as its action output rather than structured JSON tool calls. This approach gives agents the full expressiveness of Python — they can use loops, conditionals, and compose tools naturally. For security, code execution can be sandboxed via Blaxel, E2B, Modal, Docker, or a Pyodide+Deno WebAssembly sandbox.

Key Capabilities
smolagents is model-agnostic, supporting local models via transformers or Ollama, HuggingFace Inference Providers, and commercial APIs through LiteLLM (OpenAI, Anthropic, etc.). It supports text, vision, video, and audio inputs. Tools can be imported from MCP servers, LangChain, or shared via the HuggingFace Hub. The library also supports multi-agent hierarchies where a manager agent delegates to specialized sub-agents.

Integration Points
Install via pip install smolagents. Tools are defined using the @tool decorator or by subclassing Tool. MCP server tools are loaded with ToolCollection.from_mcp(). Agents can be shared to and loaded from the HuggingFace Hub for community reuse. Built-in tools include web search, Python code execution, text-to-speech, and image generation.

Technical Details
With 26,000+ GitHub stars, smolagents is Apache 2.0 licensed and available on PyPI. The library emphasizes simplicity and debuggability — the entire agent loop is readable and hackable. It includes built-in support for OpenTelemetry tracing, Gradio UI generation, and streaming outputs for real-time agent monitoring.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill smolagents-code-first-ai-agent-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill smolagents-code-first-ai-agent-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill smolagents-code-first-ai-agent-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill smolagents-code-first-ai-agent-library -a codex
```

### OpenClaw

```bash
clawhub install smolagents-code-first-ai-agent-library
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/smolagents-code-first-ai-agent-library/)
