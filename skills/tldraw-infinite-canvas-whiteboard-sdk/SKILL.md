---
name: "tldraw Infinite Canvas Whiteboard SDK for React"
description: "tldraw is a feature-complete infinite canvas engine and whiteboard SDK for React. It provides drawing, diagramming, real-time multiplayer collaboration, and AI integrations out of the box, with full extensibility for custom shapes, tools, and UI components."
category: "Image & Creative Automation"
framework: "Multi-Framework"
verification: listed
source: "https://agentskillexchange.com/skills/tldraw-infinite-canvas-whiteboard-sdk/"
---
# tldraw Infinite Canvas Whiteboard SDK for React

tldraw is a feature-complete infinite canvas engine and whiteboard SDK for React. It provides drawing, diagramming, real-time multiplayer collaboration, and AI integrations out of the box, with full extensibility for custom shapes, tools, and UI components.

## Overview

What is tldraw?

tldraw is an open-source infinite canvas SDK designed to be the foundation for any canvas-based application. Built in TypeScript for React, it provides a production-ready whiteboard experience that can be used standalone or embedded into custom applications. The project has accumulated over 44,000 stars on GitHub and powers canvas experiences used by companies like ClickUp.

Core Capabilities

The SDK ships with a complete set of drawing and diagramming tools including pressure-sensitive freehand drawing, geometric shapes, rich text editing, arrows with smart connectors, image and video support, and snapping to shapes. It supports multiplayer collaboration through its self-hostable @tldraw/sync package built on Cloudflare Durable Objects.

Extensibility and AI Integration

tldraw is designed for deep customization. Developers can create custom shapes, tools, bindings, and UI components to build entirely new interactions on top of the canvas primitives. The SDK includes built-in support for AI integrations, providing canvas primitives specifically designed for building with LLMs. This makes it suitable for agent-powered applications that need visual interaction surfaces.

Starter Kits and Use Cases

The project provides several starter kits covering common use cases: multiplayer collaboration, AI agent canvas, drag-and-drop workflow builders for automation pipelines, AI chat with canvas annotation, branching chat for conversation exploration, and WebGL shader integration. Each kit is MIT-licensed and can be scaffolded with npx create-tldraw@latest.

Technical Architecture

tldraw uses a DOM-based canvas renderer, meaning it supports anything the browser supports — including embedded websites from YouTube, Figma, GitHub, and more. It works across desktop browsers, touch screens, tablets, and mobile devices. The runtime Editor API allows programmatic control of the canvas, enabling automation and integration with external systems.

Installation and Integration

Installation is straightforward via npm: npm install tldraw. The primary component is imported as a React component that handles the entire canvas experience. The SDK requires React 18+ and provides comprehensive TypeScript types for all APIs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tldraw-infinite-canvas-whiteboard-sdk
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tldraw-infinite-canvas-whiteboard-sdk -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tldraw-infinite-canvas-whiteboard-sdk -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tldraw-infinite-canvas-whiteboard-sdk -a codex
```

### OpenClaw

```bash
clawhub install tldraw-infinite-canvas-whiteboard-sdk
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tldraw-infinite-canvas-whiteboard-sdk/)
