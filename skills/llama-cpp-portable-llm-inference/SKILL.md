---
title: "llama.cpp Portable LLM Inference Engine in C/C++"
description: "llama.cpp is a high-performance C/C++ implementation for running LLM inference across diverse hardware. It supports GGUF model quantization, GPU acceleration on NVIDIA/AMD/Apple Silicon, and provides both a CLI and an OpenAI-compatible HTTP server for local model serving."
slug: "llama-cpp-portable-llm-inference"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/ggml-org/llama.cpp"
tool_ecosystem:
  github_repo: "ggml-org/llama.cpp"
  github_stars: 100939
listed: true
---

# llama.cpp Portable LLM Inference Engine in C/C++

llama.cpp is a high-performance C/C++ implementation for running LLM inference across diverse hardware. It supports GGUF model quantization, GPU acceleration on NVIDIA/AMD/Apple Silicon, and provides both a CLI and an OpenAI-compatible HTTP server for local model serving.

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
clawhub install llama-cpp-portable-llm-inference
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

llama.cpp is the foundational open-source project for running large language models efficiently in plain C/C++ with zero external dependencies. Originally created by Georgi Gerganov, it has become the most widely used local LLM inference engine, powering tools like Ollama, LM Studio, and GPT4All under the hood.
What It Does
llama.cpp loads GGUF-format model weights and runs inference using highly optimized CPU and GPU kernels. It supports quantization levels from 1.5-bit to 8-bit integer and FP8, enabling models that would normally require 100+ GB of VRAM to run on consumer hardware. The project includes llama-cli for interactive chat, llama-server for OpenAI-compatible API serving, and tools for model conversion and quantization.
How Agents Use It
Agents connect to llama-server’s OpenAI-compatible REST API for local inference without cloud dependencies. The server supports chat completions, text completions, embeddings, and multimodal inputs (vision models). Agents can use it for code generation, document analysis, structured output with grammar-constrained decoding, and function calling. The GGUF format allows downloading pre-quantized models directly from Hugging Face.
Key Features
- Pure C/C++ with no dependencies — compiles on virtually any platform
- Apple Silicon first-class support via ARM NEON, Accelerate, and Metal
- NVIDIA CUDA and AMD HIP GPU acceleration
- 1.5-bit to 8-bit integer quantization for memory-efficient inference
- CPU+GPU hybrid inference for models larger than available VRAM
- OpenAI-compatible HTTP server (llama-server)
- Multimodal support for vision models
- Speculative decoding and continuous batching for throughput
- VS Code and Neovim plugins for local code completion
Integration Points
Install via Homebrew (brew install llama.cpp), Nix, or build from source. Download models from Hugging Face with llama-cli -hf ggml-org/gemma-3-1b-it-GGUF. Launch an API server with llama-server -hf ggml-org/gemma-3-1b-it-GGUF. The project supports over 100 model architectures including LLaMA, Mistral, Gemma, Qwen, DeepSeek, and Phi.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/llama-cpp-portable-llm-inference/)
