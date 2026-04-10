---
name: "Audit OpenClaw host security posture and hardening gaps"
description: "This skill uses OpenClaw's healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
verification: listed
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# Audit OpenClaw host security posture and hardening gaps

Tool name: OpenClaw healthcheck skill.
This entry is about a very specific operator job: auditing the machine that runs OpenClaw, identifying security gaps, and producing a staged remediation plan that preserves access. The upstream source is not a generic security product card. It defines a bounded agent behavior: establish context about the host, run read-only checks, run openclaw security audit and openclaw update status, compare the current state to the user's risk tolerance, then propose exact next steps with rollback notes and confirmation points. That makes it skill-shaped instead of a plain platform listing.
A user should invoke this when they want the assistant to act like a careful operator on a laptop, workstation, Pi, or VPS that already runs OpenClaw. Examples include reviewing SSH exposure before opening remote access, checking whether firewall and update settings match a target posture, or preparing a safer baseline after first install. The skill matters because the normal product experience does not automatically perform this multi-step audit, ask for the right approvals, or convert findings into a human-checked hardening plan.
The scope boundary is clear. This is not a general security suite, not a vulnerability database, and not an agent that blindly hardens every machine. It is specifically for assessing and tightening the host that runs OpenClaw, with approval required before state-changing actions. Integration points are the OpenClaw CLI, host networking and firewall status, SSH or local-console access paths, backup status, and optional Gateway cron scheduling for recurring audits after the first review. If you hid the OpenClaw name, the entry would still describe a real operator task: inspect an assistant host, measure exposure, and guide safe remediation without locking the user out.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
