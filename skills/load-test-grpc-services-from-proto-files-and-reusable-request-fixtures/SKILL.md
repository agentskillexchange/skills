---
name: "Load-test gRPC services from proto files and reusable request fixtures"
slug: "load-test-grpc-services-from-proto-files-and-reusable-request-fixtures"
description: "This ASE skill uses ghz to run repeatable gRPC load tests from proto files, protosets, or server reflection. An agent can replay request fixtures at controlled concurrency, capture latency and error rates, and export machine-readable reports for regression checks or performance investigations."
github_stars: 3315
verification: "security_reviewed"
source: "https://github.com/bojand/ghz"
author: "bojand"
publisher_type: "Open Source Project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bojand/ghz"
  github_stars: 3315
---

# Load-test gRPC services from proto files and reusable request fixtures

This ASE skill uses ghz to run repeatable gRPC load tests from proto files, protosets, or server reflection. An agent can replay request fixtures at controlled concurrency, capture latency and error rates, and export machine-readable reports for regression checks or performance investigations.

## Prerequisites

A gRPC service plus proto files, a protoset bundle, or server reflection, and representative request data

## Installation

Use the upstream install or setup path that matches your environment:
- brew install ghz
- git clone https://github.com/bojand/ghz
- make build
- go install github.com/bojand/ghz/cmd/ghz@latest

Requirements and caveats from upstream:
- **Install using Docker**
- DOCKER_BUILDKIT=1 docker build --output=/usr/local/bin --target=ghz-binary-built https://github.com/bojand/ghz.git
- --cert= File containing client certificate (public key), to present to the server. Must also provide -key option.

Basic usage or getting-started notes:
- ### Download
- Download a prebuilt executable binary for your operating system from the [GitHub releases page](https://github.com/bojand/ghz/releases).
- Unzip the archive and place the executable binary wherever you would like to run it from. Additionally consider adding the location directory in the PATH variable if you would like the ghz command to be available ever...

- Source: https://github.com/bojand/ghz
- Extracted from upstream docs: https://raw.githubusercontent.com/bojand/ghz/HEAD/README.md

## Documentation

- https://ghz.sh/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures/)
