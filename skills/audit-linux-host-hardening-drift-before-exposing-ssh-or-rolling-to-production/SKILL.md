---
name: "Audit Linux host hardening drift before exposing SSH or rolling to production"
slug: "audit-linux-host-hardening-drift-before-exposing-ssh-or-rolling-to-production"
description: "Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan."
github_stars: 15505
verification: "security_reviewed"
source: "https://github.com/CISOfy/lynis"
author: "CISOfy"
publisher_type: "Company"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "CISOfy/lynis"
  github_stars: 15505
---

# Audit Linux host hardening drift before exposing SSH or rolling to production

Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan.

## Prerequisites

Shell access to the target UNIX-like host, with root or sudo recommended for fuller audit coverage

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/CISOfy/lynis

Requirements and caveats from upstream:
- Article by TechRepublic, considering Lynis a "must-have" tool: [How to quickly audit a Linux system from the command line](http://www.techrepublic.com/article/how-to-quickly-audit-a-linux-system-from-the-command-line/)

Basic usage or getting-started notes:
- There are multiple options available to install Lynis.
- ### Software package
- For systems running Linux, BSD, and macOS, there is typically a package available. This is the preferred method of obtaining Lynis, as it is quick to install and easy to update. The Lynis project itself also provides...

- Source: https://github.com/CISOfy/lynis
- Extracted from upstream docs: https://raw.githubusercontent.com/CISOfy/lynis/HEAD/README.md

## Documentation

- https://cisofy.com/documentation/lynis/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-linux-host-hardening-drift-before-exposing-ssh-or-rolling-to-production/)
