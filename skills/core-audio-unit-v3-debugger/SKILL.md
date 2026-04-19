---
title: "Core Audio Unit v3 Debugger"
description: "The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple&#8217;s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments&#8217; Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation."
source: "https://developer.apple.com/documentation/audiotoolbox/audio_unit_v3_plug-ins"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
---

# Core Audio Unit v3 Debugger

The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple&#8217;s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments&#8217; Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/)
