---
name: "Collect Unix-like incident-response artifacts into one portable evidence bundle with UAC"
slug: "collect-unix-like-incident-response-artifacts-into-one-portable-evidence-bundle-with-uac"
description: "Capture volatile and persistent Unix-like system artifacts quickly before evidence disappears or responders start changing the host."
github_stars: 1306
verification: "security_reviewed"
source: "https://github.com/tclahr/uac"
author: "tclahr"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tclahr/uac"
  github_stars: 1306
---

# Collect Unix-like incident-response artifacts into one portable evidence bundle with UAC

Capture volatile and persistent Unix-like system artifacts quickly before evidence disappears or responders start changing the host.

## Prerequisites

Shell access to the target Unix-like host, UAC runtime, sufficient privileges for artifact collection, storage location for the output bundle

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install UAC from the upstream repository or release assets, review the available artifact profiles and collection modules, then run the documented collector against the target host and preserve the generated bundle for analysis.
```

## Documentation

- https://github.com/tclahr/uac

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/collect-unix-like-incident-response-artifacts-into-one-portable-evidence-bundle-with-uac/)
