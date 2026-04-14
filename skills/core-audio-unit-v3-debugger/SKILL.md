---
title: "Core Audio Unit v3 Debugger"
description: "Debugs and profiles Apple Audio Unit v3 (AUv3) plugins using auval validation tool, the AUAudioUnit Swift API, and Instruments AudioUnit trace template for latency measurement and buffer underrun detection."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
---

# Core Audio Unit v3 Debugger

The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments’ Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/)
