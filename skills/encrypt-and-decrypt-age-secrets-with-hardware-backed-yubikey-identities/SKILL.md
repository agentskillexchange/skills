---
title: "Encrypt and decrypt age secrets with hardware-backed YubiKey identities"
description: "Use age-plugin-yubikey when an agent needs age encryption tied to a physical YubiKey identity instead of software-only keys."
verification: "listed"
source: "https://github.com/str4d/age-plugin-yubikey"
author: "str4d"
publisher_type: "open_source_project"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "str4d/age-plugin-yubikey"
  github_stars: 881
---

# Encrypt and decrypt age secrets with hardware-backed YubiKey identities

Use age-plugin-yubikey when an agent needs age encryption tied to a physical YubiKey identity instead of software-only keys.

## Prerequisites

age, age-plugin-yubikey, and a configured YubiKey with supported credentials

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install age and age-plugin-yubikey, initialize the YubiKey-backed age identity described in the project docs, then use standard age commands with the plugin-enabled recipient or identity flow.
```

## Documentation

- https://github.com/str4d/age-plugin-yubikey#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/encrypt-and-decrypt-age-secrets-with-hardware-backed-yubikey-identities/)
