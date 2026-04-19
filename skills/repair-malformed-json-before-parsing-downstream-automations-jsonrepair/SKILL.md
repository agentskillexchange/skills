---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
description: "Tool used: jsonrepair (josdejong/jsonrepair). This skill is for an agent that sits between messy upstream producers and strict downstream systems. The agent takes malformed JSON or JSON-like text, runs it through jsonrepair, and produces a valid JSON document that can be parsed, validated, or stored safely by the next stage of the workflow. The job-to-be-done is specific: recover structured data from near-valid JSON so an automation does not fail on avoidable syntax issues. Invoke this when the user has unreliable JSON emitters in the loop, especially LLM output, copied config snippets, logs that include JSON with small syntax defects, or integration payloads that are consistently almost correct. This is a good fit when the agent must salvage the payload, continue processing, and optionally hand the repaired object to a schema validator, ETL step, queue consumer, or API client. It is not the right tool when the source data is fundamentally ambiguous, when the user needs a full JSON schema enforcement layer, or when the proper fix is to correct the producing system. The scope boundary keeps this from being a plain package listing. The point is not “here is a JSON library.” The point is that an agent can use jsonrepair as a bounded recovery step inside a larger automation, then continue with parsing, validation, enrichment, or routing. Typical integration points include Node.js scripts, ingestion pipelines, LLM guardrails, pre-parse middleware, and command-line repair steps before data is committed downstream."
source: "https://github.com/josdejong/jsonrepair"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "josdejong/jsonrepair"
  github_stars: 2297
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Tool used: jsonrepair (josdejong/jsonrepair). This skill is for an agent that sits between messy upstream producers and strict downstream systems. The agent takes malformed JSON or JSON-like text, runs it through jsonrepair, and produces a valid JSON document that can be parsed, validated, or stored safely by the next stage of the workflow. The job-to-be-done is specific: recover structured data from near-valid JSON so an automation does not fail on avoidable syntax issues. Invoke this when the user has unreliable JSON emitters in the loop, especially LLM output, copied config snippets, logs that include JSON with small syntax defects, or integration payloads that are consistently almost correct. This is a good fit when the agent must salvage the payload, continue processing, and optionally hand the repaired object to a schema validator, ETL step, queue consumer, or API client. It is not the right tool when the source data is fundamentally ambiguous, when the user needs a full JSON schema enforcement layer, or when the proper fix is to correct the producing system. The scope boundary keeps this from being a plain package listing. The point is not “here is a JSON library.” The point is that an agent can use jsonrepair as a bounded recovery step inside a larger automation, then continue with parsing, validation, enrichment, or routing. Typical integration points include Node.js scripts, ingestion pipelines, LLM guardrails, pre-parse middleware, and command-line repair steps before data is committed downstream.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
