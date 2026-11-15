---
name: "Repair, split, merge, and normalize PDFs with qpdf before downstream processing"
slug: "repair-split-merge-and-normalize-pdfs-with-qpdf-before-downstream-processing"
description: "Preprocess messy PDFs into a stable form before extraction, review, packaging, or delivery workflows depend on them."
github_stars: 1479
verification: "security_reviewed"
source: "https://github.com/qpdf/qpdf"
author: "qpdf"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "qpdf/qpdf"
  github_stars: 1479
---

# Repair, split, merge, and normalize PDFs with qpdf before downstream processing

Preprocess messy PDFs into a stable form before extraction, review, packaging, or delivery workflows depend on them.

## Prerequisites

qpdf installation, source PDF files, writable output path, optional downstream extraction or delivery workflow

## Installation

Use the upstream install or setup path that matches your environment:
- cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
- cmake --build build
- cmake -S . -B build -G 'MSYS Makefiles' -DCMAKE_BUILD_TYPE=RelWithDebInfo
- cmake -S . -B build

Requirements and caveats from upstream:
- qpdf depends on the external libraries [zlib](https://www.zlib.net/) and [jpeg](https://www.ijg.org/files/).
- By default, slow tests and tests that require dependencies beyond those needed to build qpdf are disabled. Slow tests

Basic usage or getting-started notes:
- Official qpdf releases are signed using [cosign](https://docs.sigstore.dev/quickstart/quickstart-cosign/). Each release includes a sha256 file containing sha256 checksums of all the release files. To verify a release,...
- To build and test qpdf, a C++ compiler that supports C++20 is required. To link with qpdf, a C++17-compatible compiler
- is sufficient.

- Source: https://github.com/qpdf/qpdf
- Extracted from upstream docs: https://raw.githubusercontent.com/qpdf/qpdf/HEAD/README.md

## Documentation

- https://qpdf.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-split-merge-and-normalize-pdfs-with-qpdf-before-downstream-processing/)
