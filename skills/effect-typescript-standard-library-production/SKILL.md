---
name: "Effect TypeScript Standard Library for Production Applications"
description: "Effect is a comprehensive TypeScript standard library that provides structured concurrency, typed errors, dependency injection, schema validation, and observability — replacing dozens of individual packages with one cohesive, type-safe framework for building production-grade applications."
verification: security_reviewed
source: "https://github.com/Effect-TS/effect"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Effect-TS/effect"
  github_stars: 13778
---

# Effect TypeScript Standard Library for Production Applications

Effect is an open-source TypeScript library that serves as a batteries-included standard library for building production applications. Created by the Effect-TS organization and licensed under MIT, it brings ideas from functional programming languages like Scala (ZIO) and Haskell to the TypeScript ecosystem, providing structured concurrency, typed error handling, dependency injection, schema validation, HTTP clients and servers, CLI argument parsing, and OpenTelemetry observability — all in a single, composable package.
Core Abstractions
The central type Effect<A, E, R> represents a computation that produces a value of type A, may fail with an error of type E, and requires a context of type R. This three-parameter type tracks success values, expected errors, and dependencies at the type level, eliminating entire categories of runtime bugs. Effects compose via pipe, flatMap, map, and generators (Effect.gen), providing a familiar async/await-like syntax with full type safety.
Key Modules
Effect ships with @effect/schema for runtime validation and encoding/decoding between types, @effect/platform for HTTP client/server abstractions, @effect/cli for building type-safe command-line tools, @effect/sql for database access, and @effect/opentelemetry for automatic tracing and metrics. The Layer system provides compile-time verified dependency injection, ensuring all service dependencies are satisfied before the application runs.
Agent Integration Points
For AI coding agents, Effect provides a structured way to handle complex application logic. An agent can use Effect's typed error channels to build workflows where every failure path is explicitly modeled, use Stream for processing large datasets with backpressure, use Schedule for retry policies, and use Fiber for structured concurrency. The schema module replaces Zod with a system that handles both validation and serialization, reducing the number of libraries an agent needs to coordinate.
Installation
Install via npm: npm install effect. The core package includes all fundamental modules. Platform-specific packages like @effect/platform-node or @effect/platform-bun provide runtime adapters. Effect requires TypeScript 5.4+ with strict: true and exactOptionalPropertyTypes: true for full type-level guarantees.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/effect-typescript-standard-library-production/)
