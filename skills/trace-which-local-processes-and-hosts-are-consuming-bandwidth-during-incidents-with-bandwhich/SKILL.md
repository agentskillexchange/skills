---
title: "Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich"
description: "Use bandwhich when an agent needs a fast, local answer to a narrow incident question: what process or remote host is consuming network bandwidth right now. This is not a generic network monitor or platform card. It is a bounded diagnostic workflow around sniffing one interface, mapping traffic back to processes, and separating process, connection, and address views during live troubleshooting. Invoke it instead of using a full observability stack when the job is immediate host-level attribution on the machine in front of you. Typical runs inspect one interface, optionally disable reverse DNS for speed, and narrow the view to processes, connections, or remote addresses before escalation."
source: "https://github.com/imsnif/bandwhich"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "imsnif/bandwhich"
  github_stars: 11691
---

# Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich

Use bandwhich when an agent needs a fast, local answer to a narrow incident question: what process or remote host is consuming network bandwidth right now. This is not a generic network monitor or platform card. It is a bounded diagnostic workflow around sniffing one interface, mapping traffic back to processes, and separating process, connection, and address views during live troubleshooting. Invoke it instead of using a full observability stack when the job is immediate host-level attribution on the machine in front of you. Typical runs inspect one interface, optionally disable reverse DNS for speed, and narrow the view to processes, connections, or remote addresses before escalation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich/)
