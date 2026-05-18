---
name: "Grist Self-Hosted Relational Spreadsheet and Database Platform"
slug: "grist-self-hosted-relational-spreadsheet-database"
description: "Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance."
github_stars: 10827
verification: "listed"
source: "https://github.com/gristlabs/grist-core"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "gristlabs/grist-core"
  github_stars: 10827
---

# Grist Self-Hosted Relational Spreadsheet and Database Platform

Grist is an open-source modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database. It supports Python formulas, a REST API, self-hosting via Docker, and AI-powered formula assistance.

## Installation

Use the upstream install or setup path that matches your environment:
- docker pull gristlabs/grist
- docker run -p 8484:8484 -it gristlabs/grist
- docker run -p 8484:8484 -v $PWD/persist:/persist -it gristlabs/grist
- docker run --env PORT=9999 -p 9999:9999 -v $PWD/persist:/persist -it gristlabs/grist

Requirements and caveats from upstream:
- To see exactly what is present in grist-core, you can run the [desktop app](https://github.com/gristlabs/grist-desktop), or use [docker](#using-grist). The absolute fastest way to try Grist out is to visit [docs.getgr...
- Python formulas.
- Full [Python syntax is supported](https://support.getgrist.com/formulas/#python), including the standard library.

Basic usage or getting-started notes:
- grist-core (this repo – also known as Grist Community edition) has what you need to run a powerful server for hosting spreadsheets.
- If you evaluate Grist by using the hosted version at [getgrist.com](https://getgrist.com), be aware that it includes some features that aren't present in grist-core. To be sure you're seeing exactly what is present in...

- Source: https://github.com/gristlabs/grist-core
- Extracted from upstream docs: https://raw.githubusercontent.com/gristlabs/grist-core/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grist-self-hosted-relational-spreadsheet-database/)
