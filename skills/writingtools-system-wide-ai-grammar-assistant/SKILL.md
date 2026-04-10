---
name: WritingTools System-Wide AI Grammar Assistant for Windows Linux and macOS
description: WritingTools is an open-source, Apple Intelligence-inspired writing assistant
  that works system-wide on Windows, Linux, and macOS. With a single hotkey, it fixes
  grammar, rewrites text, summarizes content, and more using cloud or local LLMs.
verification: security_reviewed
source: https://github.com/theJayTea/WritingTools
category:
- Content Writing &amp; SEO
framework:
- Custom Agents
tool_ecosystem:
  github_repo: theJayTea/WritingTools
  github_stars: 2186
---
# WritingTools System-Wide AI Grammar Assistant for Windows Linux and macOS

WritingTools is a free, open-source application that brings Apple Intelligence-style writing assistance to every platform. Created by theJayTea (Jesai), it lets you select any text anywhere on your computer and invoke AI-powered writing tools with a single keyboard shortcut (Ctrl+Space on Windows/Linux, or a configurable hotkey on macOS).
Core Capabilities
WritingTools provides several built-in writing modes: Proofread (fix grammar and spelling), Rewrite (restructure and improve text), Friendly (make text more casual), Professional (make text more formal), and Concise (shorten text while preserving meaning). Users can also enter fully custom instructions like &#8220;translate to French&#8221;, &#8220;add comments to this code&#8221;, or &#8220;make it title case&#8221;.
Summarization
Beyond text editing, WritingTools can summarize entire webpages, documents, emails, and even YouTube video transcripts. It offers Summary, Key Points, and Table output formats, rendered with Markdown formatting in a clean popup window. Users can then chat with the summary for follow-up questions.
LLM Backend Flexibility
WritingTools supports multiple LLM backends. The default option uses the free Google Gemini API (Gemini 2.0 Flash), but users can also connect to local LLMs via Ollama, use OpenAI-compatible APIs, or configure any custom API endpoint. This means the tool works fully offline with local models for maximum privacy.
Platform Support
The Windows and Linux version is built with Python, while the macOS port is a native Swift application built by contributor Arya Mirsepasi. Both versions are actively maintained with the project having been featured in over 28 global publications including Beebom, XDA Developers, How-To Geek, and Windows Central.
Agent Integration
For AI agent workflows, WritingTools can be integrated into content pipelines where grammar checking, rewriting, or summarization is needed as a processing step. The tool accepts text via its hotkey interface and can be scripted through its API configuration to work with different LLM providers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/writingtools-system-wide-ai-grammar-assistant/)
