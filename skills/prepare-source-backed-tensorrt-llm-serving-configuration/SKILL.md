---
name: "Prepare a source-backed TensorRT-LLM serving configuration"
slug: "prepare-source-backed-tensorrt-llm-serving-configuration"
description: "Use NVIDIA’s native configuration skill to select a checked-in single-node PyTorch serving recipe and return YAML, provenance and a launch or benchmark plan."
verification: "security_reviewed"
source: "https://github.com/NVIDIA/TensorRT-LLM/tree/main/.claude/skills/trtllm-serve-config-guide"
author: "NVIDIA Corporation"
publisher_type: "company"
category: "Developer Tools"
framework: "Claude Code"
---

# Prepare a source-backed TensorRT-LLM serving configuration

Use NVIDIA’s native configuration skill to select a checked-in single-node PyTorch serving recipe and return YAML, provenance and a launch or benchmark plan.

## Prerequisites

Claude Code; Git; a complete TensorRT-LLM checkout with examples/configs, deployment guides and the skill reference files. A supported NVIDIA GPU and compatible TensorRT-LLM runtime are needed only for subsequent execution and benchmarking.

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/NVIDIA/TensorRT-LLM.git and start Claude Code in the checkout. Read AGENTS.md and explicitly invoke the repository skill at .claude/skills/trtllm-serve-config-guide/SKILL.md. Provide the model, hardware, sequence lengths, concurrency, tensor-parallel size and performance objective. Keep its references/ directory and checked-in configuration database available; copying the skill alone omits essential evidence. Ask for YAML and provenance first. Follow NVIDIA's model-specific deployment documentation separately if you later choose to install the runtime and launch the generated command.

- Source: https://github.com/NVIDIA/TensorRT-LLM/tree/main/.claude/skills/trtllm-serve-config-guide

## Documentation

- https://github.com/NVIDIA/TensorRT-LLM/tree/main/.claude/skills/trtllm-serve-config-guide

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-source-backed-tensorrt-llm-serving-configuration/)
