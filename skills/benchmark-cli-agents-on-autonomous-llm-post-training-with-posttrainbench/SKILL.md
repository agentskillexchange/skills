---
name: "Benchmark CLI agents on autonomous LLM post-training with PostTrainBench"
slug: "benchmark-cli-agents-on-autonomous-llm-post-training-with-posttrainbench"
description: "Run Claude Code, Codex CLI, Gemini CLI, or OpenCode through bounded H100 post-training tasks and compare how well each agent improves a base LLM."
github_stars: 543
verification: "security_reviewed"
source: "https://github.com/aisa-group/PostTrainBench"
author: "AISA Group"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aisa-group/PostTrainBench"
  github_stars: 543
---

# Benchmark CLI agents on autonomous LLM post-training with PostTrainBench

Run Claude Code, Codex CLI, Gemini CLI, or OpenCode through bounded H100 post-training tasks and compare how well each agent improves a base LLM.

## Prerequisites

Python, apptainer, fuse-overlayfs, Hugging Face cache, H100 GPU access, currently HTCondor scheduler support, and credentials for the selected CLI agent scaffolds

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/aisa-group/PostTrainBench, install requirements including apptainer and fuse-overlayfs, build the standard container with bash containers/build_container.sh standard, download the Hugging Face cache with bash containers/download_hf_cache/download_hf_cache.sh, copy example.env to .env, set API keys and paths, then submit jobs with bash src/commit_utils/commit.sh.

- Source: https://github.com/aisa-group/PostTrainBench

## Documentation

- http://posttrainbench.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-cli-agents-on-autonomous-llm-post-training-with-posttrainbench/)
