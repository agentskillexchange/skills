---
name: WritingTools System-Wide AI Grammar Assistant for Windows Linux and macOS
description: >-
  WritingTools is an open-source, Apple Intelligence-inspired writing assistant
  that works system-wide on Windows, Linux, and macOS. With a single hotkey, it
  fixes grammar, rewrites text, summarizes content, and more using cloud or
  local LLMs.
version: 1.0.0
category: Content Writing & SEO
source: https://github.com/theJayTea/WritingTools
verification: listed
---

# WritingTools System-Wide AI Grammar Assistant

WritingTools is a free, open-source application that brings Apple Intelligence-style writing assistance to every platform. Select any text anywhere on your computer and invoke AI-powered writing tools with a single keyboard shortcut (Ctrl+Space on Windows/Linux, or a configurable hotkey on macOS).

## Core Capabilities

WritingTools provides several built-in writing modes: Proofread (fix grammar and spelling), Rewrite (restructure and improve text), Friendly (make text more casual), Professional (make text more formal), and Concise (shorten text while preserving meaning). Users can also enter fully custom instructions like "translate to French", "add comments to this code", or "make it title case".

## Summarization

Beyond text editing, WritingTools can summarize entire webpages, documents, emails, and even YouTube video transcripts. It offers Summary, Key Points, and Table output formats, rendered with Markdown formatting in a clean popup window. Users can then chat with the summary for follow-up questions.

## LLM Backend Flexibility

WritingTools supports multiple LLM backends. The default option uses the free Google Gemini API (Gemini 2.0 Flash), but users can also connect to local LLMs via Ollama, use OpenAI-compatible APIs, or configure any custom API endpoint. This means the tool works fully offline with local models for maximum privacy.

## Platform Support

The Windows and Linux version is built with Python, while the macOS port is a native Swift application. Both versions are actively maintained with the project having been featured in over 28 global publications including Beebom, XDA Developers, How-To Geek, and Windows Central.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill writingtools-system-wide-ai-grammar-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill writingtools-system-wide-ai-grammar-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill writingtools-system-wide-ai-grammar-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill writingtools-system-wide-ai-grammar-assistant -a codex
```

### OpenClaw

```bash
clawhub install writingtools-system-wide-ai-grammar-assistant
```
## Source

- [GitHub](https://github.com/theJayTea/WritingTools)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/writingtools-system-wide-ai-grammar-assistant/)
