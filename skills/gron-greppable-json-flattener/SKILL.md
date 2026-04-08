---
title: gron Greppable JSON Flattener
description: 'gron is a command-line tool by Tom Hudson that flattens JSON into discrete
  assignment statements, turning nested data into a greppable format. Instead of learning
  a dedicated query language, developers can use familiar Unix tools like grep, sed,
  and awk to search and filter JSON data. The tool supports reading from files, URLs,
  and standard input. The core idea is straightforward: given a JSON object, gron
  outputs each value as a path assignment like json.users[0].name = "Alice"; . This
  flat format lets you grep for any field name or value, and the full path in each
  line shows exactly where in the structure the match lives. This is especially useful
  for exploring large, poorly documented API responses where you know the value you
  want but not its location in the tree. gron also works in reverse. The --ungron
  flag (commonly aliased as ungron ) takes filtered assignment lines and reconstructs
  valid JSON. This enables a pattern where you pipe JSON through gron, grep for the
  fields you need, and ungron the result back into a clean JSON subset. Developers
  use this for extracting specific branches from configuration files, comparing JSON
  diffs, and building ad-hoc data pipelines without writing code. The output is valid
  JavaScript, meaning you can also use it in scripting contexts. gron supports colorized
  output, monochrome mode for piping, and a JSON stream output format via --json .
  It ships as a single Go binary with no runtime dependencies, available through Homebrew,
  Go install, and prebuilt releases for Linux, macOS, Windows, and FreeBSD. With over
  14,000 GitHub stars and an MIT license, gron has become a standard tool in the developer
  toolkit. It fills a gap between simple cat/grep workflows and full-featured JSON
  processors like jq, offering a zero-learning-curve approach to JSON exploration
  that works with existing shell knowledge.'
verification: security_reviewed
source: https://github.com/tomnomnom/gron
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: tomnomnom/gron
  github_stars: 14413
---

# gron Greppable JSON Flattener

gron is a command-line tool by Tom Hudson that flattens JSON into discrete assignment statements, turning nested data into a greppable format. Instead of learning a dedicated query language, developers can use familiar Unix tools like grep, sed, and awk to search and filter JSON data. The tool supports reading from files, URLs, and standard input. The core idea is straightforward: given a JSON object, gron outputs each value as a path assignment like json.users[0].name = "Alice"; . This flat format lets you grep for any field name or value, and the full path in each line shows exactly where in the structure the match lives. This is especially useful for exploring large, poorly documented API responses where you know the value you want but not its location in the tree. gron also works in reverse. The --ungron flag (commonly aliased as ungron ) takes filtered assignment lines and reconstructs valid JSON. This enables a pattern where you pipe JSON through gron, grep for the fields you need, and ungron the result back into a clean JSON subset. Developers use this for extracting specific branches from configuration files, comparing JSON diffs, and building ad-hoc data pipelines without writing code. The output is valid JavaScript, meaning you can also use it in scripting contexts. gron supports colorized output, monochrome mode for piping, and a JSON stream output format via --json . It ships as a single Go binary with no runtime dependencies, available through Homebrew, Go install, and prebuilt releases for Linux, macOS, Windows, and FreeBSD. With over 14,000 GitHub stars and an MIT license, gron has become a standard tool in the developer toolkit. It fills a gap between simple cat/grep workflows and full-featured JSON processors like jq, offering a zero-learning-curve approach to JSON exploration that works with existing shell knowledge.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gron-greppable-json-flattener/)
