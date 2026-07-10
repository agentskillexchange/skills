---
name: "Parse documents into structured content for agent ingestion with Dedoc"
slug: "parse-documents-into-structured-content-for-agent-ingestion-with-dedoc"
description: "Extract document text, tables, logical structure, and metadata into normalized output before RAG, review, or workflow automation."
github_stars: 712
verification: "security_reviewed"
source: "https://github.com/ispras/dedoc"
author: "ISP RAS"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ispras/dedoc"
  github_stars: 712
---

# Parse documents into structured content for agent ingestion with Dedoc

Extract document text, tables, logical structure, and metadata into normalized output before RAG, review, or workflow automation.

## Prerequisites

Dedoc Docker service or Python library, source documents

## Installation

Use the upstream install or setup path that matches your environment:
- docker pull dedocproject/dedoc
- docker run -p 1231:1231 --rm dedocproject/dedoc python3 /dedoc_root/dedoc/main.py
- git clone https://github.com/ispras/dedoc
- docker compose up --build

Requirements and caveats from upstream:
- [![image](https://img.shields.io/pypi/pyversions/dedoc.svg)](https://pypi.python.org/pypi/dedoc)
- [![Docker Hub](https://img.shields.io/docker/pulls/dedocproject/dedoc.svg)](https://hub.docker.com/r/dedocproject/dedoc/ "Docker Pulls")
- Dedoc is implemented in Python and works with semi-structured data formats (DOC/DOCX, ODT, XLS/XLSX, CSV, TXT, JSON) and unstructured data formats like images (PNG, JPG etc.), archives (ZIP, RAR etc.), PDF and HTML fo...

Basic usage or getting-started notes:
- <img src="https://github.com/ispras/dedoc/raw/master/docs/source/_static/example_table.jpg" alt="Table parsing example" style="width:600px;"/>
- <img src="https://github.com/ispras/dedoc/raw/master/docs/source/_static/str_ext_example_law.png" alt="Law structure example"/>
- <img src="https://github.com/ispras/dedoc/raw/master/docs/source/_static/str_ext_example_tz.png" alt="Tz structure example"/>

- Source: https://github.com/ispras/dedoc
- Extracted from upstream docs: https://raw.githubusercontent.com/ispras/dedoc/HEAD/README.md

## Documentation

- https://dedoc.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-documents-into-structured-content-for-agent-ingestion-with-dedoc/)
