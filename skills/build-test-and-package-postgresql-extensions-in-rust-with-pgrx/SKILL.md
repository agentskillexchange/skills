---
name: "Build, test, and package PostgreSQL extensions in Rust with pgrx"
slug: "build-test-and-package-postgresql-extensions-in-rust-with-pgrx"
description: "Use pgrx when an agent needs the Rust-native extension lifecycle for PostgreSQL, including local builds, test runs, and packaging across PostgreSQL versions."
github_stars: 4458
verification: "security_reviewed"
source: "https://github.com/pgcentralfoundation/pgrx"
author: "PgCentral Foundation"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pgcentralfoundation/pgrx"
  github_stars: 4458
---

# Build, test, and package PostgreSQL extensions in Rust with pgrx

Use pgrx when an agent needs the Rust-native extension lifecycle for PostgreSQL, including local builds, test runs, and packaging across PostgreSQL versions.

## Prerequisites

Rust toolchain, PostgreSQL development dependencies, and pgrx

## Installation

Use the upstream install or setup path that matches your environment:
- brew install git icu4c pkg-config
- on the command line before you run cargo pgrx init
- project and the old directory has disappeared. The solution is re-run cargo pgrx init so the
- cargo install --locked cargo-pgrx

Requirements and caveats from upstream:
- † PGRX has no MSRV policy, thus may require the latest stable version of Rust, available via Rustup
- Running PGRX on a Mac requires some additional setup.
- This can be fixed by updating Xcode and the command-line tools. You may require an OS update

Basic usage or getting-started notes:
- cargo pgrx run: Run your extension and interactively test it in psql (or pgcli)
- To fix it, run
- Before anything else, install the [system dependencies](#system-requirements).

- Source: https://github.com/pgcentralfoundation/pgrx
- Extracted from upstream docs: https://raw.githubusercontent.com/pgcentralfoundation/pgrx/HEAD/README.md

## Documentation

- https://github.com/pgcentralfoundation/pgrx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-test-and-package-postgresql-extensions-in-rust-with-pgrx/)
