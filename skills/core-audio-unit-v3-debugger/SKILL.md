---
title: Core Audio Unit v3 Debugger
description: The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins
  on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation)
  with component type, subtype, and manufacturer codes to check host compatibility,
  then captures detailed performance metrics using Instruments’ Audio Unit trace template.
  The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock,
  measures DSP processing time per buffer against the deadline (buffer size / sample
  rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading
  safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and
  checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService
  XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time().
  Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component
  types with full parameter automation validation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/
category:
- Media &amp; Transcription
framework:
- Claude Code
---

# Core Audio Unit v3 Debugger

The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments’ Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/)
