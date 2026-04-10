---
name: "PostHog Product Analytics and Feature Flags SDK"
description: "Use PostHog to capture product analytics events, identify users, evaluate feature flags, and route experimentation data into agent or application workflows. This skill gives an agent a concrete implementation path for instrumentation, event tracking, and flag-driven behavior using the real PostHog SDK."
verification: security_reviewed
source: "https://github.com/PostHog/posthog-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "posthog/posthog-js"
  github_stars: 531
  ase_npm_package: "posthog-js"
  npm_weekly_downloads: 4321251
---

# PostHog Product Analytics and Feature Flags SDK

PostHog is a product analytics and feature flag platform that many engineering teams use for event capture, user identification, experiments, and progressive rollout. A skill based on PostHog and its SDK is useful when the job-to-be-done is operational telemetry: instrumenting events, evaluating feature flags, understanding usage patterns, or shipping controlled behavior changes into an agentic or web application workflow.
A solid PostHog skill would initialize the SDK, authenticate with project keys, emit events with properties, identify users or groups, fetch or evaluate feature flags, and return structured outputs such as event payloads, flag states, cohort signals, or rollout decisions. It can also feed downstream automations like conversion reporting, workflow branching, onboarding triggers, or release gating. For agent systems, that means an agent can alter behavior based on live flags, log important actions for analysis, and emit telemetry that product teams can actually use.
Important integration points include the PostHog JS or server SDK, event schema design, identity stitching, feature flags, experiments, cohorts, and ingestion endpoints. Technical terms include event capture, distinct IDs, group analytics, exposure logging, rollout percentage, payload enrichment, and analytics pipelines. This makes the skill a concrete source-backed reference for implementing PostHog in real systems, not a generic “analytics helper” with fuzzy scope.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/posthog-product-analytics-and-feature-flags-sdk/)
