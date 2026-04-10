---
name: "Unkey Open Source API Key Management and Rate Limiting Platform"
description: "Unkey is an open-source developer platform for managing API keys, rate limiting, and usage analytics. It provides a fast, globally distributed key verification system that integrates into any API with minimal code changes."
verification: security_reviewed
source: "https://github.com/unkeyed/unkey"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "unkeyed/unkey"
  github_stars: 5224
---

# Unkey Open Source API Key Management and Rate Limiting Platform

Unkey is an open-source API management platform built for modern developer workflows. It provides three core capabilities: API key management, rate limiting, and usage analytics — all accessible through a clean SDK and REST API.
API Key Management
Unkey handles the full lifecycle of API keys: creation, verification, revocation, and expiration. Keys are verified at the edge with sub-millisecond latency through a globally distributed architecture. Each key can carry custom metadata, be scoped to specific permissions, and have configurable expiration dates. The platform supports temporary keys, key rotation, and bulk operations.
Rate Limiting
The built-in rate limiter supports sliding window, fixed window, and token bucket algorithms. Rate limits can be attached to individual keys or applied globally. The system is designed for distributed environments where traditional in-memory rate limiters fall short, using consistent hashing across edge nodes to maintain accuracy without a single point of failure.
Usage Analytics
Every key verification generates usage data that Unkey aggregates into queryable analytics. Developers can track verification counts, error rates, and usage patterns per key, per API, or across their entire platform. This data feeds into dashboards and can be exported for billing or compliance purposes.
Developer Experience
Integration starts with a single npm package (@unkey/api) or direct REST API calls. The TypeScript SDK provides full type safety and supports both Node.js and edge runtime environments. Unkey also offers official SDKs for Python, Go, and Rust. The platform can be self-hosted or used as a managed cloud service at unkey.com.
Architecture
Unkey is built with Go for its core services, with a Next.js dashboard and TypeScript SDK. The project uses Bazel for build orchestration and maintains comprehensive API documentation. It is actively developed with over 5,000 GitHub stars and a growing contributor community. The platform is designed as an open-source alternative to Kong, Zuplo, and Apigee for API key management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/unkey-api-key-management-rate-limiting/)
