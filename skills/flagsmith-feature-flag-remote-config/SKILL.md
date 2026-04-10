---
name: "Flagsmith Open Source Feature Flag and Remote Config Platform"
description: "Flagsmith is an open-source feature flagging and remote configuration platform. It enables teams to safely roll out features, run A/B tests, and manage remote config across web, mobile, and server-side applications with granular user segmentation."
verification: security_reviewed
source: "https://github.com/Flagsmith/flagsmith"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Flagsmith/flagsmith"
  github_stars: 6290
---

# Flagsmith Open Source Feature Flag and Remote Config Platform

Flagsmith is an open-source feature flag and remote configuration service built with Python and React. It provides a complete platform for managing feature flags, remote config, and A/B testing across environments, users, and user segments. The project is available under the BSD-3-Clause license and can be self-hosted via Docker or used as a managed SaaS.
Core Capabilities
Flagsmith allows development teams to wrap code sections with feature flags and toggle them on or off without redeploying. This decouples feature releases from code deployments, enabling safer rollouts and instant rollbacks. The platform supports boolean flags, multivariate flags with percentage-based splits, and remote config values that can be changed at runtime.
User Segmentation and Targeting
The segmentation engine lets teams define rules based on user traits (e.g., plan type, country, device) and target specific groups with different flag states. This is essential for beta testing programs, gradual rollouts, and A/B experiments where different user cohorts need different experiences.
SDK Ecosystem
Flagsmith provides official SDKs for 15+ languages and frameworks including JavaScript/TypeScript, Python, Ruby, Go, Java, .NET, Flutter, React Native, iOS (Swift), and Android (Kotlin). Server-side SDKs support local evaluation mode for zero-latency flag checks without network calls. Client-side SDKs fetch flags from the Flagsmith Edge API with built-in caching.
Integration Points
The platform integrates with analytics and monitoring tools including Segment, Amplitude, Mixpanel, Heap, Rudderstack, Datadog, and New Relic. Flag change events are automatically forwarded to connected analytics services, enabling teams to correlate feature releases with metrics changes. Webhook support allows custom integrations with CI/CD pipelines and notification systems.
Self-Hosting and Architecture
Self-hosting is straightforward with the official Docker image. A single docker-compose up command bootstraps the full stack including the API server, admin dashboard, and PostgreSQL database. The architecture supports horizontal scaling with multiple API instances behind a load balancer. Enterprise deployments can use the Flagsmith Edge Proxy for sub-millisecond local evaluation.
Organisation Management
Flagsmith supports multi-organisation, multi-project structures with role-based access control. Teams can create separate environments (development, staging, production) with independent flag states. Audit logs track every flag change with user attribution and timestamps.
Agent Integration Potential
AI agents can use the Flagsmith REST API to check feature flags before executing specific workflows, enable gradual rollout of new agent capabilities, and dynamically configure agent behavior through remote config values. The API supports both server-side evaluation (for backend agents) and client-side identity-based evaluation (for user-facing agents).

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/flagsmith-feature-flag-remote-config/)
