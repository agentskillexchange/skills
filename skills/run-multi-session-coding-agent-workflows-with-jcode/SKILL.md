---
name: "Run multi-session coding-agent workflows with jcode"
slug: "run-multi-session-coding-agent-workflows-with-jcode"
description: "Use jcode as a local coding-agent harness for long-running, multi-session repository work with custom provider and memory configuration."
github_stars: 8229
verification: "security_reviewed"
source: "https://github.com/1jehuang/jcode"
author: "1jehuang"
publisher_type: "individual"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "1jehuang/jcode"
  github_stars: 8229
---

# Run multi-session coding-agent workflows with jcode

Use jcode as a local coding-agent harness for long-running, multi-session repository work with custom provider and memory configuration.

## Prerequisites

Local shell, Git, jcode CLI, configured model provider

## Installation

Use the upstream install or setup path that matches your environment:
- brew tap 1jehuang/jcode
- brew install jcode
- git clone https://github.com/1jehuang/jcode.git
- cargo build --release

Requirements and caveats from upstream:
- extra_body — inject non-standard top-level fields into every chat/completions request body for backends that require them. See [Extra request-body fields](#extra-request-body-fields-extra_body) below.
- For local servers that do not require auth:
- Some OpenAI-compatible backends require non-standard top-level request fields. For example, NVIDIA NIM DeepSeek-V4 reasoning models (deepseek-ai/deepseek-v4-flash, deepseek-ai/deepseek-v4-pro) only enable thinking whe...

Basic usage or getting-started notes:
- [Website](https://solosystems.dev/jcode) · [Features](#features) · [Install](#installation) · [Quick Start](#quick-start) · [Further Reading](#further-reading) · [Contributing](CONTRIBUTING.md)
- jcode is built to be as performant and resource efficient as possible. Every metric is optimized to the bone, which is important for scaling multi-session workflows. Here we sample a few metrics to show the difference...
- Measured on this Linux machine across 10 interactive PTY launches. Antigravity CLI was unauthenticated for this run; its sign-in screen rendered normally and emitted an internal CLI ready for user input marker, but di...

- Source: https://github.com/1jehuang/jcode
- Extracted from upstream docs: https://raw.githubusercontent.com/1jehuang/jcode/HEAD/README.md

## Documentation

- https://solosystems.dev/jcode

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-session-coding-agent-workflows-with-jcode/)
