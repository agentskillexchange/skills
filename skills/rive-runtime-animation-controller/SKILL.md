---
title: "Rive Runtime Animation Controller"
description: "Controls Rive (.riv) interactive animations at runtime using @rive-app/canvas-advanced, manages state machine inputs, and synchronizes animation states with application data via the Rive WASM runtime."
verification: "security_reviewed"
source: "https://github.com/rive-app/rive-react"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "rive-app/rive-react"
  github_stars: 1111
---

# Rive Runtime Animation Controller

The Rive Runtime Animation Controller manages interactive vector animations using the @rive-app/canvas-advanced package and Rive’s WASM runtime. It loads .riv files exported from the Rive editor, instantiates artboards, and drives state machine transitions by programmatically setting boolean, number, and trigger inputs via StateMachineInput objects. The agent handles multiple artboards within a single .riv file, synchronizes animation playback with application state (scroll position, user input, data changes), and manages the requestAnimationFrame render loop with proper cleanup. It supports Rive’s text runs for dynamic text content, mesh deformations for character animation, and Rive events (RiveEvent) for bidirectional communication between animation and host application. For React integration, it generates components using @rive-app/react-canvas with useRive and useStateMachineInput hooks. Performance optimization includes offscreen canvas rendering with transferToImageBitmap and Web Worker-based animation updates. Handles fallback to Lottie export for browsers without WASM support.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/rive-runtime-animation-controller/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rive-runtime-animation-controller
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/rive-runtime-animation-controller`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rive-runtime-animation-controller/)
