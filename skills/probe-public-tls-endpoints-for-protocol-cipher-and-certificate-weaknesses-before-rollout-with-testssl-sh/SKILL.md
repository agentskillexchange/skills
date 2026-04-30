---
title: "Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh"
description: "Run a thorough TLS preflight against a host before launch, certificate renewal, or incident review."
verification: "listed"
source: "https://github.com/testssl/testssl.sh"
author: "testssl project"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "testssl/testssl.sh"
  github_stars: 8986
---

# Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh

Run a thorough TLS preflight against a host before launch, certificate renewal, or incident review.

## Prerequisites

Shell environment, OpenSSL-compatible networking tools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository or download a release, then run `./testssl.sh <host>` or `./testssl.sh <host>:443` against the target endpoint.
```

## Documentation

- https://testssl.sh/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/)
