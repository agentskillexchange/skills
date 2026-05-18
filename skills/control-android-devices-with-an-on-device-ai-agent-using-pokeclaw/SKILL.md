---
name: "Control Android devices with an on-device AI agent using PokeClaw"
slug: "control-android-devices-with-an-on-device-ai-agent-using-pokeclaw"
description: "Run an on-device Android control loop that inspects screens and performs app actions locally for mobile automation and testing workflows."
github_stars: 760
verification: "listed"
source: "https://github.com/agents-io/PokeClaw"
author: "agents-io"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "agents-io/PokeClaw"
  github_stars: 760
---

# Control Android devices with an on-device AI agent using PokeClaw

Run an on-device Android control loop that inspects screens and performs app actions locally for mobile automation and testing workflows.

## Prerequisites

PokeClaw; Android device or emulator; project-documented runtime dependencies

## Installation

Requirements and caveats from upstream:
- DroidRun/Mobilerun local/open-source runs the agent loop in a Python CLI/container on a host machine and talks to a Portal APK through ADB/port forwarding. The Portal APK uses Android Accessibility for tree/gesture/sc...
- minitap/mobile-use, Mobile-Agent, AppAgent, and AppAgentX are external SDK/research harnesses that normally require Python plus ADB, UIAutomator, screenshots, Docker, cloud phones, or host-side model/API services.
- does not require a computer to be connected while tasks run

Basic usage or getting-started notes:
- It can run Gemma 4 on-device for local, private phone control, and it also supports optional cloud models when you want stronger reasoning for harder tasks.
- task state leaks into the next run
- model download, storage, or LiteRT startup fails before the model can run

- Source: https://github.com/agents-io/PokeClaw
- Extracted from upstream docs: https://raw.githubusercontent.com/agents-io/PokeClaw/HEAD/README.md

## Documentation

- https://github.com/agents-io/PokeClaw

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-android-devices-with-an-on-device-ai-agent-using-pokeclaw/)
