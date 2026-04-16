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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-and-repair-word-documents-with-layout-safe-docx-workflows/)
