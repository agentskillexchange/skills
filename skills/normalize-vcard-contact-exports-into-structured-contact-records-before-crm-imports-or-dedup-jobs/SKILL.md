---
title: "Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs"
description: "Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management."
verification: "security_reviewed"
source: "https://github.com/py-vobject/vobject"
publisher_type: "GitHub Organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "py-vobject/vobject"
  github_stars: 50
---

# Normalize vCard contact exports into structured contact records before CRM imports or dedup jobs

Use vobject when an agent receives .vcf contact exports and needs reliable parsing into names, emails, phone numbers, organizations, and addresses before import or cleanup. This skill is for vCard normalization and serialization, not contact sync, outreach, or CRM management.

## Prerequisites

Python, pip

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install vobject
```

## Documentation

- http://py-vobject.github.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-vcard-contact-exports-into-structured-contact-records-before-crm-imports-or-dedup-jobs/)
