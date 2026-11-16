---
name: "Run evidence-backed mobile app smoke checks with AutoCua"
slug: "run-evidence-backed-mobile-app-smoke-checks-with-autocua"
description: "Run bounded natural-language smoke checks on simulator app builds, then review per-task status and saved observations before reporting results."
github_stars: 1245
verification: "security_reviewed"
source: "https://github.com/ComputerUseAgent/AutoCua"
author: "Ashish Yadav"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ComputerUseAgent/AutoCua"
  github_stars: 1245
---

# Run evidence-backed mobile app smoke checks with AutoCua

Run bounded natural-language smoke checks on simulator app builds, then review per-task status and saved observations before reporting results.

## Prerequisites

Python 3.10+, AutoCua, configured model provider; iOS: macOS, full Xcode, simulator runtime and WebDriverAgent; Android: emulator/system image and supported hypervisor; simulator-compatible app build

## Installation

Install or set up from the source-backed instructions:

Create a Python 3.10+ virtual environment and run pip install AutoCua==3.0.0. Follow upstream mobile simulator setup in README.md and agent_capabilities.md. Configure the chosen provider in the environment; install the documented WebDriverAgent checkout for iOS or provision the Android emulator after accepting SDK terms. Put a simulator .ipa/.app or Android .apk in AutoCua_data/app_build/. Invoke run_agent with simulation mode, app_build, a bounded task and save_conversation=True; preserve earlier evidence before recording another run.

- Source: https://github.com/ComputerUseAgent/AutoCua

## Documentation

- https://github.com/ComputerUseAgent/AutoCua/blob/285ddce9508868cc6a89befe289dc0c7030d8ac4/agent_capabilities.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-evidence-backed-mobile-app-smoke-checks-with-autocua/)
