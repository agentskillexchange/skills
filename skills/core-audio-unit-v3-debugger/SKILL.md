---
name: "Core Audio Unit v3 Debugger"
description: "Debugs and profiles Apple Audio Unit v3 (AUv3) plugins using auval validation tool, the AUAudioUnit Swift API, and Instruments AudioUnit trace template for latency measurement and buffer underrun detection."
category: "Media &amp; Transcription"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/"
---
# Core Audio Unit v3 Debugger

Debugs and profiles Apple Audio Unit v3 (AUv3) plugins using auval validation tool, the AUAudioUnit Swift API, and Instruments AudioUnit trace template for latency measurement and buffer underrun detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill core-audio-unit-v3-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill core-audio-unit-v3-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill core-audio-unit-v3-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill core-audio-unit-v3-debugger -a codex
```

### OpenClaw

```bash
clawhub install core-audio-unit-v3-debugger
```

## Details

The Core Audio Unit v3 Debugger validates and profiles AUv3 audio plugins on macOS and iOS using Apple’s audio toolchain. It runs auval (Audio Unit Validation) with component type, subtype, and manufacturer codes to check host compatibility, then captures detailed performance metrics using Instruments’ Audio Unit trace template. The agent monitors real-time buffer callbacks via AUAudioUnit.internalRenderBlock, measures DSP processing time per buffer against the deadline (buffer size / sample rate), and flags buffer underruns. It inspects AUParameterTree for parameter threading safety, validates kAudioComponentFlag_SandboxSafe for App Store compliance, and checks Inter-App Audio connectivity. For debugging, it attaches to the AUHostingService XPC process and logs renderBlock invocations with nanosecond timestamps via mach_absolute_time(). Supports both Effect (aufx), Instrument (aumu), and MIDI Processor (aumi) component types with full parameter automation validation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/core-audio-unit-v3-debugger/)
