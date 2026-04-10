---
title: "Rive Runtime Animation Controller"
description: "Controls Rive (.riv) interactive animations at runtime using @rive-app/canvas-advanced, manages state machine inputs, and synchronizes animation states with application data via the Rive WASM runtime."
slug: "rive-runtime-animation-controller"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://github.com/rive-app/rive-react"
tool_ecosystem:
  github_repo: "rive-app/rive-react"
  github_stars: 1111
listed: true
---

# Rive Runtime Animation Controller

Controls Rive (.riv) interactive animations at runtime using @rive-app/canvas-advanced, manages state machine inputs, and synchronizes animation states with application data via the Rive WASM runtime.

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
clawhub install rive-runtime-animation-controller
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Rive Runtime Animation Controller manages interactive vector animations using the @rive-app/canvas-advanced package and Rive’s WASM runtime. It loads .riv files exported from the Rive editor, instantiates artboards, and drives state machine transitions by programmatically setting boolean, number, and trigger inputs via StateMachineInput objects. The agent handles multiple artboards within a single .riv file, synchronizes animation playback with application state (scroll position, user input, data changes), and manages the requestAnimationFrame render loop with proper cleanup. It supports Rive’s text runs for dynamic text content, mesh deformations for character animation, and Rive events (RiveEvent) for bidirectional communication between animation and host application. For React integration, it generates components using @rive-app/react-canvas with useRive and useStateMachineInput hooks. Performance optimization includes offscreen canvas rendering with transferToImageBitmap and Web Worker-based animation updates. Handles fallback to Lottie export for browsers without WASM support.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rive-runtime-animation-controller/)
