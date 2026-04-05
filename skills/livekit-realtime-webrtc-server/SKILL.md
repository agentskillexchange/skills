---
name: "LiveKit Real-Time Video Audio and Data Server with WebRTC"
description: "LiveKit is an open-source, scalable WebRTC-based real-time communication server written in Go. It provides multi-user conferencing, streaming, and data channels with client SDKs for JavaScript, Swift, Kotlin, Flutter, React, Go, Python, Rust, and Unity."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/livekit/livekit"
tool_ecosystem:
  github_repo: livekit/livekit
  github_stars: 17964
---
# LiveKit Real-Time Video Audio and Data Server with WebRTC

LiveKit is an open-source, scalable WebRTC-based real-time communication server written in Go. It provides multi-user conferencing, streaming, and data channels with client SDKs for JavaScript, Swift, Kotlin, Flutter, React, Go, Python, Rust, and Unity.

## Overview

Overview

LiveKit is a production-grade, open-source WebRTC SFU (Selective Forwarding Unit) that enables developers to build real-time video, audio, and data applications. Built with Go using the Pion WebRTC implementation, LiveKit handles the complex infrastructure of real-time media routing while exposing clean client and server SDKs.

Key Capabilities

LiveKit provides a comprehensive real-time communication stack: scalable multi-user video and audio conferencing, simulcast and SVC codec support (VP9, AV1), speaker detection, selective track subscription, end-to-end encryption, moderation APIs, and webhook integrations. It supports UDP, TCP, and TURN for robust connectivity across network conditions.

Architecture and Deployment

The server ships as a single Go binary that can be deployed standalone, via Docker, or on Kubernetes. It supports distributed multi-region topologies for global scale. JWT-based authentication secures room access. The LiveKit CLI (`lk`) provides management tools for rooms, tokens, and diagnostics.

Agent Integration

LiveKit integrates with AI agents through its Agents framework, enabling real-time multimodal AI applications. Agents can join rooms as programmable backend participants, processing audio/video streams and interacting with human participants. The Egress service records or streams rooms, while Ingress accepts external sources like RTMP, WHIP, or OBS Studio.

Client SDKs

Official client SDKs are available for JavaScript/TypeScript, Swift (iOS/macOS), Kotlin (Android), Flutter/Dart, React (Components UI), Go, Python, Rust, Unity, and React Native. Server SDKs exist for Go, Node.js, Python, Ruby, Kotlin/Java, Rust, and PHP. Each SDK provides full room management, track publishing/subscribing, and data channel communication.

Installation
``brew install livekit
livekit-server --dev``

Or via Docker: `docker run --rm -p 7880:7880 -p 7881:7881 -p 7882:7882/udp livekit/livekit-server --dev`

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill livekit-realtime-webrtc-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill livekit-realtime-webrtc-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill livekit-realtime-webrtc-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill livekit-realtime-webrtc-server -a codex
```

### OpenClaw

```bash
clawhub install livekit-realtime-webrtc-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/livekit-realtime-webrtc-server/)
