---
name: "Generate fast static photo album sites from curated folders with DD Photos"
slug: "generate-fast-static-photo-album-sites-from-curated-folders-with-dd-photos"
description: "Turn exported photo folders into a mobile-friendly static album site without standing up a database-backed gallery system."
github_stars: 155
verification: "listed"
source: "https://github.com/dougdonohoe/ddphotos"
author: "Doug Donohoe"
publisher_type: "individual"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dougdonohoe/ddphotos"
  github_stars: 155
---

# Generate fast static photo album sites from curated folders with DD Photos

Turn exported photo folders into a mobile-friendly static album site without standing up a database-backed gallery system.

## Prerequisites

Go toolchain or built binaries, source photo folders, DD Photos config files, optional static hosting target such as S3 or a web server

## Installation

Use the upstream install or setup path that matches your environment:
- docker run --rm -v ~/my-ddphotos:/ddphotos dougdonohoe/ddphotos init

Requirements and caveats from upstream:
- [![Docker Image Version](https://img.shields.io/docker/v/dougdonohoe/ddphotos?logo=docker&label=Docker%20Hub)](https://hub.docker.com/r/dougdonohoe/ddphotos)
- [![Docker Pulls](https://img.shields.io/docker/pulls/dougdonohoe/ddphotos?logo=docker&label=Docker%20Pulls)](https://hub.docker.com/r/dougdonohoe/ddphotos)
- ## Docker Quick Start

Basic usage or getting-started notes:
- ./ddphotos run # run dev server at http://localhost:5173
- Once you have defined where your photos live, you run the photogen tool,
- Dry-run mode by default (use -doit to write files).

- Source: https://github.com/dougdonohoe/ddphotos
- Extracted from upstream docs: https://raw.githubusercontent.com/dougdonohoe/ddphotos/HEAD/README.md

## Documentation

- https://ddphotos.donohoe.info

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-fast-static-photo-album-sites-from-curated-folders-with-dd-photos/)
