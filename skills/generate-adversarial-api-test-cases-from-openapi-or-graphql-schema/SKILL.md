---
title: "Generate adversarial API test cases from an OpenAPI or GraphQL schema"
description: "This skill uses Schemathesis , the open source property-based API testing tool for OpenAPI and GraphQL services, to generate high-variance test traffic from a machine-readable schema. An agent invokes it when the goal is not just to call an API, but to actively probe it for crashes, invariant violations, schema mismatches, flaky validation, and 5xx responses that appear only under unusual inputs. The important boundary is that this is not a general API client or generic SDK entry. The agent is performing a narrow operator task: derive many concrete request cases from a declared schema, execute them against a target service or test environment, and convert the findings into actionable defects or CI failures. If the user only wants to consume the API normally, browse docs, or generate a client, this skill is the wrong tool. Use it when you have a schema file or discoverable schema URL, a reachable service under test, and a need for automated bug hunting or regression coverage. It fits API hardening, pre-release verification, and pull request validation. Integration points include CLI runs in CI, Python and pytest-based workflows, GitHub Actions or similar pipelines, and downstream bug report generation. Because the schema is the contract, the agent can also scope its run to specific operations, auth modes, or environments and then summarize only the failing cases that need human attention."
source: "https://github.com/schemathesis/schemathesis"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "schemathesis/schemathesis"
  github_stars: 3214
---

# Generate adversarial API test cases from an OpenAPI or GraphQL schema

This skill uses Schemathesis , the open source property-based API testing tool for OpenAPI and GraphQL services, to generate high-variance test traffic from a machine-readable schema. An agent invokes it when the goal is not just to call an API, but to actively probe it for crashes, invariant violations, schema mismatches, flaky validation, and 5xx responses that appear only under unusual inputs. The important boundary is that this is not a general API client or generic SDK entry. The agent is performing a narrow operator task: derive many concrete request cases from a declared schema, execute them against a target service or test environment, and convert the findings into actionable defects or CI failures. If the user only wants to consume the API normally, browse docs, or generate a client, this skill is the wrong tool. Use it when you have a schema file or discoverable schema URL, a reachable service under test, and a need for automated bug hunting or regression coverage. It fits API hardening, pre-release verification, and pull request validation. Integration points include CLI runs in CI, Python and pytest-based workflows, GitHub Actions or similar pipelines, and downstream bug report generation. Because the schema is the contract, the agent can also scope its run to specific operations, auth modes, or environments and then summarize only the failing cases that need human attention.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-adversarial-api-test-cases-from-openapi-or-graphql-schema/)
