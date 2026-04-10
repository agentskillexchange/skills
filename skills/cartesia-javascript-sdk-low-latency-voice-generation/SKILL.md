---
name: "Cartesia JavaScript SDK for Low-Latency Voice Generation"
description: "An ASE skill built around the official Cartesia JavaScript SDK for text-to-speech and voice API workflows. It is a strong fit for agents that need programmatic voice generation, low-latency speech responses, and direct integration with Cartesia’s hosted models."
verification: security_reviewed
source: "https://github.com/cartesia-ai/cartesia-js"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
---

# Cartesia JavaScript SDK for Low-Latency Voice Generation

Cartesia JavaScript SDK for Low-Latency Voice Generation is a source-backed ASE skill based on the official @cartesia/cartesia-js client from Cartesia. The SDK provides a typed interface to the Cartesia REST API from server-side JavaScript or TypeScript, including text-to-speech generation through Cartesia voice models such as Sonic. For ASE, that matters because it gives agents a real vendor SDK with a defined API surface instead of a made-up “voice AI” wrapper.
The practical job-to-be-done is building reliable voice output into agent workflows. An agent can use this SDK to submit transcripts for synthesis, choose model and output parameters, control format settings, and hand generated audio to downstream delivery systems. That makes it useful for voice assistants, narrated alerts, generated call prompts, product demos, dynamic audio snippets, and systems that need fast turnaround from text input to playable speech output. Because the SDK is the official client, it also reduces the friction of auth handling and request shaping compared with custom REST plumbing.
Integration points include Node.js services, TypeScript backends, queue workers, automation pipelines, and applications that already manage outbound media or telephony events. Cartesia publishes official docs, the repository is active and licensed, and the package is distributed on npm, which satisfies the ASE intake gate for real source, real maintenance, and clear adoption signals. In short, this skill gives agents a concrete way to plug into Cartesia voice generation workflows with current upstream documentation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cartesia-javascript-sdk-low-latency-voice-generation/)
