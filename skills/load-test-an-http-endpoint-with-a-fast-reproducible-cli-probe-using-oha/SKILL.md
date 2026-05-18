---
name: "Load-test an HTTP endpoint with a fast reproducible CLI probe using oha"
slug: "load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha"
description: "Run a quick concurrent HTTP benchmark against a URL before deeper performance work or regression triage."
github_stars: 10198
verification: "listed"
source: "https://github.com/hatoo/oha"
author: "hatoo"
publisher_type: "open_source_project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hatoo/oha"
  github_stars: 10198
---

# Load-test an HTTP endpoint with a fast reproducible CLI probe using oha

Run a quick concurrent HTTP benchmark against a URL before deeper performance work or regression triage.

## Prerequisites

oha

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install oha
- cargo install --no-default-features --features native-tls oha
- cargo install --features vsock oha
- brew install oha

Requirements and caveats from upstream:
- This program is built on stable Rust, with both make and cmake prerequisites to install via cargo.
- It will remain experimental as long as H3 is experimental. It currently depends on using rustls for TLS.
- ### Official Docker image

Basic usage or getting-started notes:
- You can optionally build oha against [native-tls](https://github.com/sfackler/rust-native-tls) instead of [rustls](https://github.com/rustls/rustls).
- You can enable VSOCK support by enabling vsock feature.
- You can enable experimental HTTP3 support by enabling the http3 feature. This uses the [H3](https://github.com/hyperium/h3) library by the developers of Hyper.

- Source: https://github.com/hatoo/oha
- Extracted from upstream docs: https://raw.githubusercontent.com/hatoo/oha/HEAD/README.md

## Documentation

- https://github.com/hatoo/oha

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha/)
