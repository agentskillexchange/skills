---
name: "Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs"
slug: "compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs"
description: "Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON."
github_stars: 330
verification: "listed"
source: "https://github.com/simonw/csv-diff"
author: "Simon Willison"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/csv-diff"
  github_stars: 330
---

# Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs

Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON.

## Prerequisites

Python 3, pip, two comparable CSV, TSV, or JSON snapshots, and a stable key column or field.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install csv-diff
- $ docker build -t csvdiff .
- $ docker run --rm -v $(pwd):/files csvdiff
- $ docker run --rm -v $(pwd):/files csvdiff one.csv two.csv

Requirements and caveats from upstream:
- --extra name "Python format string with {id} for variables"
- ## As a Python library
- You can also import the Python library into your own code like so:

Basic usage or getting-started notes:
- Consider two CSV files:
- one.csv
- id,name,age

- Source: https://github.com/simonw/csv-diff
- Extracted from upstream docs: https://raw.githubusercontent.com/simonw/csv-diff/HEAD/README.md

## Documentation

- https://github.com/simonw/csv-diff

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/)
