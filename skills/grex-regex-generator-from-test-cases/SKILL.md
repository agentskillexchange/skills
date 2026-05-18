---
name: "grex Regular Expression Generator from Test Cases"
slug: "grex-regex-generator-from-test-cases"
description: "grex is a command-line tool and library that automatically generates regular expressions from user-provided test cases. Written in Rust with Python bindings, it produces the most specific regex that matches the given input, supporting Unicode 16.0, character class detection, quantifier notation, and case-insensitive matching."
github_stars: 8079
verification: "listed"
source: "https://github.com/pemistahl/grex"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "pemistahl/grex"
  github_stars: 8079
---

# grex Regular Expression Generator from Test Cases

grex is a command-line tool and library that automatically generates regular expressions from user-provided test cases. Written in Rust with Python bindings, it produces the most specific regex that matches the given input, supporting Unicode 16.0, character class detection, quantifier notation, and case-insensitive matching.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/pemistahl/grex.git
- cargo build
- cargo test
- cargo bench

Requirements and caveats from upstream:
- [![python build status](https://github.com/pemistahl/grex/actions/workflows/python-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/python-build.yml)
- ![supported Python versions](https://img.shields.io/badge/Python-%3E%3D%203.12-blue?logo=Python&logoColor=yellow)
- Specifies the minimum length a repeated substring must have in order to be converted if

Basic usage or getting-started notes:
- Input:
- [INPUT]... One or more test cases separated by blank space
- -f, --file <FILE> Reads test cases on separate lines from a file

- Source: https://github.com/pemistahl/grex
- Extracted from upstream docs: https://raw.githubusercontent.com/pemistahl/grex/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grex-regex-generator-from-test-cases/)
