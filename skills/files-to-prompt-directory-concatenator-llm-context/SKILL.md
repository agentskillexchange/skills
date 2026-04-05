---
name: "files-to-prompt Directory Concatenator for LLM Context"
description: "files-to-prompt by Simon Willison concatenates an entire directory of files into a single prompt for use with LLMs. It supports file extension filtering, gitignore-aware exclusions, Claude XML format output, Markdown fenced code blocks, line numbering, and stdin piping for flexible codebase-to-prompt workflows."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/simonw/files-to-prompt"
tool_ecosystem:
  github_repo: "simonw/files-to-prompt"
  github_stars: 2643
  license: "Apache-2.0"
---
# files-to-prompt Directory Concatenator for LLM Context

files-to-prompt by Simon Willison concatenates an entire directory of files into a single prompt for use with LLMs. It supports file extension filtering, gitignore-aware exclusions, Claude XML format output, Markdown fenced code blocks, line numbering, and stdin piping for flexible codebase-to-prompt workflows.

files-to-prompt is a Python CLI tool by Simon Willison that takes one or more files or directories and concatenates their contents into a single text output, formatted for consumption by Large Language Models. Each file is preceded by its relative path and separated by delimiters, giving the LLM full context about the codebase structure.

How It Works Run files-to-prompt path/to/directory to output every file in that directory with its path as a header. The tool recursively walks the directory tree, respects .gitignore patterns by default, and produces clean output that LLMs can parse to understand project structure and file relationships.

Output Formats The tool supports multiple output modes. Use --cxml for Claude XML format (optimized for Anthropic models), --markdown for Markdown with fenced code blocks, or the default delimiter-separated format. Line numbers can be added with -n for precise code references.

Filtering and Control Filter by file extension with -e txt -e md, ignore specific patterns with --ignore "*.log", include hidden files with --include-hidden, and disable gitignore processing with --ignore-gitignore. Files can also be piped in from other commands like find using stdin, with NUL-separated input supported via --null.

Installation Install via pip: pip install files-to-prompt. The tool requires Python 3.8+ and has minimal dependencies.

Use Cases files-to-prompt is ideal for preparing codebase context for AI coding assistants, feeding project files into LLM prompts for code review or refactoring, generating context windows for RAG pipelines, and creating reproducible prompt inputs from directory trees. It pairs well with tools like llm for end-to-end CLI AI workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill files-to-prompt-directory-concatenator-llm-context
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill files-to-prompt-directory-concatenator-llm-context -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill files-to-prompt-directory-concatenator-llm-context -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill files-to-prompt-directory-concatenator-llm-context -a codex
```

### OpenClaw

```bash
clawhub install files-to-prompt-directory-concatenator-llm-context
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/files-to-prompt-directory-concatenator-llm-context/)
