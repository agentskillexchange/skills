---
title: "Fabric AI Prompt Pattern Framework"
description: "Fabric is an open-source framework for augmenting humans using AI. It provides a modular system of crowdsourced prompt patterns that solve specific problems—from summarizing content to extracting wisdom to analyzing security threats—all usable from the command line."
verification: "security_reviewed"
source: "https://github.com/danielmiessler/fabric"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "danielmiessler/fabric"
  github_stars: 40278
  license: "MIT"
---

# Fabric AI Prompt Pattern Framework

What is Fabric?
Fabric is an open-source framework created by Daniel Miessler for augmenting human capabilities using AI. The core concept is “patterns”—carefully crafted, crowdsourced prompt templates that solve specific, well-defined problems. Instead of writing ad-hoc prompts, users invoke named patterns like extract_wisdom, summarize, analyze_threat, write_essay, or create_coding_project. Each pattern is a standalone markdown file with a system prompt optimized for its task.


The framework ships as a Go CLI that integrates with multiple LLM providers including OpenAI, Anthropic, Google, Ollama, and any OpenAI-compatible API. Patterns can be piped together in Unix-style workflows, making Fabric a composable building block for AI-augmented command-line pipelines.


How It Works
Install Fabric with go install github.com/danielmiessler/fabric@latest and run fabric --setup to configure your LLM provider API keys. To use a pattern, pipe input into Fabric: cat article.txt | fabric --pattern summarize or yt --transcript URL | fabric --pattern extract_wisdom. The tool handles the LLM API call, applies the pattern’s system prompt, and outputs the structured result to stdout.


Fabric includes a built-in YouTube transcript extractor, speech-to-text support with the --transcribe-file flag, and media file splitting for processing long audio. Users can create custom patterns by adding markdown files to their local patterns directory, and the community-maintained pattern library covers domains from cybersecurity and software development to content creation and personal productivity.


Output and Integration
Fabric outputs structured markdown text designed for further processing or direct reading. Results can be saved, piped to other tools, or chained through multiple patterns. The framework supports model selection per invocation, temperature control, and streaming output. With over 40,000 GitHub stars, MIT license, and hundreds of community-contributed patterns, Fabric has become one of the most popular AI CLI tools for developers and security professionals.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fabric-ai-prompt-pattern-framework/)
