---
name: "Pulumi Component Resource Scaffolder"
description: "Scaffolds Pulumi multi-language component resources in TypeScript, Python, and Go with auto-generated SDKs. Creates reusable infrastructure abstractions with proper input/output typing, resource options, and Pulumi schema definitions."
category: "Templates & Workflows"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pulumi-component-resource-scaffolder/"
---

# Pulumi Component Resource Scaffolder

Scaffolds Pulumi multi-language component resources in TypeScript, Python, and Go with auto-generated SDKs. Creates reusable infrastructure abstractions with proper input/output typing, resource options, and Pulumi schema definitions.

## Overview

Overview

The Pulumi Component Resource Scaffolder skill enables agents to create reusable, multi-language infrastructure components using Pulumi’s Component Resource model. Unlike single-resource definitions, component resources encapsulate multiple child resources into a single logical unit — for example, a VPC component that creates subnets, route tables, NAT gateways, and security groups as a single deployable abstraction with a clean input/output interface.

How It Works

The agent generates a Pulumi component by extending `pulumi.ComponentResource` in the target language. For TypeScript, it creates a class with typed `Args` interface inputs and registered output properties. The constructor calls `super(type, name, {}, opts)` and instantiates child resources with `{ parent: this }` to establish the resource hierarchy. The skill also generates a `schema.json` file conforming to the Pulumi Package Schema specification, enabling automatic SDK generation for Python, Go, .NET, and Java via `pulumi package gen-sdk`.

Output and Integration

Produces a complete component package structure: `provider/cmd/pulumi-resource-<name>/main.go` for the provider binary, `sdk/nodejs/` and `sdk/python/` directories with generated type-safe SDKs, and example Pulumi programs in `examples/` demonstrating component usage. Handles resource options including `dependsOn`, `protect`, `deleteBeforeReplace`, and `transformations`. Generates unit tests using `pulumi.runtime.setMocks()` for TypeScript and `pulumi.runtime.set_mocks()` for Python. Supports publishing to the Pulumi Registry or private package feeds via npm and PyPI. All generated code follows Pulumi’s best practices for resource naming, auto-naming, and stack reference patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pulumi-component-resource-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pulumi-component-resource-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pulumi-component-resource-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pulumi-component-resource-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install pulumi-component-resource-scaffolder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pulumi-component-resource-scaffolder/
