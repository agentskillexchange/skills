---
name: "Bootstrap and verify self-hosted Rakazo from published images"
slug: "bootstrap-and-verify-self-hosted-rakazo-from-published-images"
description: "Prepare a Docker-based Rakazo installation, preserve private configuration, and verify service health, the selected sandbox, and an optional first bot reply before handoff."
github_stars: 5822
verification: "security_reviewed"
source: "https://github.com/elie222/rakazo"
author: "elie222"
publisher_type: "open-source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "elie222/rakazo"
  github_stars: 5822
---

# Bootstrap and verify self-hosted Rakazo from published images

Prepare a Docker-based Rakazo installation, preserve private configuration, and verify service health, the selected sandbox, and an optional first bot reply before handoff.

## Prerequisites

Docker Engine, Docker Compose plugin, curl, OpenSSL; coding agent with shell access; optional browser assistance

## Installation

Install or set up from the source-backed instructions:

Read https://github.com/elie222/rakazo/blob/f9165321526c4923816c5e854c16ff078059bd07/SETUP_PROMPT.md and https://github.com/elie222/rakazo/blob/f9165321526c4923816c5e854c16ff078059bd07/docs/self-host.md. In an agreed directory, download and inspect https://raw.githubusercontent.com/elie222/rakazo/f9165321526c4923816c5e854c16ff078059bd07/infra/compose/install-images.sh. Set RAKAZO_DOWNLOAD_BASE to https://raw.githubusercontent.com/elie222/rakazo/f9165321526c4923816c5e854c16ff078059bd07/infra/compose for revision-aligned configuration, then run bash install-images.sh --prepare-only. Review existing environment and egress behavior, configure only agreed options, and run bash install-images.sh. Verify internal API health, selected sandbox and web UI; verify a harmless reply only after model connection. Do not overwrite private configuration or delete volumes.

- Source: https://github.com/elie222/rakazo

## Documentation

- https://github.com/elie222/rakazo/blob/f9165321526c4923816c5e854c16ff078059bd07/SETUP_PROMPT.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-and-verify-self-hosted-rakazo-from-published-images/)
