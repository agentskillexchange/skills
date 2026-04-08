---
title: LiveKit Real-Time Video Audio and Data Server with WebRTC
description: 'Overview LiveKit is a production-grade, open-source WebRTC SFU (Selective
  Forwarding Unit) that enables developers to build real-time video, audio, and data
  applications. Built with Go using the Pion WebRTC implementation, LiveKit handles
  the complex infrastructure of real-time media routing while exposing clean client
  and server SDKs. Key Capabilities LiveKit provides a comprehensive real-time communication
  stack: scalable multi-user video and audio conferencing, simulcast and SVC codec
  support (VP9, AV1), speaker detection, selective track subscription, end-to-end
  encryption, moderation APIs, and webhook integrations. It supports UDP, TCP, and
  TURN for robust connectivity across network conditions. Architecture and Deployment
  The server ships as a single Go binary that can be deployed standalone, via Docker,
  or on Kubernetes. It supports distributed multi-region topologies for global scale.
  JWT-based authentication secures room access. The LiveKit CLI ( lk ) provides management
  tools for rooms, tokens, and diagnostics. Agent Integration LiveKit integrates with
  AI agents through its Agents framework, enabling real-time multimodal AI applications.
  Agents can join rooms as programmable backend participants, processing audio/video
  streams and interacting with human participants. The Egress service records or streams
  rooms, while Ingress accepts external sources like RTMP, WHIP, or OBS Studio. Client
  SDKs Official client SDKs are available for JavaScript/TypeScript, Swift (iOS/macOS),
  Kotlin (Android), Flutter/Dart, React (Components UI), Go, Python, Rust, Unity,
  and React Native. Server SDKs exist for Go, Node.js, Python, Ruby, Kotlin/Java,
  Rust, and PHP. Each SDK provides full room management, track publishing/subscribing,
  and data channel communication. Installation brew install livekit livekit-server
  --dev Or via Docker: docker run --rm -p 7880:7880 -p 7881:7881 -p 7882:7882/udp
  livekit/livekit-server --dev'
verification: security_reviewed
source: https://github.com/livekit/livekit
category:
- Integrations &amp; Connectors
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: livekit/livekit
  github_stars: 17975
---

# LiveKit Real-Time Video Audio and Data Server with WebRTC

Overview LiveKit is a production-grade, open-source WebRTC SFU (Selective Forwarding Unit) that enables developers to build real-time video, audio, and data applications. Built with Go using the Pion WebRTC implementation, LiveKit handles the complex infrastructure of real-time media routing while exposing clean client and server SDKs. Key Capabilities LiveKit provides a comprehensive real-time communication stack: scalable multi-user video and audio conferencing, simulcast and SVC codec support (VP9, AV1), speaker detection, selective track subscription, end-to-end encryption, moderation APIs, and webhook integrations. It supports UDP, TCP, and TURN for robust connectivity across network conditions. Architecture and Deployment The server ships as a single Go binary that can be deployed standalone, via Docker, or on Kubernetes. It supports distributed multi-region topologies for global scale. JWT-based authentication secures room access. The LiveKit CLI ( lk ) provides management tools for rooms, tokens, and diagnostics. Agent Integration LiveKit integrates with AI agents through its Agents framework, enabling real-time multimodal AI applications. Agents can join rooms as programmable backend participants, processing audio/video streams and interacting with human participants. The Egress service records or streams rooms, while Ingress accepts external sources like RTMP, WHIP, or OBS Studio. Client SDKs Official client SDKs are available for JavaScript/TypeScript, Swift (iOS/macOS), Kotlin (Android), Flutter/Dart, React (Components UI), Go, Python, Rust, Unity, and React Native. Server SDKs exist for Go, Node.js, Python, Ruby, Kotlin/Java, Rust, and PHP. Each SDK provides full room management, track publishing/subscribing, and data channel communication. Installation brew install livekit livekit-server --dev Or via Docker: docker run --rm -p 7880:7880 -p 7881:7881 -p 7882:7882/udp livekit/livekit-server --dev

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/livekit-realtime-webrtc-server/)
