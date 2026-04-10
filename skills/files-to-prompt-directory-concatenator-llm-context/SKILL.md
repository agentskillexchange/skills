---
title: "files-to-prompt Directory Concatenator for LLM Context"
description: "files-to-prompt by Simon Willison concatenates an entire directory of files into a single prompt for use with LLMs. It supports file extension filtering, gitignore-aware exclusions, Claude XML format output, Markdown fenced code blocks, line numbering, and stdin piping for flexible codebase-to-prompt workflows."
slug: "files-to-prompt-directory-concatenator-llm-context"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/simonw/files-to-prompt"
tool_ecosystem:
  github_repo: "simonw/files-to-prompt"
  github_stars: 2643
listed: true
---

# files-to-prompt Directory Concatenator for LLM Context

files-to-prompt by Simon Willison concatenates an entire directory of files into a single prompt for use with LLMs. It supports file extension filtering, gitignore-aware exclusions, Claude XML format output, Markdown fenced code blocks, line numbering, and stdin piping for flexible codebase-to-prompt workflows.

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
clawhub install files-to-prompt-directory-concatenator-llm-context
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

files-to-prompt is a Python CLI tool by Simon Willison that takes one or more files or directories and concatenates their contents into a single text output, formatted for consumption by Large Language Models. Each file is preceded by its relative path and separated by delimiters, giving the LLM full context about the codebase structure.
How It Works
Run files-to-prompt path/to/directory to output every file in that directory with its path as a header. The tool recursively walks the directory tree, respects .gitignore patterns by default, and produces clean output that LLMs can parse to understand project structure and file relationships.
Output Formats
The tool supports multiple output modes. Use --cxml for Claude XML format (optimized for Anthropic models), --markdown for Markdown with fenced code blocks, or the default delimiter-separated format. Line numbers can be added with -n for precise code references.
Filtering and Control
Filter by file extension with -e txt -e md, ignore specific patterns with --ignore "*.log", include hidden files with --include-hidden, and disable gitignore processing with --ignore-gitignore. Files can also be piped in from other commands like find using stdin, with NUL-separated input supported via --null.
Installation
Install via pip: pip install files-to-prompt. The tool requires Python 3.8+ and has minimal dependencies.
Use Cases
files-to-prompt is ideal for preparing codebase context for AI coding assistants, feeding project files into LLM prompts for code review or refactoring, generating context windows for RAG pipelines, and creating reproducible prompt inputs from directory trees. It pairs well with tools like llm for end-to-end CLI AI workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/files-to-prompt-directory-concatenator-llm-context/)
