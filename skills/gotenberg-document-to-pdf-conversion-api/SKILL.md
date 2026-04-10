---
title: "Gotenberg Document-to-PDF Conversion API"
description: "Gotenberg is a Docker-based API for converting HTML, URLs, Markdown, and office documents into PDF, then performing post-processing tasks such as merge, split, watermark, metadata edits, and encryption. It wraps Chromium, LibreOffice, and PDF engines behind a single HTTP interface."
slug: "gotenberg-document-to-pdf-conversion-api"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/gotenberg/gotenberg"
---

# Gotenberg Document-to-PDF Conversion API

Gotenberg is a Docker-based API for converting HTML, URLs, Markdown, and office documents into PDF, then performing post-processing tasks such as merge, split, watermark, metadata edits, and encryption. It wraps Chromium, LibreOffice, and PDF engines behind a single HTTP interface.

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
clawhub install gotenberg-document-to-pdf-conversion-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Gotenberg is a developer-friendly API for document conversion and PDF post-processing. The project runs as a Docker image and exposes HTTP endpoints that accept files or URLs over multipart/form-data, then returns PDFs or derived outputs. The official documentation and README highlight three big capability groups: Chromium-based rendering for HTML, URLs, and Markdown; LibreOffice-driven conversion for office formats such as DOCX, XLSX, and PPTX; and PDF engine endpoints for merging, splitting, rotating, watermarking, flattening, encrypting, and manipulating metadata.
This gives it a concrete job to be done inside ASE: turn inbound documents or web pages into printable PDFs, automate office-to-PDF conversion, and run downstream PDF operations in server-side workflows without maintaining bespoke LibreOffice or browser automation wrappers. Gotenberg also supports features that matter in production pipelines, including waiting for dynamic content before rendering, custom headers and cookies for authenticated pages, PDF/A and PDF/UA options, screenshots, and direct cloud-storage fetch and upload patterns.
An ASE skill tied to Gotenberg can therefore orchestrate document-generation pipelines for invoices, reports, contracts, archived web pages, and post-processed bundles. Integration points include Docker deployments, object storage workflows, webhook-driven document generation, backend services that submit HTML or office files, and compliance-oriented pipelines that need standardized PDF output plus metadata or encryption controls.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gotenberg-document-to-pdf-conversion-api/)
