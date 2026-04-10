---
title: "grex Regular Expression Generator from Test Cases"
description: "grex is a command-line tool and library that automatically generates regular expressions from user-provided test cases. Written in Rust with Python bindings, it produces the most specific regex that matches the given input, supporting Unicode 16.0, character class detection, quantifier notation, and case-insensitive matching."
slug: "grex-regex-generator-from-test-cases"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/pemistahl/grex"
tool_ecosystem:
  github_repo: "pemistahl/grex"
  github_stars: 8079
---

# grex Regular Expression Generator from Test Cases

grex is a command-line tool and library that automatically generates regular expressions from user-provided test cases. Written in Rust with Python bindings, it produces the most specific regex that matches the given input, supporting Unicode 16.0, character class detection, quantifier notation, and case-insensitive matching.

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
clawhub install grex-regex-generator-from-test-cases
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

What is grex?
grex is a CLI tool and Rust library for generating regular expressions from example strings. Created by Peter M. Stahl, it has earned over 8,000 GitHub stars and is available on crates.io, PyPI (as the grex Python package), and through Homebrew, MacPorts, Chocolatey, and Scoop. The project started as a Rust port of the JavaScript tool regexgen but has since grown well beyond it in features.
How It Works
You provide grex with a set of test strings — either as command-line arguments or from a file — and it produces a single Perl-compatible regular expression guaranteed to match all provided inputs. By default, grex generates the most specific regex possible that matches only the given strings and nothing else. This behavior has been verified through property tests in the test suite.
Command-line flags control how general or specific the output is. You can enable conversion to shorthand character classes (\w, \d, \s), toggle anchors (^ and $), use case-insensitive matching, switch between capturing and non-capturing groups, and enable verbose multi-line output with syntax highlighting. The algorithm detects common prefixes, suffixes, repeated substrings, alternation patterns, and optional characters, converting them to appropriate regex quantifiers and operators.
What It Produces
The output is a single regex string written to stdout. With verbose mode enabled, the expression is indented across multiple lines for readability. grex is fully compliant with Unicode Standard 16.0 and correctly handles grapheme clusters consisting of multiple Unicode symbols. It also supports escaping non-ASCII characters and converting astral code points to surrogate pairs for environments that require it.
Use Cases and Integration
grex is useful for bootstrapping regex patterns for data validation, log parsing, input sanitization, and text extraction. Agents can pipe example strings into grex and receive a working regex pattern as output. The Python bindings allow direct integration in Python scripts and notebooks. As a Rust library, it can be embedded in any Rust application for regex generation at runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grex-regex-generator-from-test-cases/)
