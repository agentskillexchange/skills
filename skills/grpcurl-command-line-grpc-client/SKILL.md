---
title: "grpcurl Command-Line gRPC Client"
description: "Like cURL but for gRPC servers. A command-line tool for interacting with gRPC services using server reflection or proto files, supporting unary calls, streaming, TLS, and metadata headers."
slug: "grpcurl-command-line-grpc-client"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/fullstorydev/grpcurl"
tool_ecosystem:
  github_repo: "fullstorydev/grpcurl"
  github_stars: 12548
listed: true
---

# grpcurl Command-Line gRPC Client

Like cURL but for gRPC servers. A command-line tool for interacting with gRPC services using server reflection or proto files, supporting unary calls, streaming, TLS, and metadata headers.

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
clawhub install grpcurl-command-line-grpc-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

grpcurl is a command-line tool developed by FullStory that enables interaction with gRPC servers in the same way curl works for HTTP/REST APIs. gRPC APIs are notoriously difficult to test manually because they use Protocol Buffers binary encoding rather than human-readable JSON, and standard HTTP tools cannot speak the HTTP/2-based gRPC wire protocol. grpcurl solves this by providing a curl-like interface that handles protobuf serialization, HTTP/2 framing, and gRPC-specific features transparently.
The grpcurl Command-Line gRPC Client skill gives agents the ability to discover, test, and debug gRPC services from the command line. grpcurl can connect to a gRPC server and use server reflection to discover available services and methods without needing local proto files. Running grpcurl localhost:50051 list lists all services, and grpcurl localhost:50051 describe mypackage.MyService shows the full service definition including request/response message schemas. For servers without reflection enabled, grpcurl accepts proto source files or compiled descriptor sets via the -proto or -protoset flags.
Invoking RPCs is straightforward: grpcurl -d '{"name": "world"}' localhost:50051 helloworld.Greeter/SayHello sends a unary request with a JSON body and prints the response as formatted JSON. grpcurl supports all four gRPC communication patterns: unary, server streaming, client streaming, and bidirectional streaming. For streaming RPCs, multiple request messages can be sent by providing a series of JSON objects separated by newlines.
The tool handles TLS connections with configurable CA certificates, client certificates for mutual TLS, and an insecure mode for development. Custom metadata headers can be attached via -H flags, enabling authentication token injection and request tracing. grpcurl also supports Unix domain sockets, custom authority headers, and connect timeout configuration. Written in Go and distributed as a single static binary, grpcurl is installable via go install, Homebrew, and pre-built releases for Linux, macOS, and Windows. The underlying grpcurl Go package can also be used as a library for building custom gRPC tooling. With over 12,000 GitHub stars, an MIT license, and broad adoption in the gRPC ecosystem, grpcurl is the standard tool for command-line gRPC interaction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grpcurl-command-line-grpc-client/)
