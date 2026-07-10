---
title: "Lint X.509 certificates against Web PKI rules with zlint before issuance or rollout"
description: "Check certificates and precertificates for Web PKI standards violations before CA issuance, trust-store submission, or deployment."
verification: "security_reviewed"
source: "https://github.com/zmap/zlint"
author: "zmap"
publisher_type: "open_source_project"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zmap/zlint"
  github_stars: 429
---

# Lint X.509 certificates against Web PKI rules with zlint before issuance or rollout

Check certificates and precertificates for Web PKI standards violations before CA issuance, trust-store submission, or deployment.

## Prerequisites

PEM or DER certificate or precertificate input, zlint CLI or Go library, operator able to interpret lint findings

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install zlint from the upstream repository or releases, then run it against the target certificate or precertificate file.
```

## Documentation

- https://zmap.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-x509-certificates-against-web-pki-rules-with-zlint-before-issuance-or-rollout/)
