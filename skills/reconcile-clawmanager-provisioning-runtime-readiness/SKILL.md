---
name: "Reconcile ClawManager Provisioning Operations with Runtime Readiness"
slug: "reconcile-clawmanager-provisioning-runtime-readiness"
description: "Inspect an existing provisioning operation and its owner-scoped instance through the Northbound API, distinguishing operation success from runtime availability before handoff."
github_stars: 1889
verification: "security_reviewed"
source: "https://github.com/Yuan-lab-LLM/ClawManager"
author: "Yuan-lab-LLM"
publisher_type: "open_source"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Yuan-lab-LLM/ClawManager"
  github_stars: 1889
---

# Reconcile ClawManager Provisioning Operations with Runtime Readiness

Inspect an existing provisioning operation and its owner-scoped instance through the Northbound API, distinguishing operation success from runtime availability before handoff.

## Prerequisites

Existing ClawManager deployment and Northbound gateway; HTTPS JSON client; authorized Northbound session; applicable instance-read scope

## Installation

Install or set up from the source-backed instructions:

Use an administrator-provisioned ClawManager installation with the separate Northbound gateway enabled. Follow the pinned Northbound API guide for gateway/Core mTLS deployment and one-time JWE session setup; this skill requires no new runtime or package installation. Supply the approved HTTPS base URL and existing operation/instance identifiers, verify auth/me and read scopes, then use only the documented GET endpoints for reconciliation. Do not deploy the platform as part of invoking this workflow.

- Source: https://github.com/Yuan-lab-LLM/ClawManager

## Documentation

- https://github.com/Yuan-lab-LLM/ClawManager/blob/33a232290789a598995d7b7ec4e801bea4f4d108/docs/northbound-api-guide.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reconcile-clawmanager-provisioning-runtime-readiness/)
