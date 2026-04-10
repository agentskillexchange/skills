---
title: "fq Binary Format Inspector and jq for Media Files"
description: "fq is a command-line tool that brings jq-style querying to binary formats. It decodes, inspects, and transforms media containers, executables, packet captures, and dozens of other binary formats using familiar jq expressions and an interactive REPL."
slug: "fq-binary-format-inspector-jq-media"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/wader/fq"
tool_ecosystem:
  github_repo: "wader/fq"
  github_stars: 10468
listed: true
---

# fq Binary Format Inspector and jq for Media Files

fq is a command-line tool that brings jq-style querying to binary formats. It decodes, inspects, and transforms media containers, executables, packet captures, and dozens of other binary formats using familiar jq expressions and an interactive REPL.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install fq-binary-format-inspector-jq-media
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

What is fq?
fq is a command-line tool for working with binary data using jq-style expressions. Created by Mattias Wadman, it aims to be jq, hexdump, dd, and gdb for files combined into one tool. Originally designed for inspecting media codecs and containers like MP4, FLAC, and JPEG, fq has expanded to support executables (ELF, Mach-O), packet captures (pcap, pcapng with TCP reassembly), serialization formats (JSON, YAML, XML, CBOR, protobuf, msgpack), and many more.
How It Works
Install fq via Homebrew (brew install wader/tap/fq), Go (go install github.com/wader/fq@latest), or system package managers for Arch, Nix, FreeBSD, and others. Run fq . file.mp4 to decode and display a file as a tree structure. Use fq d file.mp4 for a detailed decode view, or write jq expressions to query specific structures within binary files.
Format Support
fq supports over 200 binary and text formats. Media formats include MP4, Matroska/WebM, AVI, FLAC, MP3, Ogg, MIDI, JPEG, GIF, and PNG. System formats include ELF, Mach-O, and NES ROMs. Network formats include pcap and pcapng with full TCP reassembly. Data formats include Avro, BSON, CBOR, MessagePack, and Protocol Buffers. Each decoder understands the internal structure of its format and presents it as a queryable tree.
Interactive REPL
fq features an interactive REPL with auto-completion for function names and decoded field names. You can navigate decoded structures, slice binary data, transform between formats, and concatenate binary segments. The REPL supports the full jq language plus fq-specific extensions for binary data manipulation, including hexadecimal, octal, and binary integer literals.
Integration Points
fq reads from files, stdin, or URLs. Output can be formatted as JSON, text, or raw binary, making it composable with other Unix tools. It is particularly useful for debugging media pipelines, analyzing network traffic, reverse engineering file formats, and validating binary data integrity in automated workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fq-binary-format-inspector-jq-media/)
