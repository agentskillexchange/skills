---
name: "Diagnose Paradev host and terminal failures with the doctor skill"
slug: "diagnose-paradev-host-and-terminal-failures-with-the-doctor-skill"
description: "Capture Paradev service, account, host and version evidence, propose one symptom-matched repair, and verify the original failure before escalation."
verification: "security_reviewed"
source: "https://github.com/ParadevAI/Paradev/blob/7b3643f33143bd0d479a90f53125651803b9961d/plugins/superset/skills/doctor/SKILL.md"
author: "ParadevAI"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Diagnose Paradev host and terminal failures with the doctor skill

Capture Paradev service, account, host and version evidence, propose one symptom-matched repair, and verify the original failure before escalation.

## Prerequisites

Paradev desktop app and superset CLI (paradev alias); shell access; existing SSH access only for an affected remote host; optional relevant local service logs

## Installation

Install or set up from the source-backed instructions:

Install the Paradev desktop app from https://github.com/ParadevAI/Paradev/releases/latest and launch it; upstream documents automatic managed skill provisioning at launch. Verify the bundled CLI with superset --version. In Claude Code invoke /superset:doctor with the symptom; other supported agents discover the managed skill under the superset- prefix. Source reviewed at revision 7b3643f33143bd0d479a90f53125651803b9961d. No upstream installation or authenticated runtime test was performed during metadata review.

- Source: https://github.com/ParadevAI/Paradev/blob/7b3643f33143bd0d479a90f53125651803b9961d/plugins/superset/skills/doctor/SKILL.md

## Documentation

- https://docs.paradev.com/skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-paradev-host-and-terminal-failures-with-the-doctor-skill/)
