---
title: "Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich"
description: "Identify which processes, connections, and remote hosts are actually using bandwidth before you chase the wrong incident hypothesis."
verification: security_reviewed
source: "https://github.com/imsnif/bandwhich"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "imsnif/bandwhich"
  github_stars: 11691
---

# Trace which local processes and hosts are consuming bandwidth during incidents with bandwhich

Use bandwhich when an agent needs a fast, local answer to a narrow incident question: what process or remote host is consuming network bandwidth right now. This is not a generic network monitor or platform card. It is a bounded diagnostic workflow around sniffing one interface, mapping traffic back to processes, and separating process, connection, and address views during live troubleshooting.

Invoke it instead of using a full observability stack when the job is immediate host-level attribution on the machine in front of you. Typical runs inspect one interface, optionally disable reverse DNS for speed, and narrow the view to processes, connections, or remote addresses before escalation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-which-local-processes-and-hosts-are-consuming-bandwidth-during-incidents-with-bandwhich/)
