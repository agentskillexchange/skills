---
name: "Check R table schemas and duplicate keys before combining data with janitor"
slug: "check-r-table-schemas-duplicate-keys-janitor"
description: "Normalize column names, compare data-frame types and expose duplicate records before an R data pipeline combines incoming tables."
github_stars: 1461
verification: "security_reviewed"
source: "https://github.com/sfirke/janitor"
author: "Sam Firke and contributors"
publisher_type: "Open Source Project"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sfirke/janitor"
  github_stars: 1461
---

# Check R table schemas and duplicate keys before combining data with janitor

Normalize column names, compare data-frame types and expose duplicate records before an R data pipeline combines incoming tables.

## Prerequisites

R with Rscript and janitor; CSV importer or readxl for Excel inputs

## Installation

Install or set up from the source-backed instructions:

Rscript -e 'install.packages("janitor", repos="https://cloud.r-project.org")' For Excel inputs, install readxl separately. Implement the documented clean_names, compare_df_cols and get_dupes steps in a local R script; invoke it with Rscript and preserve the original input files.

- Source: https://github.com/sfirke/janitor

## Documentation

- https://github.com/sfirke/janitor/blob/main/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-r-table-schemas-duplicate-keys-janitor/)
