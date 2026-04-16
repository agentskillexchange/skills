---
title: "yq YAML and Structured Data Processor"
description: "Process, query, and transform YAML, JSON, XML, CSV, TOML, and properties files from the command line using yq. Supports jq-like expressions for reading, updating, and converting between formats."
verification: "security_reviewed"
source: "https://github.com/mikefarah/yq"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "mikefarah/yq"
  github_stars: 15143
---

# yq YAML and Structured Data Processor

The yq YAML and Structured Data Processor skill uses mikefarah/yq, a portable command-line tool that applies jq-like expression syntax to YAML, JSON, XML, CSV, TOML, INI, HCL, and properties files. With over 15,000 GitHub stars and millions of downloads, yq is the go-to tool for configuration file manipulation in DevOps and infrastructure automation workflows.


yq reads structured data, applies path expressions to select or modify nodes, and outputs the result. Reading a nested value is as simple as running yq '.a.b[0].c' file.yaml. In-place updates use the -i flag: yq -i '.image.tag = "v2.1.0"' deployment.yaml. Environment variable interpolation is built in via strenv(), which means the agent can template configuration files without external tools. Multiple updates chain naturally with the pipe operator.


Format conversion is a core strength. Converting JSON to pretty-printed YAML is yq -Poy data.json. Converting YAML to JSON is yq -o json data.yaml. XML, CSV, and TOML conversions follow the same pattern. This makes yq essential for pipelines that consume data in one format and produce it in another—Kubernetes manifests to JSON for API calls, CSV exports to YAML for configuration management, or XML API responses to structured YAML for further processing.


Advanced operations include merging multiple files with glob patterns, finding and updating items in arrays by field value, creating new documents from expressions, and evaluating multiple files simultaneously with the ea (evaluate all) command. The expression language supports conditionals, string functions, regex, recursive descent, and type coercion.


yq is written in Go and ships as a single dependency-free binary for Linux, macOS, and Windows. It is available via Homebrew, snap, apt (via PPA), Docker, pip, and direct download. Licensed under MIT, it maintains an active release cadence with the latest version being v4.52.4. For any agent working with configuration files, Helm values, Kubernetes manifests, or data transformation pipelines, yq provides the foundation for precise, scriptable edits without manual file manipulation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yq-yaml-structured-data-processor/)
