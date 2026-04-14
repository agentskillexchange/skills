---
title: "Paperless-ngx Document OCR and Archive Management System"
description: "Paperless-ngx is an open source document management system that turns scanned or uploaded paperwork into a searchable archive. It combines OCR-driven ingestion, indexing, tagging, storage, and retrieval for teams that need structured access to documents."
verification: security_reviewed
source: "https://github.com/paperless-ngx/paperless-ngx"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "paperless-ngx/paperless-ngx"
  github_stars: 38063
---

# Paperless-ngx Document OCR and Archive Management System

Paperless-ngx is a community-maintained document management system from the paperless-ngx/paperless-ngx project. Its main job is to transform physical or downloaded documents into a searchable digital archive, making it a practical fit for workflows that need document ingestion, OCR, tagging, and structured retrieval.

The upstream project is the official successor to Paperless and Paperless-ng, and its documentation emphasizes scanning, indexing, and archiving files in a single web application. For automation use cases, that means an agent can watch inbound files, classify them, enrich metadata, and push them into a consistent archive that remains searchable later. The project also has a public documentation site, a demo instance, active releases, and a current development cadence, which makes it a credible upstream for ASE intake.

This maps well to data extraction and transformation because Paperless-ngx turns raw source documents into queryable records with OCR-backed text, metadata, and archive structure. A skill built around it could support invoice intake, records retention, searchable document vaults, or back-office processing pipelines. The easiest documented deployment path is Docker Compose, which lowers the barrier for teams that want a self-hosted document workflow engine without building one from scratch.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/paperless-ngx-document-ocr-archive-management-system/)
