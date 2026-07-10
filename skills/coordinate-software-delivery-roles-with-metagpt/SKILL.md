---
name: "Coordinate software delivery roles with MetaGPT"
slug: "coordinate-software-delivery-roles-with-metagpt"
description: "Use MetaGPT to turn a product requirement into coordinated product, architecture, project, and engineering agent outputs that an operator can review and iterate."
github_stars: 68717
verification: "security_reviewed"
source: "https://github.com/FoundationAgents/MetaGPT"
author: "FoundationAgents"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "FoundationAgents/MetaGPT"
  github_stars: 68717
---

# Coordinate software delivery roles with MetaGPT

Use MetaGPT to turn a product requirement into coordinated product, architecture, project, and engineering agent outputs that an operator can review and iterate.

## Prerequisites

Python environment, MetaGPT package or repository install, configured model provider, product requirement, optional repository context, and review criteria for generated artifacts.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install --upgrade metagpt

Requirements and caveats from upstream:
- Ensure that Python 3.9 or later, but less than 3.12, is installed on your system. You can check this by using: python --version.
- You can use conda like this: conda create -n metagpt python=3.9 && conda activate metagpt
- **Install [node](https://nodejs.org/en/download) and [pnpm](https://pnpm.io/installation#using-npm) before actual use.**

Basic usage or getting-started notes:
- For detailed installation guidance, please refer to [cli_install](https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html#install-stable-version)
- You can init the config of MetaGPT by running the following command, or manually create ~/.metagpt/config2.yaml file:
- metagpt --init-config # it will create ~/.metagpt/config2.yaml, just modify it to your needs

- Source: https://github.com/FoundationAgents/MetaGPT
- Extracted from upstream docs: https://raw.githubusercontent.com/FoundationAgents/MetaGPT/HEAD/README.md

## Documentation

- https://github.com/FoundationAgents/MetaGPT

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-software-delivery-roles-with-metagpt/)
