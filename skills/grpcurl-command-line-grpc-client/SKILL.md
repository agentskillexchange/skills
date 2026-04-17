---
title: "grpcurl Command-Line gRPC Client"
description: "grpcurl is a command-line tool developed by FullStory that enables interaction with gRPC servers in the same way curl works for HTTP/REST APIs. gRPC APIs are notoriously difficult to test manually because they use Protocol Buffers binary encoding rather than human-readable JSON, and standard HTTP tools cannot speak the HTTP/2-based gRPC wire protocol. grpcurl solves this by providing a curl-like interface that handles protobuf serialization, HTTP/2 framing, and gRPC-specific features transparently.\nThe grpcurl Command-Line gRPC Client skill gives agents the ability to discover, test, and debug gRPC services from the command line. grpcurl can connect to a gRPC server and use server reflection to discover available services and methods without needing local proto files. Running grpcurl localhost:50051 list lists all services, and grpcurl localhost:50051 describe mypackage.MyService shows the full service definition including request/response message schemas. For servers without reflection enabled, grpcurl accepts proto source files or compiled descriptor sets via the -proto or -protoset flags.\nInvoking RPCs is straightforward: grpcurl -d '{\"name\": \"world\"}' localhost:50051 helloworld.Greeter/SayHello sends a unary request with a JSON body and prints the response as formatted JSON. grpcurl supports all four gRPC communication patterns: unary, server streaming, client streaming, and bidirectional streaming. For streaming RPCs, multiple request messages can be sent by providing a series of JSON objects separated by newlines.\nThe tool handles TLS connections with configurable CA certificates, client certificates for mutual TLS, and an insecure mode for development. Custom metadata headers can be attached via -H flags, enabling authentication token injection and request tracing. grpcurl also supports Unix domain sockets, custom authority headers, and connect timeout configuration. Written in Go and distributed as a single static binary, grpcurl is installable via go install, Homebrew, and pre-built releases for Linux, macOS, and Windows. The underlying grpcurl Go package can also be used as a library for building custom gRPC tooling. With over 12,000 GitHub stars, an MIT license, and broad adoption in the gRPC ecosystem, grpcurl is the standard tool for command-line gRPC interaction."
verification: security_reviewed
source: "https://github.com/fullstorydev/grpcurl"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "fullstorydev/grpcurl"
  github_stars: 12548
---

# grpcurl Command-Line gRPC Client

grpcurl is a command-line tool developed by FullStory that enables interaction with gRPC servers in the same way curl works for HTTP/REST APIs. gRPC APIs are notoriously difficult to test manually because they use Protocol Buffers binary encoding rather than human-readable JSON, and standard HTTP tools cannot speak the HTTP/2-based gRPC wire protocol. grpcurl solves this by providing a curl-like interface that handles protobuf serialization, HTTP/2 framing, and gRPC-specific features transparently.
The grpcurl Command-Line gRPC Client skill gives agents the ability to discover, test, and debug gRPC services from the command line. grpcurl can connect to a gRPC server and use server reflection to discover available services and methods without needing local proto files. Running grpcurl localhost:50051 list lists all services, and grpcurl localhost:50051 describe mypackage.MyService shows the full service definition including request/response message schemas. For servers without reflection enabled, grpcurl accepts proto source files or compiled descriptor sets via the -proto or -protoset flags.
Invoking RPCs is straightforward: grpcurl -d '{"name": "world"}' localhost:50051 helloworld.Greeter/SayHello sends a unary request with a JSON body and prints the response as formatted JSON. grpcurl supports all four gRPC communication patterns: unary, server streaming, client streaming, and bidirectional streaming. For streaming RPCs, multiple request messages can be sent by providing a series of JSON objects separated by newlines.
The tool handles TLS connections with configurable CA certificates, client certificates for mutual TLS, and an insecure mode for development. Custom metadata headers can be attached via -H flags, enabling authentication token injection and request tracing. grpcurl also supports Unix domain sockets, custom authority headers, and connect timeout configuration. Written in Go and distributed as a single static binary, grpcurl is installable via go install, Homebrew, and pre-built releases for Linux, macOS, and Windows. The underlying grpcurl Go package can also be used as a library for building custom gRPC tooling. With over 12,000 GitHub stars, an MIT license, and broad adoption in the gRPC ecosystem, grpcurl is the standard tool for command-line gRPC interaction.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grpcurl-command-line-grpc-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/grpcurl-command-line-grpc-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grpcurl-command-line-grpc-client/)
