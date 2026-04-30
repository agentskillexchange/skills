---
title: "SOPS Secret File Encryption and Rotation"
description: "SOPS manages encrypted YAML, JSON, ENV, INI, and binary files with KMS, age, and PGP. It is a tight fit for secrets handling, rotation, and encrypted configuration workflows."
verification: "security_reviewed"
source: "https://github.com/getsops/sops"
author: "Getsops"
publisher_type: "Open Source Project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "getsops/sops"
  github_stars: 21476
---

# SOPS Secret File Encryption and Rotation

SOPS manages encrypted YAML, JSON, ENV, INI, and binary files with KMS, age, and PGP. It is a tight fit for secrets handling, rotation, and encrypted configuration workflows.

## Prerequisites

AWS KMS, GCP KMS, Azure Key Vault, age, or PGP depending on encryption backend

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
brew install sops
```

## Documentation

- https://github.com/getsops/sops

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sops-secret-file-encryption-rotation/)
