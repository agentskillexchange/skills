---
title: "onefetch Git Repository Information and Statistics CLI"
description: "Overview onefetch is a command-line information tool for Git repositories, written in Rust. Think of it as neofetch for your code projects — it generates a visual summary of a repository including language breakdown, contributor statistics, license, version, creation date, lines of code, and more, all displayed alongside an ASCII art logo of the dominant programming language. Key Features Language Detection: onefetch detects and displays the programming language breakdown of a repository with percentage statistics, supporting over 100 languages. ASCII Art Logos: Each detected language has a hand-crafted ASCII art logo displayed alongside repository information, making output visually distinctive. Git Statistics: Shows commit count, contributor count, repository age, lines of code, last change date, repository URL, version (from tags), and pending changes. License Detection: Automatically detects the license type from LICENSE files in the repository. JSON and YAML Output: Structured output via --output json or --output yaml for programmatic consumption by scripts and agents. Customization: Disable specific info lines, change ASCII art colors, use custom images instead of ASCII logos, and configure which languages to show or hide. How It Works An agent skill using onefetch allows AI agents to quickly gather comprehensive repository metadata before starting work on a project. The agent runs onefetch --output json in the repository root to get structured data about the project&#8217;s languages, size, contributors, license, and version. This context helps the agent understand the project&#8217;s technology stack, maturity, and scale before making changes. Technical Details onefetch is written in Rust and distributed via cargo install onefetch , Homebrew, and system package managers. It reads repository data directly from the Git index and working tree, using tree-sitter for accurate language detection. The tool runs entirely locally with no network calls. It is licensed under MIT with over 11,700 GitHub stars and very active development with recent commits. The tool supports operation on partial clones and shallow repositories. Integration Points JSON/YAML output for structured data consumption Git hook integration to display project info on clone or pull CI/CD pipelines for project metadata extraction Composable with other CLI tools through standard Unix pipes"
source: "https://github.com/o2sh/onefetch"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "o2sh/onefetch"
  github_stars: 11710
---

# onefetch Git Repository Information and Statistics CLI

Overview onefetch is a command-line information tool for Git repositories, written in Rust. Think of it as neofetch for your code projects — it generates a visual summary of a repository including language breakdown, contributor statistics, license, version, creation date, lines of code, and more, all displayed alongside an ASCII art logo of the dominant programming language. Key Features Language Detection: onefetch detects and displays the programming language breakdown of a repository with percentage statistics, supporting over 100 languages. ASCII Art Logos: Each detected language has a hand-crafted ASCII art logo displayed alongside repository information, making output visually distinctive. Git Statistics: Shows commit count, contributor count, repository age, lines of code, last change date, repository URL, version (from tags), and pending changes. License Detection: Automatically detects the license type from LICENSE files in the repository. JSON and YAML Output: Structured output via --output json or --output yaml for programmatic consumption by scripts and agents. Customization: Disable specific info lines, change ASCII art colors, use custom images instead of ASCII logos, and configure which languages to show or hide. How It Works An agent skill using onefetch allows AI agents to quickly gather comprehensive repository metadata before starting work on a project. The agent runs onefetch --output json in the repository root to get structured data about the project&#8217;s languages, size, contributors, license, and version. This context helps the agent understand the project&#8217;s technology stack, maturity, and scale before making changes. Technical Details onefetch is written in Rust and distributed via cargo install onefetch , Homebrew, and system package managers. It reads repository data directly from the Git index and working tree, using tree-sitter for accurate language detection. The tool runs entirely locally with no network calls. It is licensed under MIT with over 11,700 GitHub stars and very active development with recent commits. The tool supports operation on partial clones and shallow repositories. Integration Points JSON/YAML output for structured data consumption Git hook integration to display project info on clone or pull CI/CD pipelines for project metadata extraction Composable with other CLI tools through standard Unix pipes

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/onefetch-git-repository-info-statistics-cli/)
