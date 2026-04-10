---
title: "Paperless-ngx Document OCR and Archive Management System"
description: "Paperless-ngx is an open source document management system that turns scanned or uploaded paperwork into a searchable archive. It combines OCR-driven ingestion, indexing, tagging, storage, and retrieval for teams that need structured access to documents."
slug: "paperless-ngx-document-ocr-archive-management-system"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/paperless-ngx/paperless-ngx"
---

# Paperless-ngx Document OCR and Archive Management System

Paperless-ngx is an open source document management system that turns scanned or uploaded paperwork into a searchable archive. It combines OCR-driven ingestion, indexing, tagging, storage, and retrieval for teams that need structured access to documents.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install paperless-ngx-document-ocr-archive-management-system
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Paperless-ngx is a community-maintained document management system from the paperless-ngx/paperless-ngx project. Its main job is to transform physical or downloaded documents into a searchable digital archive, making it a practical fit for workflows that need document ingestion, OCR, tagging, and structured retrieval.
The upstream project is the official successor to Paperless and Paperless-ng, and its documentation emphasizes scanning, indexing, and archiving files in a single web application. For automation use cases, that means an agent can watch inbound files, classify them, enrich metadata, and push them into a consistent archive that remains searchable later. The project also has a public documentation site, a demo instance, active releases, and a current development cadence, which makes it a credible upstream for ASE intake.
This maps well to data extraction and transformation because Paperless-ngx turns raw source documents into queryable records with OCR-backed text, metadata, and archive structure. A skill built around it could support invoice intake, records retention, searchable document vaults, or back-office processing pipelines. The easiest documented deployment path is Docker Compose, which lowers the barrier for teams that want a self-hosted document workflow engine without building one from scratch.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/paperless-ngx-document-ocr-archive-management-system/)
