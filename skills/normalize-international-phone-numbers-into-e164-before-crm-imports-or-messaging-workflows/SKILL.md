---
title: "Normalize international phone numbers into E.164 before CRM imports or messaging workflows"
description: "Tool: libphonenumber-js. This skill lets an agent take raw phone-number input from forms, CSV exports, scraped datasets, or CRM records and turn it into a normalized value that downstream systems can trust. The core job is simple but important: parse the number, apply country-aware validation rules, and emit a stable representation such as E.164 so later steps do not fail because one record says (213) 373-4253 and another says +1 213 373 4253 . When to use it: invoke this skill before importing contacts, deduplicating lead lists, syncing data between CRMs, validating signup forms, or preparing outbound SMS or voice workflows. In those cases, using the product normally would mean hand-cleaning spreadsheet columns, guessing country defaults, or relying on brittle regex checks that miss valid international formats. An agent using libphonenumber-js can standardize the data, flag impossible numbers, and pass cleaner records to the next step. Scope boundary: this is not a messaging API, telephony platform, call-routing system, or customer-engagement suite. It does not send SMS messages, buy numbers, or manage campaigns. Its boundary is much tighter: parse, validate, and format personal phone numbers so downstream systems receive consistent identifiers. Integration points: form validation, CSV and spreadsheet imports, CRM deduplication jobs, contact enrichment pipelines, and outbound messaging preparation. Upstream evidence includes the official npm package, the maintained source repository, MIT licensing, and strong recent package adoption."
source: "https://www.npmjs.com/package/libphonenumber-js"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "libphonenumber-js"
  npm_weekly_downloads: 15571336
---

# Normalize international phone numbers into E.164 before CRM imports or messaging workflows

Tool: libphonenumber-js. This skill lets an agent take raw phone-number input from forms, CSV exports, scraped datasets, or CRM records and turn it into a normalized value that downstream systems can trust. The core job is simple but important: parse the number, apply country-aware validation rules, and emit a stable representation such as E.164 so later steps do not fail because one record says (213) 373-4253 and another says +1 213 373 4253 . When to use it: invoke this skill before importing contacts, deduplicating lead lists, syncing data between CRMs, validating signup forms, or preparing outbound SMS or voice workflows. In those cases, using the product normally would mean hand-cleaning spreadsheet columns, guessing country defaults, or relying on brittle regex checks that miss valid international formats. An agent using libphonenumber-js can standardize the data, flag impossible numbers, and pass cleaner records to the next step. Scope boundary: this is not a messaging API, telephony platform, call-routing system, or customer-engagement suite. It does not send SMS messages, buy numbers, or manage campaigns. Its boundary is much tighter: parse, validate, and format personal phone numbers so downstream systems receive consistent identifiers. Integration points: form validation, CSV and spreadsheet imports, CRM deduplication jobs, contact enrichment pipelines, and outbound messaging preparation. Upstream evidence includes the official npm package, the maintained source repository, MIT licensing, and strong recent package adoption.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-international-phone-numbers-into-e164-before-crm-imports-or-messaging-workflows/)
