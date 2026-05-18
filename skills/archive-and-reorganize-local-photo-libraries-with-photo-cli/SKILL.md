---
name: "Archive and reorganize local photo libraries with photo-cli"
slug: "archive-and-reorganize-local-photo-libraries-with-photo-cli"
description: "Use photo-cli when an agent needs to normalize a local photo archive by reading capture metadata, reverse geocoding locations, and rebuilding a cleaner folder structure without moving into a hosted photo platform."
github_stars: 68
verification: "listed"
source: "https://github.com/photo-cli/photo-cli"
author: "photo-cli contributors"
publisher_type: "open_source_project"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "photo-cli/photo-cli"
  github_stars: 68
---

# Archive and reorganize local photo libraries with photo-cli

Use photo-cli when an agent needs to normalize a local photo archive by reading capture metadata, reverse geocoding locations, and rebuilding a cleaner folder structure without moving into a hosted photo platform.

## Prerequisites

photo-cli, access to the source photo library, destination storage for the reorganized archive

## Installation

Use the upstream install or setup path that matches your environment:
- npx @modelcontextprotocol/inspector {photo-cli-standalone-executable-or-dotnet-tool-path-or-docker-command} mcp --input {archive-folder-path}
- npx @modelcontextprotocol/inspector photo-cli mcp --input {archive-folder-path}
- docker run --rm --volume ./test-photographs:/photos/input --volume ./archive:/photos/output photocli/photocli archive --input /photos/input --output /photos/output --album-type DateRange --album-name My-Album --auto-r...

Requirements and caveats from upstream:
- This application can be installed by Homebrew (macOS & Linux), container (Docker, Podman), standalone executable (without dependency and SDK) or as .NET tool.
- A photo archive folder created with photo-cli archive (must contain the photo-cli.db SQLite database).
- "command": "{photo-cli-standalone-executable-or-dotnet-tool-path-or-docker-command}",

Basic usage or getting-started notes:
- [![Nuget release](https://img.shields.io/nuget/v/photo-cli?label=stable&color=blue)](https-://www.nuget.org/packages/photo-cli/) [![Nuget download count](https://img.shields.io/nuget/dt/photo-cli)](https://www.nuget.o...
- [Features Explained With An Example](#features-explained-with-examples)
- [Sample Usage Screenshots](#sample-usage-screenshots)

- Source: https://github.com/photo-cli/photo-cli
- Extracted from upstream docs: https://raw.githubusercontent.com/photo-cli/photo-cli/HEAD/README.md

## Documentation

- https://photocli.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/archive-and-reorganize-local-photo-libraries-with-photo-cli/)
