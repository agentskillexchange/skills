---
title: "Core Audio Unit v3 Debugger"
description: "The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments’ Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation."
verification: security_reviewed
source: "https://developer.apple.com/documentation/audiotoolbox/audio_unit_v3_plug-ins"
framework:
  - "Claude Code"
---

# Core Audio Unit v3 Debugger

The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments’ Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/core-audio-unit-v3-debugger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/core-audio-unit-v3-debugger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/)
