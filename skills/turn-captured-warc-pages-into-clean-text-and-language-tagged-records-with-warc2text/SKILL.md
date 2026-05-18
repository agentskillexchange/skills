---
name: "Turn captured WARC pages into clean text and language-tagged records with warc2text"
slug: "turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text"
description: "Use warc2text when an agent already has WARC captures and needs readable text, language identification, and exportable records for review, search, or corpus building instead of re-crawling pages."
github_stars: 23
verification: "security_reviewed"
source: "https://github.com/bitextor/warc2text"
author: "Bitextor contributors"
publisher_type: "open_source_project"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bitextor/warc2text"
  github_stars: 23
---

# Turn captured WARC pages into clean text and language-tagged records with warc2text

Use warc2text when an agent already has WARC captures and needs readable text, language identification, and exportable records for review, search, or corpus building instead of re-crawling pages.

## Prerequisites

warc2text build or binary, WARC input files, local output storage

## Installation

Use the upstream install or setup path that matches your environment:
- git clone --recurse-submodules https://github.com/bitextor/warc2text.git
- git clone https://github.com/bitextor/warc2text.git
- brew install uchardet libzip
- cmake -DCMAKE_INSTALL_PREFIX=/your/prefix/path ..

Requirements and caveats from upstream:
- On a node with EasyBuild installed you can install warc2text as a module:
- --skip-text-extraction Skip text extraction and output only html. This option is not compatible with "text" value in -f option and also requires to skip language identification.

Basic usage or getting-started notes:
- On Debian/Ubuntu/Mint:
- apt-get install build-essential cmake libuchardet-dev libzip-dev libboost-thread-dev libboost-regex-dev libboost-filesystem-dev libboost-log-dev libboost-iostreams-dev libboost-locale-dev libboost-program-options-dev
- On Mac:

- Source: https://github.com/bitextor/warc2text
- Extracted from upstream docs: https://raw.githubusercontent.com/bitextor/warc2text/HEAD/README.md

## Documentation

- https://github.com/bitextor/warc2text

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text/)
