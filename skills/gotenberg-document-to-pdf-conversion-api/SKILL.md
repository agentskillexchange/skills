---
name: Gotenberg Document-to-PDF Conversion API
description: Gotenberg is a Docker-based API for converting HTML, URLs, Markdown,
  and office documents into PDF, then performing post-processing tasks such as merge,
  split, watermark, metadata edits, and encryption. It wraps Chromium, LibreOffice,
  and PDF engines behind a single HTTP interface.
verification: security_reviewed
source: https://github.com/gotenberg/gotenberg
category:
- Library &amp; API Reference
framework:
- Multi-Framework
---
# Gotenberg Document-to-PDF Conversion API

Gotenberg is a developer-friendly API for document conversion and PDF post-processing. The project runs as a Docker image and exposes HTTP endpoints that accept files or URLs over multipart/form-data, then returns PDFs or derived outputs. The official documentation and README highlight three big capability groups: Chromium-based rendering for HTML, URLs, and Markdown; LibreOffice-driven conversion for office formats such as DOCX, XLSX, and PPTX; and PDF engine endpoints for merging, splitting, rotating, watermarking, flattening, encrypting, and manipulating metadata.
This gives it a concrete job to be done inside ASE: turn inbound documents or web pages into printable PDFs, automate office-to-PDF conversion, and run downstream PDF operations in server-side workflows without maintaining bespoke LibreOffice or browser automation wrappers. Gotenberg also supports features that matter in production pipelines, including waiting for dynamic content before rendering, custom headers and cookies for authenticated pages, PDF/A and PDF/UA options, screenshots, and direct cloud-storage fetch and upload patterns.
An ASE skill tied to Gotenberg can therefore orchestrate document-generation pipelines for invoices, reports, contracts, archived web pages, and post-processed bundles. Integration points include Docker deployments, object storage workflows, webhook-driven document generation, backend services that submit HTML or office files, and compliance-oriented pipelines that need standardized PDF output plus metadata or encryption controls.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gotenberg-document-to-pdf-conversion-api/)
