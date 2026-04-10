---
name: pdfme Open Source TypeScript PDF Generation Library with WYSIWYG Designer
description: pdfme is an open-source TypeScript and React library for generating PDFs
  programmatically. It includes a WYSIWYG template designer, PDF viewer, and CLI tools
  for validation and generation in both browser and Node.js environments.
verification: security_reviewed
source: https://github.com/pdfme/pdfme
category:
- Developer Tools
framework:
- Multi-Framework
---
# pdfme Open Source TypeScript PDF Generation Library with WYSIWYG Designer

pdfme is an open-source PDF generation library built entirely with TypeScript and React. It provides a complete toolkit for creating, designing, and generating PDF documents in both browser and Node.js environments. With over 4,200 GitHub stars and 50,000+ weekly npm downloads, pdfme has become one of the most popular open-source PDF generation solutions in the JavaScript ecosystem.
Core Components
The library is organized into several packages that work together:

@pdfme/generator — The core PDF generation engine that takes JSON templates and input data to produce PDF files. Works in Node.js and the browser.
@pdfme/ui — A React-based WYSIWYG template designer and PDF viewer that lets anyone visually create and edit PDF templates without writing code.
@pdfme/common — Shared types, schemas, and utilities used across all pdfme packages.
@pdfme/cli — A command-line interface for validating templates, diagnosing issues, and generating PDFs in agentic and CI/CD workflows.

How It Works
pdfme uses a JSON-based template format that describes the layout, fonts, and dynamic fields of a PDF. Templates define a base PDF (or blank page) with positioned schema elements like text fields, images, barcodes, QR codes, and tables. At generation time, you pass the template along with input data, and pdfme produces the final PDF.
The template designer provides a drag-and-drop interface for positioning elements, configuring fonts, setting alignment, and previewing the result in real time. Templates can be exported as JSON and reused across different inputs.
Agent Integration
For AI agents and automation workflows, pdfme offers several integration points:

The CLI supports pdfme validate to check template JSON before generation
pdfme doctor diagnoses runtime, font, and configuration issues
pdfme generate --image --grid produces PDFs with visual layout inspection
Templates are pure JSON, making them easy to generate, modify, and version-control programmatically

Installation
Install with npm:
npm install @pdfme/generator @pdfme/common
For the designer UI:
npm install @pdfme/ui
For CLI tools:
npm install -g @pdfme/cli
Use Cases
pdfme is used for invoices, contracts, certificates, reports, onboarding documents, HR forms, shipping labels, and any workflow requiring programmatic PDF creation with consistent formatting. The JSON template approach makes it particularly well-suited for agent-driven document generation where templates can be composed and filled dynamically.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdfme-typescript-pdf-generation-library/)
