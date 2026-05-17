---
name: "Sign agent-made Git commits with gitsign"
slug: "sign-agent-made-git-commits-with-gitsign"
description: "Apply keyless Sigstore-backed signatures to Git commits so automated changes retain verifiable provenance."
github_stars: 1079
verification: "security_reviewed"
source: "https://github.com/sigstore/gitsign"
author: "Sigstore maintainers"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sigstore/gitsign"
  github_stars: 1079
---

# Sign agent-made Git commits with gitsign

Apply keyless Sigstore-backed signatures to Git commits so automated changes retain verifiable provenance.

## Prerequisites

git, gitsign

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install `gitsign`, configure Git to use it for commit signing, then create commits normally and verify the signatures in Git or your forge UI.
```

## Documentation

- https://github.com/sigstore/gitsign

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sign-agent-made-git-commits-with-gitsign/)
