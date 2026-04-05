---
name: "Documenso Open Source Document Signing Platform"
description: "Documenso is an open-source digital document signing platform and DocuSign alternative. It enables secure electronic signatures with self-hosting capabilities, providing transparent and trustworthy document workflows built on open trust infrastructure."
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/documenso/documenso"
tool_ecosystem:
  github_repo: "documenso/documenso"
  github_stars: 12580
---
# Documenso Open Source Document Signing Platform

Documenso is an open-source digital document signing platform and DocuSign alternative. It enables secure electronic signatures with self-hosting capabilities, providing transparent and trustworthy document workflows built on open trust infrastructure.

Documenso is an open-source document signing platform built with TypeScript and Next.js. It serves as a self-hostable alternative to proprietary solutions like DocuSign, providing legally valid electronic signatures while keeping signing infrastructure under your control. The project is licensed under AGPL-3.0 and has over 12,000 GitHub stars.



Core Signing Workflow

Documenso supports the complete document signing lifecycle: upload a PDF, place signature fields, send to recipients, and collect legally binding electronic signatures. The platform supports multiple signature types including drawn signatures, typed signatures, and uploaded signature images. Recipients receive email notifications with secure signing links that work in any browser without account creation.



Document Templates

Frequently used document types can be saved as templates with pre-configured signature fields, recipient roles, and default settings. This streamlines repetitive signing workflows for contracts, NDAs, offer letters, and other standard documents. Templates support dynamic fields that auto-populate with recipient data.



API and Webhooks

The Documenso REST API enables programmatic document creation, field placement, and sending. Developers can integrate signing workflows directly into applications, CRMs, or onboarding flows. Webhook events fire on key lifecycle transitions (document sent, viewed, signed, completed) enabling real-time status tracking and downstream automation.



Self-Hosting Architecture

Documenso runs as a Next.js application with PostgreSQL and Prisma ORM. Self-hosting is supported via Docker with a provided docker-compose configuration. The stack includes the web application, API server, background job processor, and email sending via SMTP or supported transactional email providers. All signing data stays on your infrastructure.



Security and Compliance

Documents are digitally sealed using X.509 certificates, creating tamper-evident PDFs that meet eIDAS and ESIGN Act requirements. The signing process generates a detailed audit trail with IP addresses, timestamps, and browser fingerprints. Self-hosted deployments give organizations full control over data residency and retention policies.



Team and Organization Features

Documenso supports team workspaces where multiple users share document templates, track signing progress, and manage organizational settings. Role-based access controls define who can create, send, and manage documents. Team-level branding customization allows organizations to use their own logo and colors in signing emails and pages.



Agent Integration Potential

AI agents can use the Documenso API to automate document preparation, trigger signing requests as part of onboarding or contract workflows, and monitor completion status. The webhook system enables event-driven agent actions when documents reach specific states, making it suitable for automated approval pipelines and compliance workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill documenso-open-source-document-signing
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill documenso-open-source-document-signing -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill documenso-open-source-document-signing -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill documenso-open-source-document-signing -a codex
```

### OpenClaw

```bash
clawhub install documenso-open-source-document-signing
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/documenso-open-source-document-signing/)
