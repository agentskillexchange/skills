---
title: "Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs"
description: "Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management."
verification: security_reviewed
source: "https://github.com/py-vobject/vobject"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "py-vobject/vobject"
  github_stars: 50
---

# Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs

Tool: vobject

This skill is for agents that need to ingest contact exports instead of leaving them trapped inside .vcf files. vobject is a long-running Python package for parsing and generating vCard and iCalendar data, and the bounded workflow here is clear: read contact files, extract structured fields such as names, emails, phone numbers, addresses, organizations, and notes, normalize them into records another system can validate, and optionally serialize clean vCard output again after cleanup. That makes it useful in migrations, dedup jobs, contact reconciliation, and mailbox or address-book exports that need machine handling before import.

Invoke this skill when the user has exported contacts from a phone, email client, CRM, or directory service and wants downstream automation to classify, merge, validate, or import those records. It is also useful when an agent needs to compare contact snapshots over time or prepare cleaner records before syncing them into another system.

The scope boundary keeps it honest. This is not a CRM, not a sync platform, not a messaging tool, and not a contacts database. It does not decide ownership, perform outreach, or manage user permissions. It handles the narrow but important conversion layer between vCard files and structured contact data. That is a real agent task, and it stays valuable even without naming the underlying package.

Integration points include CRM import pipelines, address-book migrations, dedup and merge routines, validation jobs, and contact cleanup workflows that start with exported files rather than live APIs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs/)
