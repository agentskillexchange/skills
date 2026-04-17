---
name: Normalize vCard contact exports into structured contact records before CRM imports
  or dedup jobs
description: Use vobject when an agent receives .vcf contact exports and needs reliable
  parsing into names, emails, phone numbers, organizations, and addresses before import
  or cleanup. This skill is for vCard normalization and serialization, not contact
  sync, outreach, or CRM management.
category: Integrations & Connectors
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/py-vobject/vobject
tool_ecosystem:
  github_repo: py-vobject/vobject
  github_stars: 50
  tool: vobject
---
# Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs
Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs/)
