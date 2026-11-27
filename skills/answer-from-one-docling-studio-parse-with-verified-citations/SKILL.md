---
name: "Answer from one Docling Studio parse with verified citations"
slug: "answer-from-one-docling-studio-parse-with-verified-citations"
description: "Read a PDF outline under a token and round budget, verify quoted evidence against one parse, and return a cited answer or a clear evidence gap."
github_stars: 275
verification: "security_reviewed"
source: "https://github.com/scub-france/docling-Studio"
author: "scub-france"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "scub-france/docling-Studio"
  github_stars: 275
---

# Answer from one Docling Studio parse with verified citations

Read a PDF outline under a token and round budget, verify quoted evidence against one parse, and return a cited answer or a clear evidence gap.

## Prerequisites

Git; Docker with at least 6 GB memory; private Docling Studio instance; approved parsed PDF; MCP client

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/scub-france/Docling-Studio.git and check out 1de19294076980570bb0ed127b3f4bc741292677. From the repository root run docker build --target local -t docling-studio:ase-reviewed . then docker run -p 127.0.0.1:3000:3000 -v docling-data:/app/data -v docling-uploads:/app/uploads docling-studio:ase-reviewed. Allow at least 6 GB Docker memory. First parsing downloads Docling models. Import and parse the approved PDF in Studio, then connect an MCP client to http://localhost:3000/mcp. This source build avoids assuming a mutable published image includes the inspected prompt.

- Source: https://github.com/scub-france/docling-Studio

## Documentation

- https://github.com/scub-france/docling-Studio/blob/1de19294076980570bb0ed127b3f4bc741292677/docs/mcp-server.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/answer-from-one-docling-studio-parse-with-verified-citations/)
