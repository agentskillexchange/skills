---
name: "Run reproducible document-parser evaluations with the OmniDocBench skill"
slug: "run-reproducible-document-parser-evaluations-with-omnidocbench-skill"
description: "Validate parser predictions, run OmniDocBench evaluations, and report formula, table, text, and reading-order scores with runtime diagnostics."
verification: "security_reviewed"
source: "https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/skills/SKILL.md"
author: "OpenDataLab"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
---

# Run reproducible document-parser evaluations with the OmniDocBench skill

Validate parser predictions, run OmniDocBench evaluations, and report formula, table, text, and reading-order scores with runtime diagnostics.

## Prerequisites

Git; shell-capable agent; Docker with accessible daemon or Python 3.10 source environment; ground-truth JSON and page Markdown predictions; writable output storage; TeX Live/CJK, ImageMagick and Ghostscript for CDM.

## Installation

Install or set up from the source-backed instructions:

Clone the complete upstream repository using git clone https://github.com/opendatalab/OmniDocBench.git, enter OmniDocBench, and check out ea2d138c7d2e185feb71ef8014e97d7206820b34. Keep skills/SKILL.md with skills/scripts/ and the evaluator source; configure your agent to read the skill using its own skill-loading mechanism. Follow the pinned README Docker setup; its documented image is ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204. Supply existing ground-truth JSON, page Markdown predictions, and a separate output directory. For a source environment, use Python 3.10 and pip install -e . from the repository root; CDM also needs the documented TeX Live/CJK, ImageMagick and Ghostscript setup. Generate configuration using python skills/scripts/generate_end2end_config.py --gt /absolute/path/OmniDocBench.json --pred /absolute/path/predictions --out configs/custom_end2end.yaml --workers 2. Run python pdf_validation.py --config configs/custom_end2end.yaml in that configured runtime. Inspect results using python skills/scripts/parse_results.py /absolute/path/results --prefix YOUR_RESULT_PREFIX --pred /absolute/path/predictions. Use paths as seen by the chosen runtime and read-only input mounts. These are setup instructions; no evaluation was run during discovery.

- Source: https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/skills/SKILL.md

## Documentation

- https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/skills/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-reproducible-document-parser-evaluations-with-omnidocbench-skill/)
