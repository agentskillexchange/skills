---
title: "Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs"
description: "Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management."
verification: "security_reviewed"
source: "https://github.com/py-vobject/vobject"
category: ["Integrations &amp; Connectors"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "py-vobject/vobject"
  github_stars: 50
---

# Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs

Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs/)
