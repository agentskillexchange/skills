---
title: "Normalize international phone numbers into E.164 before CRM imports or messaging workflows"
description: "Use libphonenumber-js when an agent needs to clean messy phone-number input, validate it against country rules, and return a stable E.164 value before storing contacts or triggering downstream messaging. The skill is about normalization and validation, not telephony delivery, call routing, or campaign orchestration."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/libphonenumber-js"
author: "catamphetamine"
publisher_type: "Individual Maintainer"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  npm_package: "libphonenumber-js"
  npm_weekly_downloads: 15571336
---

# Normalize international phone numbers into E.164 before CRM imports or messaging workflows

Use libphonenumber-js when an agent needs to clean messy phone-number input, validate it against country rules, and return a stable E.164 value before storing contacts or triggering downstream messaging. The skill is about normalization and validation, not telephony delivery, call routing, or campaign orchestration.

## Prerequisites

Node.js and npm

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install libphonenumber-js --save
```

## Documentation

- https://github.com/catamphetamine/libphonenumber-js#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-international-phone-numbers-into-e164-before-crm-imports-or-messaging-workflows/)
