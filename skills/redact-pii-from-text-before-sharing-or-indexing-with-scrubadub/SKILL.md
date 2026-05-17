---
name: "Redact PII from text before sharing or indexing with scrubadub"
slug: "redact-pii-from-text-before-sharing-or-indexing-with-scrubadub"
description: "Use scrubadub when an agent needs to strip emails, phone numbers, names, and similar sensitive text before sending content to external systems or search indexes."
github_stars: 421
verification: "security_reviewed"
source: "https://github.com/LeapBeyond/scrubadub"
author: "LeapBeyond"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "LeapBeyond/scrubadub"
  github_stars: 421
---

# Redact PII from text before sharing or indexing with scrubadub

Use scrubadub when an agent needs to strip emails, phone numbers, names, and similar sensitive text before sending content to external systems or search indexes.

## Prerequisites

Python and scrubadub, plus any text source the agent needs to sanitize.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install scrubadub`, then run its cleaners in preprocessing steps before text is shared externally, indexed, or passed into downstream LLM workflows.
```

## Documentation

- https://scrubadub.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redact-pii-from-text-before-sharing-or-indexing-with-scrubadub/)
