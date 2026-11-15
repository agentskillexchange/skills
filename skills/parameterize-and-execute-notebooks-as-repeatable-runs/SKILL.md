---
name: "Parameterize and execute notebooks as repeatable runs"
slug: "parameterize-and-execute-notebooks-as-repeatable-runs"
description: "Use Papermill when an agent needs to treat a Jupyter notebook like a reusable job instead of a one-off interactive document. The skill injects parameters, runs the notebook end to end, and preserves the executed output as an artifact for review or handoff."
github_stars: 6429
verification: "security_reviewed"
source: "https://github.com/nteract/papermill"
author: "nteract"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "nteract/papermill"
  github_stars: 6429
---

# Parameterize and execute notebooks as repeatable runs

Use Papermill when an agent needs to treat a Jupyter notebook like a reusable job instead of a one-off interactive document. The skill injects parameters, runs the notebook end to end, and preserves the executed output as an artifact for review or handoff.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install papermill
- pip install papermill[all]

Requirements and caveats from upstream:
- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/papermill)](https://pypi.org/project/papermill/)
- [![papermill](https://snyk.io/advisor/python/papermill/badge.svg)](https://snyk.io/advisor/python/papermill)
- like s3, or azure -- or use all. To use Black to format parameters you can add as an extra requires ['black'].

Basic usage or getting-started notes:
- example:
- Perhaps you have a financial report that you wish to run with
- Do you want to run a notebook and depending on its results, choose a

- Source: https://github.com/nteract/papermill
- Extracted from upstream docs: https://raw.githubusercontent.com/nteract/papermill/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parameterize-and-execute-notebooks-as-repeatable-runs/)
