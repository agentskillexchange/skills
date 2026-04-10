---
name: "OpenReplay Self-Hosted Session Replay and Product Analytics Platform"
description: "OpenReplay is an open-source session replay suite you can self-host. It captures user sessions with network activity, console logs, JS errors, store state, and performance metrics to help reproduce issues and iterate on products faster."
verification: security_reviewed
source: "https://github.com/openreplay/openreplay"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
---

# OpenReplay Self-Hosted Session Replay and Product Analytics Platform

OpenReplay is an open-source session replay and product analytics platform with nearly 12,000 GitHub stars. Unlike cloud-based alternatives like FullStory or Hotjar, OpenReplay is designed to be fully self-hosted, keeping all user session data within your own infrastructure for complete data ownership and privacy compliance.
Core Capabilities
OpenReplay captures comprehensive session data that goes beyond basic screen recordings:

Session Replay — Pixel-perfect replay of user sessions showing clicks, scrolls, navigation, and interactions. Each session is automatically analyzed using heuristics for easy triage.
DevTools Integration — Captures network activity, console logs, JavaScript errors, Redux/VueX/MobX/NgRx/Pinia/Zustand state changes, GraphQL queries, and Fetch/Axios requests alongside the replay.
Performance Metrics — Records page speed metrics, CPU/memory usage, and Web Vitals for every session.
Assist — Live session viewing and WebRTC-based co-browsing without third-party screen sharing tools.
Spot — A Chrome extension for recording bugs directly from the browser with full technical context included.

Analytics and Search
OpenReplay provides an omni-search feature that lets you filter sessions by user actions, session attributes, or technical events without requiring custom instrumentation. The analytics module surfaces the most impactful issues affecting conversion and revenue, helping teams prioritize fixes based on actual user impact.
Privacy and Security
Fine-grained privacy controls let you choose exactly what to capture, obscure, or ignore. Sensitive data can be masked at the tracker level before it ever reaches your servers. The self-hosted architecture means session data never leaves your cloud infrastructure.
Deployment
OpenReplay supports deployment on major cloud platforms:

AWS, Google Cloud, Azure, DigitalOcean, Scaleway, OVHcloud
Kubernetes with Helm charts
The tracker is a lightweight ~26KB (.br) JavaScript snippet that sends data asynchronously

Integration Ecosystem
OpenReplay integrates with backend logging and monitoring tools including Sentry, Datadog, CloudWatch, Stackdriver, and Elastic. Framework plugins support React, Angular, Vue, Svelte, Next.js, and React Native. The plugin architecture allows extending data capture with custom metadata.
Agent Integration
For AI agents and automation workflows, OpenReplay provides REST APIs for searching sessions, querying analytics data, and managing projects programmatically. Agents can use session replay data to understand user behavior patterns, identify UX issues, and correlate frontend errors with backend logs for automated debugging workflows.
Installation
Deploy using the official scripts for your cloud provider, or use the managed cloud service at app.openreplay.com. The JavaScript tracker is installed via npm:
npm install @openreplay/tracker

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openreplay-self-hosted-session-replay-analytics/)
