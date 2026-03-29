---
name: "Rive Runtime Animation Controller"
description: "Controls Rive (.riv) interactive animations at runtime using @rive-app/canvas-advanced, manages state machine inputs, and synchronizes animation states with application data via the Rive WASM runtime."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rive-runtime-animation-controller/"
tool_ecosystem:
  tool: react
  github_stars: 244163
  npm_weekly_downloads: 104796073
  github_repo: facebook/react
  license: MIT
  maintained: true
---
# Rive Runtime Animation Controller

Controls Rive (.riv) interactive animations at runtime using @rive-app/canvas-advanced, manages state machine inputs, and synchronizes animation states with application data via the Rive WASM runtime.

## Overview

The Rive Runtime Animation Controller manages interactive vector animations using the @rive-app/canvas-advanced package and Rive’s WASM runtime. It loads .riv files exported from the Rive editor, instantiates artboards, and drives state machine transitions by programmatically setting boolean, number, and trigger inputs via StateMachineInput objects. The agent handles multiple artboards within a single .riv file, synchronizes animation playback with application state (scroll position, user input, data changes), and manages the requestAnimationFrame render loop with proper cleanup. It supports Rive’s text runs for dynamic text content, mesh deformations for character animation, and Rive events (RiveEvent) for bidirectional communication between animation and host application. For React integration, it generates components using @rive-app/react-canvas with useRive and useStateMachineInput hooks. Performance optimization includes offscreen canvas rendering with transferToImageBitmap and Web Worker-based animation updates. Handles fallback to Lottie export for browsers without WASM support.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rive-runtime-animation-controller
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rive-runtime-animation-controller -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rive-runtime-animation-controller -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rive-runtime-animation-controller -a codex
```

### OpenClaw

```bash
clawhub install rive-runtime-animation-controller
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rive-runtime-animation-controller/)
