---
name: "Tiptap Headless Rich Text Editor Framework for Web Applications"
description: "Tiptap is a headless, framework-agnostic rich text editor built on ProseMirror. It provides a fully customizable editing experience through 100+ extensions, supporting React, Vue, and plain JavaScript with no preset UI constraints."
category: "Content Writing &amp; SEO"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/ueberdosis/tiptap"
tool_ecosystem:
  tool: tiptap
  github_repo: ueberdosis/tiptap
  github_stars: 35948
  npm_weekly_downloads: 40129
  license: MIT
  maintained: true
---
# Tiptap Headless Rich Text Editor Framework for Web Applications

Tiptap is a headless, framework-agnostic rich text editor built on ProseMirror. It provides a fully customizable editing experience through 100+ extensions, supporting React, Vue, and plain JavaScript with no preset UI constraints.

## Overview

Tiptap is a headless rich text editor framework developed by Ueberdosis. Built on the ProseMirror library, it provides a robust foundation for creating custom editing experiences in web applications. Being headless means Tiptap ships without a preset user interface, giving developers complete design freedom while handling the complex editing logic underneath.

Core Capabilities
The editor supports React, Vue, Svelte, and plain JavaScript through official framework bindings. Over 100 extensions are available for functionality ranging from basic text formatting and lists to advanced features like tables, code blocks with syntax highlighting, mentions, collaborative editing, and drag-and-drop block reordering. Custom extensions can be authored to add any editing behavior.

How It Works
Install via npm install @tiptap/core @tiptap/starter-kit and create an editor instance with your chosen extensions. Tiptap manages the document model, input handling, selection management, and undo/redo history. Output can be rendered as HTML, JSON, or plain text. The Hocuspocus companion library provides a CRDT-based collaboration backend powered by Yjs for real-time multi-user editing.

Agent Integration
AI agents building content management systems, documentation platforms, or writing tools can use Tiptap as the editing layer. Its programmatic API allows agents to create, modify, and format rich text documents through code. The JSON document model enables structured content manipulation, and the extension system supports adding AI-powered features like auto-completion, grammar checking, or content suggestion directly into the editing experience.

Key Features

Headless architecture with full design control
Framework bindings for React, Vue, Svelte, and vanilla JS
100+ extensions for rich editing features
ProseMirror-based reliability and performance
Real-time collaboration via Hocuspocus and Yjs
HTML, JSON, and plain text output formats
MIT licensed open-source core

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tiptap-headless-rich-text-editor-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tiptap-headless-rich-text-editor-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tiptap-headless-rich-text-editor-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tiptap-headless-rich-text-editor-framework -a codex
```

### OpenClaw

```bash
clawhub install tiptap-headless-rich-text-editor-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tiptap-headless-rich-text-editor-framework/)
