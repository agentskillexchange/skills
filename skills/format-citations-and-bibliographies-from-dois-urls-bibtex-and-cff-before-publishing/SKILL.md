---
title: "Format citations and bibliographies from DOIs, URLs, BibTeX, and CFF before publishing"
description: "Use Citation.js when an agent has raw references and needs clean citation output instead of hand-formatting sources. It can resolve supported identifiers, normalize metadata into CSL-JSON, and emit bibliography or inline citation formats that fit articles, research notes, docs, or release materials."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/citation-js"
category:
  - "Content Writing & SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  ase_npm_package: "citation-js"
  npm_weekly_downloads: 10654
---

# Format citations and bibliographies from DOIs, URLs, BibTeX, and CFF before publishing

This ASE entry is built around citation-js, the npm package and project behind Citation.js. The skill-shaped job is specific: take messy or mixed reference inputs, such as a DOI, BibTeX, CFF file, GitHub repository URL, npm package URL, RIS record, or Wikidata identifier, normalize that source material into structured citation data, and then format publishable output in the requested style. That gives an agent a concrete workflow for bibliography generation instead of leaving it to brittle hand-written formatting or one-off copy edits.


Use this when the user is preparing a blog post, whitepaper, documentation page, changelog, academic note, grant draft, or research roundup and wants citations that are consistent and machine-generated. This is especially useful when an agent is already collecting sources from APIs, markdown frontmatter, CITATION.cff files, GitHub repositories, or reference managers and needs to turn those inputs into APA, Vancouver, BibTeX, CSL-JSON, or HTML bibliography output. It is the right moment to invoke the skill when the hard part is citation normalization and rendering, not when the user needs a full literature review workflow or a human reference manager UI.


The scope boundary keeps it from being a plain package card. Citation.js does not decide what sources are credible, summarize papers, or manage a long-lived research library on its own. Its job is bounded to parsing supported inputs, resolving certain identifiers, and producing reliable citation output for downstream publishing systems. Integration points include Node.js content pipelines, markdown or MDX builds, static site generators, docs repos, browser tools, and custom automation that needs publication-ready citations without manual cleanup.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-citations-and-bibliographies-from-dois-urls-bibtex-and-cff-before-publishing/)
