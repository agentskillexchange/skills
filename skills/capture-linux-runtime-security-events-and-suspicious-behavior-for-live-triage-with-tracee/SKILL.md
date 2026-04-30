---
title: "Capture Linux runtime security events and suspicious behavior for live triage with Tracee"
description: "Watch live Linux and container activity through eBPF so you can triage suspicious runtime behavior before it disappears into guesswork."
verification: "listed"
source: "https://github.com/aquasecurity/tracee"
author: "Aqua Security"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "aquasecurity/tracee"
  github_stars: 4468
---

# Capture Linux runtime security events and suspicious behavior for live triage with Tracee

Watch live Linux and container activity through eBPF so you can triage suspicious runtime behavior before it disappears into guesswork.

## Prerequisites

Linux host or Kubernetes environment with the required kernel support, Tracee runtime or container image, elevated access to collect eBPF events, and access to the target system or cluster

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Tracee from the upstream binary, container, Helm chart, or package path documented by the project, confirm the host or cluster meets the kernel and privilege requirements, then run Tracee with the documented event or rule filters for the target environment.
```

## Documentation

- https://aquasecurity.github.io/tracee/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-linux-runtime-security-events-and-suspicious-behavior-for-live-triage-with-tracee/)
