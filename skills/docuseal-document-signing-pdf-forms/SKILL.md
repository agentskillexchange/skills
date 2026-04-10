---
title: "DocuSeal Open Source Document Signing and PDF Form Platform"
description: "DocuSeal is an open-source DocuSign alternative for creating, filling, and signing digital documents. It provides a WYSIWYG PDF form builder with 12 field types, automated email workflows, API and webhook integrations, and embeddable signing components for React, Vue, and Angular."
slug: "docuseal-document-signing-pdf-forms"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/docusealco/docuseal"
tool_ecosystem:
  github_repo: "docusealco/docuseal"
  github_stars: 11695
---

# DocuSeal Open Source Document Signing and PDF Form Platform

DocuSeal is an open-source DocuSign alternative for creating, filling, and signing digital documents. It provides a WYSIWYG PDF form builder with 12 field types, automated email workflows, API and webhook integrations, and embeddable signing components for React, Vue, and Angular.

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
clawhub install docuseal-document-signing-pdf-forms
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

DocuSeal is a self-hosted, open-source platform for secure digital document signing and processing. It provides a complete document workflow — from PDF form creation with a drag-and-drop WYSIWYG builder to automated email delivery, signing, and verification — all without depending on third-party SaaS services.
How It Works
DocuSeal is a Ruby on Rails application that can be deployed via Docker in minutes. Users upload PDF or Word documents, then use the visual form builder to add signature fields, date fields, checkboxes, file uploads, and other field types (12 types total). Documents are assigned to signers by email, who receive automated notifications and complete signing through a mobile-optimized web interface. Signed documents receive automatic PDF eSignatures with cryptographic verification.
Key Features
- WYSIWYG form builder: Drag-and-drop interface for placing 12 field types including Signature, Date, File, Checkbox, Text, Select, and more on any PDF.
- Multiple signers: Support for multiple submitters per document with configurable signing order.
- Automated workflows: SMTP email delivery, automated reminders, and SMS-based identity verification for signers.
- Storage flexibility: Files stored on local disk or cloud storage (AWS S3, Google Cloud Storage, Azure Blob).
- PDF signature verification: Automatic digital signatures on completed documents with cryptographic verification support.
- REST API and webhooks: Full API for template management, submission creation, and status tracking. Webhooks notify external systems on document events.
- Embeddable components: Official React, Vue, and Angular components for embedding the signing form and form builder directly into your application.
- Bulk operations: Send documents in bulk using CSV or XLSX spreadsheet imports.
- HTML API templates: Create templates programmatically using HTML markup instead of the visual builder.
- White-label: Custom company logo, branding, and SSO/SAML support.
Integration Points
Deploy with Docker: docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal. For production, use the provided docker-compose.yml with Caddy for automatic HTTPS. The REST API supports full CRUD operations on templates and submissions. Embed signing forms using @docuseal/react, @docuseal/vue, or @docuseal/angular npm packages.
Agent Integration
AI agents can use DocuSeal’s REST API to automate document workflows — create templates from HTML, initiate signing requests, track submission status, and retrieve signed documents. The webhook system enables event-driven automation where agents respond to document completion events, extract signed data, and trigger downstream processes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docuseal-document-signing-pdf-forms/)
