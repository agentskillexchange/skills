---
title: "Create and repair Word documents with layout-safe DOCX workflows"
description: "Use the Anthropic docx skill when an agent needs to produce or repair a real .docx deliverable with headings, tables, numbering, tracked changes, or layout constraints. It frames the work as a document-building workflow with validation and packaging rules, not as a generic document library listing."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/docx"
category:
  - "Templates & Workflows"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116918
---

# Create and repair Word documents with layout-safe DOCX workflows

The upstream tool is Anthropic’s docx skill from the anthropics/skills repository. What the agent actually does is create, edit, validate, and repair Word documents as real deliverables. That includes generating new .docx files, unpacking and fixing existing documents, preserving numbering and table behavior, handling tracked changes, converting legacy .doc inputs, and validating that the final file opens cleanly instead of shipping malformed XML.

Users should invoke this when the request is document-native: build a memo, template, report, or letterhead in Word format, clean up a broken DOCX, accept tracked changes, replace images, or preserve document structure while editing. This is where an agent is more useful than “using the product normally,” because the real work is not clicking around Word. The hard part is following layout-safe rules, using the right generation path, and avoiding fragile edits that corrupt styles, tables, or lists.

The scope boundary is clear. This is not a plain listing for Microsoft Word, pandoc, or a JavaScript DOCX library. It is also not the right entry for PDF manipulation, spreadsheet work, or HTML publishing. The skill is about bounded agent behavior around DOCX outputs. Integration points include docx generation libraries, pandoc for extraction, LibreOffice for conversions, XML unpack/repack workflows, and validation helpers that catch packaging errors before delivery.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/create-and-repair-word-documents-with-layout-safe-docx-workflows/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/create-and-repair-word-documents-with-layout-safe-docx-workflows
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/create-and-repair-word-documents-with-layout-safe-docx-workflows`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-and-repair-word-documents-with-layout-safe-docx-workflows/)
