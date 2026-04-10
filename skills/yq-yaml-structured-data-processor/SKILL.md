---
title: "yq YAML and Structured Data Processor"
description: "Process, query, and transform YAML, JSON, XML, CSV, TOML, and properties files from the command line using yq. Supports jq-like expressions for reading, updating, and converting between formats."
slug: "yq-yaml-structured-data-processor"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/mikefarah/yq"
tool_ecosystem:
  github_repo: "mikefarah/yq"
  github_stars: 15143
listed: true
---

# yq YAML and Structured Data Processor

Process, query, and transform YAML, JSON, XML, CSV, TOML, and properties files from the command line using yq. Supports jq-like expressions for reading, updating, and converting between formats.

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
clawhub install yq-yaml-structured-data-processor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The yq YAML and Structured Data Processor skill uses mikefarah/yq, a portable command-line tool that applies jq-like expression syntax to YAML, JSON, XML, CSV, TOML, INI, HCL, and properties files. With over 15,000 GitHub stars and millions of downloads, yq is the go-to tool for configuration file manipulation in DevOps and infrastructure automation workflows.
yq reads structured data, applies path expressions to select or modify nodes, and outputs the result. Reading a nested value is as simple as running yq '.a.b[0].c' file.yaml. In-place updates use the -i flag: yq -i '.image.tag = "v2.1.0"' deployment.yaml. Environment variable interpolation is built in via strenv(), which means the agent can template configuration files without external tools. Multiple updates chain naturally with the pipe operator.
Format conversion is a core strength. Converting JSON to pretty-printed YAML is yq -Poy data.json. Converting YAML to JSON is yq -o json data.yaml. XML, CSV, and TOML conversions follow the same pattern. This makes yq essential for pipelines that consume data in one format and produce it in another—Kubernetes manifests to JSON for API calls, CSV exports to YAML for configuration management, or XML API responses to structured YAML for further processing.
Advanced operations include merging multiple files with glob patterns, finding and updating items in arrays by field value, creating new documents from expressions, and evaluating multiple files simultaneously with the ea (evaluate all) command. The expression language supports conditionals, string functions, regex, recursive descent, and type coercion.
yq is written in Go and ships as a single dependency-free binary for Linux, macOS, and Windows. It is available via Homebrew, snap, apt (via PPA), Docker, pip, and direct download. Licensed under MIT, it maintains an active release cadence with the latest version being v4.52.4. For any agent working with configuration files, Helm values, Kubernetes manifests, or data transformation pipelines, yq provides the foundation for precise, scriptable edits without manual file manipulation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yq-yaml-structured-data-processor/)
