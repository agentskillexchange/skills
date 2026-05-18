---
name: "Decode, inspect, sign, and verify JWTs while debugging auth flows with jwt-cli"
slug: "decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli"
description: "Decode JWTs, inspect claims, and verify or sign tokens with local keys during auth debugging and test setup."
github_stars: 1464
verification: "listed"
source: "https://github.com/mike-engel/jwt-cli"
author: "mike-engel"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mike-engel/jwt-cli"
  github_stars: 1464
  npm_package: "jwt-cli"
  npm_weekly_downloads: 3419
---

# Decode, inspect, sign, and verify JWTs while debugging auth flows with jwt-cli

Decode JWTs, inspect claims, and verify or sign tokens with local keys during auth debugging and test setup.

## Prerequisites

jwt-cli

## Installation

Use the upstream install or setup path that matches your environment:
- brew install mike-engel/jwt-cli/jwt-cli
- cargo install jwt-cli
- cargo test
- cargo run -- help

Requirements and caveats from upstream:
- Currently the underlying token encoding and decoding library, [jsonwebtoken](https://github.com/Keats/jsonwebtoken), doesn't support the SEC1 private key format and requires a conversion to the PKCS8 type. You can rea...

Basic usage or getting-started notes:
- You may also install the binary from the [release](https://github.com/mike-engel/jwt-cli/releases) page, if you're unable to use Homebrew or Cargo install methods below.
- Only 64bit linux, macOS, and Windows targets are pre-built. Sorry if you're not on one of those! You'll need to build it from the source. See the [contributing](#contributing) section on how to install and build the p...
- You should install it somewhere in your $PATH. For Linux and macOS, a good place is generally /usr/local/bin. For Windows, there isn't a good place by default :(.

- Source: https://github.com/mike-engel/jwt-cli
- Extracted from upstream docs: https://raw.githubusercontent.com/mike-engel/jwt-cli/HEAD/README.md

## Documentation

- https://github.com/mike-engel/jwt-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli/)
