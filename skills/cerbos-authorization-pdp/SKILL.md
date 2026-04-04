---
name: "Cerbos Open Source Authorization Policy Decision Point"
description: "Cerbos is an open-core, language-agnostic, scalable authorization solution that makes implementing and managing user permissions simple. It uses context-aware YAML access control policies managed through Git-ops, providing high-availability APIs for dynamic access decisions across applications."
category: "Security & Verification"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/cerbos/cerbos"
---
# Cerbos Open Source Authorization Policy Decision Point

Cerbos is an open-core, language-agnostic, scalable authorization solution that makes implementing and managing user permissions simple. It uses context-aware YAML access control policies managed through Git-ops, providing high-availability APIs for dynamic access decisions across applications.

## Overview

Cerbos is a self-hosted authorization layer available at github.com/cerbos/cerbos that decouples access control logic from application code. Instead of scattering permission checks throughout a codebase, developers define authorization policies as YAML files and deploy Cerbos as a Policy Decision Point (PDP) that applications query at runtime. The PDP runs as a sidecar, service, or serverless function, responding to authorization requests with allow/deny decisions in single-digit milliseconds.

Authorization policies in Cerbos are written in YAML and stored alongside application code in version control. Each policy defines rules for a specific resource type, specifying which roles can perform which actions under what conditions. Conditions can reference any attribute of the principal (user), the resource being accessed, or derived roles computed from the context. This makes it possible to express complex rules like "managers can approve expense reports only for their direct reports" or "users can edit documents they created, but only during business hours" without embedding that logic in application code.

Cerbos provides gRPC and HTTP APIs that accept a principal, resource, and action, then evaluate the matching policy and return a decision. Client SDKs are available for Go, Java, JavaScript, Python, Ruby, Rust, PHP, .NET, and Elixir. The API is stateless — Cerbos does not maintain session data or store user information — which makes it horizontally scalable and simple to deploy in containerized environments.

For agent skills, Cerbos enables agents to enforce fine-grained access control when performing operations on behalf of users. An agent can check whether a user has permission to perform an action before executing it, implement policy-as-code workflows where policy changes are tested and deployed through CI/CD, and validate authorization configurations against test suites using the Cerbos testing framework. The `cerbos compile` command validates policies at build time, catching errors before deployment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cerbos-authorization-pdp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cerbos-authorization-pdp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cerbos-authorization-pdp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cerbos-authorization-pdp -a codex
```

### OpenClaw

```bash
clawhub install cerbos-authorization-pdp
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cerbos-authorization-pdp/)
