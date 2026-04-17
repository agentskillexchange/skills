---
title: "llama.cpp Portable LLM Inference Engine in C/C++"
description: "llama.cpp is the foundational open-source project for running large language models efficiently in plain C/C++ with zero external dependencies. Originally created by Georgi Gerganov, it has become the most widely used local LLM inference engine, powering tools like Ollama, LM Studio, and GPT4All under the hood.\nWhat It Does\nllama.cpp loads GGUF-format model weights and runs inference using highly optimized CPU and GPU kernels. It supports quantization levels from 1.5-bit to 8-bit integer and FP8, enabling models that would normally require 100+ GB of VRAM to run on consumer hardware. The project includes llama-cli for interactive chat, llama-server for OpenAI-compatible API serving, and tools for model conversion and quantization.\nHow Agents Use It\nAgents connect to llama-server’s OpenAI-compatible REST API for local inference without cloud dependencies. The server supports chat completions, text completions, embeddings, and multimodal inputs (vision models). Agents can use it for code generation, document analysis, structured output with grammar-constrained decoding, and function calling. The GGUF format allows downloading pre-quantized models directly from Hugging Face.\nKey Features\n\nPure C/C++ with no dependencies — compiles on virtually any platform\nApple Silicon first-class support via ARM NEON, Accelerate, and Metal\nNVIDIA CUDA and AMD HIP GPU acceleration\n1.5-bit to 8-bit integer quantization for memory-efficient inference\nCPU+GPU hybrid inference for models larger than available VRAM\nOpenAI-compatible HTTP server (llama-server)\nMultimodal support for vision models\nSpeculative decoding and continuous batching for throughput\nVS Code and Neovim plugins for local code completion\n\nIntegration Points\nInstall via Homebrew (brew install llama.cpp), Nix, or build from source. Download models from Hugging Face with llama-cli -hf ggml-org/gemma-3-1b-it-GGUF. Launch an API server with llama-server -hf ggml-org/gemma-3-1b-it-GGUF. The project supports over 100 model architectures including LLaMA, Mistral, Gemma, Qwen, DeepSeek, and Phi."
verification: security_reviewed
source: "https://github.com/ggml-org/llama.cpp"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ggml-org/llama.cpp"
  github_stars: 100939
---

# llama.cpp Portable LLM Inference Engine in C/C++

llama.cpp is the foundational open-source project for running large language models efficiently in plain C/C++ with zero external dependencies. Originally created by Georgi Gerganov, it has become the most widely used local LLM inference engine, powering tools like Ollama, LM Studio, and GPT4All under the hood.
What It Does
llama.cpp loads GGUF-format model weights and runs inference using highly optimized CPU and GPU kernels. It supports quantization levels from 1.5-bit to 8-bit integer and FP8, enabling models that would normally require 100+ GB of VRAM to run on consumer hardware. The project includes llama-cli for interactive chat, llama-server for OpenAI-compatible API serving, and tools for model conversion and quantization.
How Agents Use It
Agents connect to llama-server’s OpenAI-compatible REST API for local inference without cloud dependencies. The server supports chat completions, text completions, embeddings, and multimodal inputs (vision models). Agents can use it for code generation, document analysis, structured output with grammar-constrained decoding, and function calling. The GGUF format allows downloading pre-quantized models directly from Hugging Face.
Key Features

Pure C/C++ with no dependencies — compiles on virtually any platform
Apple Silicon first-class support via ARM NEON, Accelerate, and Metal
NVIDIA CUDA and AMD HIP GPU acceleration
1.5-bit to 8-bit integer quantization for memory-efficient inference
CPU+GPU hybrid inference for models larger than available VRAM
OpenAI-compatible HTTP server (llama-server)
Multimodal support for vision models
Speculative decoding and continuous batching for throughput
VS Code and Neovim plugins for local code completion

Integration Points
Install via Homebrew (brew install llama.cpp), Nix, or build from source. Download models from Hugging Face with llama-cli -hf ggml-org/gemma-3-1b-it-GGUF. Launch an API server with llama-server -hf ggml-org/gemma-3-1b-it-GGUF. The project supports over 100 model architectures including LLaMA, Mistral, Gemma, Qwen, DeepSeek, and Phi.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/llama-cpp-portable-llm-inference
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/llama-cpp-portable-llm-inference` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/llama-cpp-portable-llm-inference/)
