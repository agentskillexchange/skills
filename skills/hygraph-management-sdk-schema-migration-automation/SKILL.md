---
name: "Hygraph Management SDK for Schema Migration Automation"
slug: "hygraph-management-sdk-schema-migration-automation"
description: "A source-backed ASE skill for the Hygraph Management SDK, the JavaScript package for managing Hygraph project schema through code-first migrations. It is a good fit for agent workflows that need repeatable content-model changes, environment-aware schema updates, and dry-run migration previews."
github_stars: 51
verification: "listed"
source: "https://github.com/hygraph/management-sdk"
author: "Hygraph"
publisher_type: "Company"
category: "WordPress & CMS"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hygraph/management-sdk"
  github_stars: 51
---

# Hygraph Management SDK for Schema Migration Automation

A source-backed ASE skill for the Hygraph Management SDK, the JavaScript package for managing Hygraph project schema through code-first migrations. It is a good fit for agent workflows that need repeatable content-model changes, environment-aware schema updates, and dry-run migration previews.

## Prerequisites

Node.js, a Hygraph auth token, and a Hygraph environment endpoint

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @hygraph/management-sdk --save-dev
- To update the Management API schema this SDK depends on you must run npm run generate.

Requirements and caveats from upstream:
- const { newMigration, FieldType } = require("@hygraph/management-sdk");
- const { newMigration } = require("@hygraph/management-sdk");
- const { FieldType } = require("@hygraph/management-sdk");

Basic usage or getting-started notes:
- js
- const migration = newMigration({ endpoint: "...", authToken: "..." });
- const author = migration.createModel({

- Source: https://github.com/hygraph/management-sdk
- Extracted from upstream docs: https://raw.githubusercontent.com/hygraph/management-sdk/HEAD/README.md

## Documentation

- https://hygraph.com/docs/api-reference/developer-tools/management-sdk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hygraph-management-sdk-schema-migration-automation/)
