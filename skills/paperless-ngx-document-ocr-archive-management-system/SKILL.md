---
title: "Paperless-ngx Document OCR and Archive Management System"
description: "Paperless-ngx is a community-maintained document management system from the paperless-ngx/paperless-ngx project. Its main job is to transform physical or downloaded documents into a searchable digital archive, making it a practical fit for workflows that need document ingestion, OCR, tagging, and structured retrieval.\nThe upstream project is the official successor to Paperless and Paperless-ng, and its documentation emphasizes scanning, indexing, and archiving files in a single web application. For automation use cases, that means an agent can watch inbound files, classify them, enrich metadata, and push them into a consistent archive that remains searchable later. The project also has a public documentation site, a demo instance, active releases, and a current development cadence, which makes it a credible upstream for ASE intake.\nThis maps well to data extraction and transformation because Paperless-ngx turns raw source documents into queryable records with OCR-backed text, metadata, and archive structure. A skill built around it could support invoice intake, records retention, searchable document vaults, or back-office processing pipelines. The easiest documented deployment path is Docker Compose, which lowers the barrier for teams that want a self-hosted document workflow engine without building one from scratch."
verification: security_reviewed
source: "https://github.com/paperless-ngx/paperless-ngx"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/paperless-ngx-document-ocr-archive-management-system
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/paperless-ngx-document-ocr-archive-management-system` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/paperless-ngx-document-ocr-archive-management-system/)
