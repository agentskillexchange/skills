---
title: "Normalize raw CLI output into JSON for reliable downstream parsing and automation"
description: "Uses jc to turn command output and supported file formats into structured JSON so an agent can filter, diff, validate, and store results without brittle regex parsing. Best when a workflow already depends on standard CLI tools but needs machine-readable output for the next step."
verification: "security_reviewed"
source: "https://github.com/kellyjonbrazil/jc"
category: ["Data Extraction &amp; Transformation"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "kellyjonbrazil/jc"
  github_stars: 8573
---

# Normalize raw CLI output into JSON for reliable downstream parsing and automation

Uses jc to turn command output and supported file formats into structured JSON so an agent can filter, diff, validate, and store results without brittle regex parsing. Best when a workflow already depends on standard CLI tools but needs machine-readable output for the next step.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-cli-output-into-json-for-reliable-agent-automation/)
