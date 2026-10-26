---
name: "fd Fast File Finder CLI"
slug: "fd-fast-file-finder-cli"
description: "A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness."
github_stars: 42280
verification: "security_reviewed"
source: "https://github.com/sharkdp/fd"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "sharkdp/fd"
  github_stars: 42280
---

# fd Fast File Finder CLI

A fast and user-friendly alternative to the find command, written in Rust. fd provides intuitive syntax, regex and glob support, colorized output, parallel execution, and automatic .gitignore awareness.

## Installation

On macOS or Linux with Homebrew already installed, install the upstream `fd`
package:

```sh
brew install fd
```

Verify that the executable is available and inspect its options:

```sh
fd --version
fd --help
```

From a test directory, run `fd .` to list matching paths without changing files.
By default, fd respects ignore rules and omits hidden files. Review its options
before broadening the search scope or using commands that act on matched files.

For other operating systems and package managers, follow the
[upstream installation guide](https://github.com/sharkdp/fd#installation).

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fd-fast-file-finder-cli/)
