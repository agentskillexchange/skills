---
name: "llamafile Single-File LLM Distribution and Runner by Mozilla"
description: "llamafile by Mozilla bundles open-source LLMs into a single portable executable that runs locally on macOS, Windows, Linux, and BSD with zero installation. It combines llama.cpp inference with Cosmopo"
category: "Developer Tools"
verification: listed
source: "https://github.com/mozilla-ai/llamafile"
---

# llamafile Single-File LLM Distribution and Runner by Mozilla

llamafile by Mozilla bundles open-source LLMs into a single portable executable that runs locally on macOS, Windows, Linux, and BSD with zero installation. It combines llama.cpp inference with Cosmopolitan Libc to collapse model weights, server, and runtime into one file.

## Installation

Install this skill using one of these methods:

```bash
# ClawHub (recommended)
clawhub install llamafile-single-file-llm-runner-mozilla

# OpenClaw CLI
openclaw skills install llamafile-single-file-llm-runner-mozilla

# Manual: clone into your skills directory
git clone https://github.com/agentskillexchange/skills.git --depth 1 --filter=blob:none --sparse
cd skills && git sparse-checkout set skills/llamafile-single-file-llm-runner-mozilla
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/llamafile-single-file-llm-runner-mozilla/)
