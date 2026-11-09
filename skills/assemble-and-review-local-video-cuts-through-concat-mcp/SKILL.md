---
name: "Assemble and review local video cuts through Concat MCP"
slug: "assemble-and-review-local-video-cuts-through-concat-mcp"
description: "Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and track export completion through MCP."
verification: "security_reviewed"
source: "https://github.com/jub0t/Concat/blob/9fcd218ba75d0f4856cc2daf36eeae906a08818d/docs/MCP.md"
author: "jub0t"
publisher_type: "community"
category: "Media & Transcription"
framework: "MCP"
---

# Assemble and review local video cuts through Concat MCP

Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and track export completion through MCP.

## Prerequisites

Concat desktop binary with built-in MCP server; MCP-capable agent client; local source footage and writable project/output directories

## Installation

Install or set up from the source-backed instructions:

Download and install the appropriate desktop build from https://github.com/jub0t/Concat/releases/tag/v0.2.9. Configure your MCP client with the installed Concat binary as command and --mcp as its argument. macOS command: /Applications/Concat.app/Contents/MacOS/concat; packaged Linux: /usr/bin/concat; Windows: the installed concat.exe path. For Claude Code on macOS: claude mcp add concat -- /Applications/Concat.app/Contents/MacOS/concat --mcp. Call concat_version and inspect the tool schemas. No separate npm package is required. See the pinned documentation for window/headless mode and permitted filesystem roots.

- Source: https://github.com/jub0t/Concat/blob/9fcd218ba75d0f4856cc2daf36eeae906a08818d/docs/MCP.md

## Documentation

- https://github.com/jub0t/Concat/blob/9fcd218ba75d0f4856cc2daf36eeae906a08818d/docs/MCP.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemble-and-review-local-video-cuts-through-concat-mcp/)
