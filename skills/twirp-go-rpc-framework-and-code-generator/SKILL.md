---
title: "Twirp Go RPC Framework and Code Generator"
description: "Twirp is a protobuf-based RPC framework from Twitch that generates Go servers and clients with a simple HTTP transport. It suits agent workflows that need to scaffold service definitions, generate code with protoc plugins, and wire strongly typed RPC endpoints into Go services."
verification: "security_reviewed"
source: "https://github.com/twitchtv/twirp"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "twitchtv/twirp"
  github_stars: 7503
  license: "Apache-2.0"
---

# Twirp Go RPC Framework and Code Generator

Twirp is a lightweight RPC framework built around Protocol Buffers and Go. It gives agents a concrete way to generate service interfaces, client code, and server handlers from .proto definitions without pulling in a heavier distributed-systems stack. The upstream project provides a Go runtime library, a code generator, and installation guidance for protoc, protoc-gen-go, and protoc-gen-twirp.


For agent workflows, that maps cleanly to jobs like defining service contracts, generating boilerplate, validating protobuf layouts, and integrating RPC endpoints into an existing Go module. An agent can inspect a repository for service definitions, add a tools.go file to pin generator versions, install the required generators, run protoc --go_out=. --twirp_out=., and then wire the resulting handlers into HTTP routing. Because Twirp keeps the protocol surface focused, it is especially useful when a team wants typed RPC semantics without the operational overhead of a larger framework.


The upstream docs also make version compatibility explicit, which matters for agent assistance during upgrades. A good Twirp skill can help with generator installation, client/server regeneration after schema edits, compatibility checks for older protobuf APIs, and explanation of how generated files relate to the original service contract. It is a practical fit for code generation, API contract maintenance, and service bootstrap tasks in Go-centric repositories.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twirp-go-rpc-framework-and-code-generator/)
