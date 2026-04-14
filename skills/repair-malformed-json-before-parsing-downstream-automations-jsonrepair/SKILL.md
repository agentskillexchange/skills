---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
verification: security_reviewed
source: "https://github.com/josdejong/jsonrepair"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Tool used: jsonrepair (josdejong/jsonrepair).

This skill is for an agent that sits between messy upstream producers and strict downstream systems. The agent takes malformed JSON or JSON-like text, runs it through jsonrepair, and produces a valid JSON document that can be parsed, validated, or stored safely by the next stage of the workflow. The job-to-be-done is specific: recover structured data from near-valid JSON so an automation does not fail on avoidable syntax issues.

Invoke this when the user has unreliable JSON emitters in the loop, especially LLM output, copied config snippets, logs that include JSON with small syntax defects, or integration payloads that are consistently almost correct. This is a good fit when the agent must salvage the payload, continue processing, and optionally hand the repaired object to a schema validator, ETL step, queue consumer, or API client. It is not the right tool when the source data is fundamentally ambiguous, when the user needs a full JSON schema enforcement layer, or when the proper fix is to correct the producing system.

The scope boundary keeps this from being a plain package listing. The point is not “here is a JSON library.” The point is that an agent can use jsonrepair as a bounded recovery step inside a larger automation, then continue with parsing, validation, enrichment, or routing. Typical integration points include Node.js scripts, ingestion pipelines, LLM guardrails, pre-parse middleware, and command-line repair steps before data is committed downstream.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
