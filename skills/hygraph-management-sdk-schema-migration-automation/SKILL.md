---
name: Hygraph Management SDK for Schema Migration Automation
description: A source-backed ASE skill for the Hygraph Management SDK, the JavaScript
  package for managing Hygraph project schema through code-first migrations. It is
  a good fit for agent workflows that need repeatable content-model changes, environment-aware
  schema updates, and dry-run migration previews.
verification: security_reviewed
source: https://github.com/hygraph/management-sdk
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
---
# Hygraph Management SDK for Schema Migration Automation

Hygraph Management SDK for Schema Migration Automation is a source-backed ASE skill built on the official @hygraph/management-sdk package published by Hygraph and maintained in the hygraph/management-sdk repository. The SDK is designed to programmatically manage a Hygraph project schema through migrations, including models, fields, locales, stages, enumerations, and other structured content definitions. The upstream README shows a concrete code API for creating migrations, previewing changes with dry runs, and applying them against a specific project environment with an auth token and endpoint.
The job-to-be-done here is controlled content schema evolution. An agent can use this skill to define or update content models in code, create repeatable migrations for new fields and relationships, preview the exact changes before rollout, and apply those changes consistently across environments. That is useful when teams want to automate CMS setup for new projects, manage schema drift between environments, or treat content architecture as part of the same delivery workflow as application code.
Integration points include Node.js build scripts, CI pipelines, repository-managed migration folders, and Hygraph projects that already expose environment endpoints and API access tokens. Because the SDK is a real npm package with official docs, a public GitHub repository, recent enough maintenance, and clear installation and usage guidance, it passes the ASE intake gate as a legitimate tool-backed skill. For ASE, this gives agents a concrete Hygraph automation primitive rather than a generic CMS setup abstraction.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hygraph-management-sdk-schema-migration-automation/)
