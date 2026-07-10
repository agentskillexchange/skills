---
title: "Twirp Go RPC Framework and Code Generator"
description: "Twirp is a protobuf-based RPC framework from Twitch that generates Go servers and clients with a simple HTTP transport. It suits agent workflows that need to scaffold service definitions, generate code with protoc plugins, and wire strongly typed RPC endpoints into Go services."
verification: "listed"
source: "https://github.com/twitchtv/twirp"
author: "Twitch"
publisher_type: "Company"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "twitchtv/twirp"
  github_stars: 7503
---

# Twirp Go RPC Framework and Code Generator

Twirp is a protobuf-based RPC framework from Twitch that generates Go servers and clients with a simple HTTP transport. It suits agent workflows that need to scaffold service definitions, generate code with protoc plugins, and wire strongly typed RPC endpoints into Go services.

## Prerequisites

Go, protoc, protoc-gen-go, protoc-gen-twirp

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
go install github.com/twitchtv/twirp/protoc-gen-twirp@latest
```

## Documentation

- https://twitchtv.github.io/twirp/docs/install.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twirp-go-rpc-framework-and-code-generator/)
