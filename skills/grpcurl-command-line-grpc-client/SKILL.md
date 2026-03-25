---
name: "grpcurl Command-Line gRPC Client"
description: "Like cURL but for gRPC servers. A command-line tool for interacting with gRPC services using server reflection or proto files, supporting unary calls, streaming, TLS, and metadata headers."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/grpcurl-command-line-grpc-client/"
---

# grpcurl Command-Line gRPC Client

Like cURL but for gRPC servers. A command-line tool for interacting with gRPC services using server reflection or proto files, supporting unary calls, streaming, TLS, and metadata headers.

## Overview

grpcurl is a command-line tool developed by FullStory that enables interaction with gRPC servers in the same way curl works for HTTP/REST APIs. gRPC APIs are notoriously difficult to test manually because they use Protocol Buffers binary encoding rather than human-readable JSON, and standard HTTP tools cannot speak the HTTP/2-based gRPC wire protocol. grpcurl solves this by providing a curl-like interface that handles protobuf serialization, HTTP/2 framing, and gRPC-specific features transparently.

The grpcurl Command-Line gRPC Client skill gives agents the ability to discover, test, and debug gRPC services from the command line. grpcurl can connect to a gRPC server and use server reflection to discover available services and methods without needing local proto files. Running `grpcurl localhost:50051 list` lists all services, and `grpcurl localhost:50051 describe mypackage.MyService` shows the full service definition including request/response message schemas. For servers without reflection enabled, grpcurl accepts proto source files or compiled descriptor sets via the `-proto` or `-protoset` flags.

Invoking RPCs is straightforward: `grpcurl -d '{"name": "world"}' localhost:50051 helloworld.Greeter/SayHello` sends a unary request with a JSON body and prints the response as formatted JSON. grpcurl supports all four gRPC communication patterns: unary, server streaming, client streaming, and bidirectional streaming. For streaming RPCs, multiple request messages can be sent by providing a series of JSON objects separated by newlines.

The tool handles TLS connections with configurable CA certificates, client certificates for mutual TLS, and an insecure mode for development. Custom metadata headers can be attached via `-H` flags, enabling authentication token injection and request tracing. grpcurl also supports Unix domain sockets, custom authority headers, and connect timeout configuration. Written in Go and distributed as a single static binary, grpcurl is installable via `go install`, Homebrew, and pre-built releases for Linux, macOS, and Windows. The underlying grpcurl Go package can also be used as a library for building custom gRPC tooling. With over 12,000 GitHub stars, an MIT license, and broad adoption in the gRPC ecosystem, grpcurl is the standard tool for command-line gRPC interaction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grpcurl-command-line-grpc-client
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grpcurl-command-line-grpc-client -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grpcurl-command-line-grpc-client -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grpcurl-command-line-grpc-client -a codex
```

### OpenClaw

```bash
clawhub install grpcurl-command-line-grpc-client
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grpcurl-command-line-grpc-client/
