---
title: "Load-test gRPC services from proto files and reusable request fixtures"
description: "This ASE skill uses ghz to run repeatable gRPC load tests from proto files, protosets, or server reflection. An agent can replay request fixtures at controlled concurrency, capture latency and error rates, and export machine-readable reports for regression checks or performance investigations."
verification: security_reviewed
source: "https://github.com/bojand/ghz"
category:
  - "Runbooks &amp; Diagnostics"
tool_ecosystem:
  github_repo: "bojand/ghz"
  github_stars: 3315
---

# Load-test gRPC services from proto files and reusable request fixtures

This ASE skill uses ghz to run repeatable gRPC load tests from proto files, protosets, or server reflection. An agent can replay request fixtures at controlled concurrency, capture latency and error rates, and export machine-readable reports for regression checks or performance investigations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures/)
