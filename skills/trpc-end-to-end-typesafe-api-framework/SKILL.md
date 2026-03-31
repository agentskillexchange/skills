---
name: "tRPC End-to-End Typesafe API Framework"
description: "tRPC enables developers to build fully typesafe APIs in TypeScript without schemas, code generation, or runtime bloat. The client infers server types directly, providing autocompletion for inputs, outputs, and errors. It supports request batching, subscriptions, and adapters for Next.js, Express, Fastify, and many other frameworks."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/trpc/trpc"
---
# tRPC End-to-End Typesafe API Framework

tRPC enables developers to build fully typesafe APIs in TypeScript without schemas, code generation, or runtime bloat. The client infers server types directly, providing autocompletion for inputs, outputs, and errors. It supports request batching, subscriptions, and adapters for Next.js, Express, Fastify, and many other frameworks.

## Overview

tRPC is a TypeScript RPC framework that eliminates the gap between server and client type definitions. Instead of defining API schemas in OpenAPI, GraphQL SDL, or Protocol Buffers and then generating client code, tRPC lets the client import the server’s type definitions directly. When a server-side procedure changes its input or output shape, TypeScript immediately flags type errors on the client before the code even runs.

The framework uses a procedure-based model where developers define queries, mutations, and subscriptions as typed functions on the server. Each procedure specifies its input validation using libraries like Zod, Valibot, or ArkType, and tRPC infers the validated types through to the client. This means the client gets full autocompletion on request parameters and response data without any manual type declarations or generated client code.

tRPC includes built-in request batching: multiple procedure calls made in the same event loop tick are automatically combined into a single HTTP request and split back apart on the server. This reduces network overhead without requiring developers to think about batching logic. The framework also supports real-time subscriptions via WebSockets or Server-Sent Events, enabling push-based data flows with the same type safety as regular queries.

Official adapters exist for Next.js (both App Router and Pages Router), Express, Fastify, and standalone HTTP servers. Community adapters cover SvelteKit, Nuxt, Remix, Astro, AWS Lambda, Cloudflare Workers, and more. The React integration provides hooks built on TanStack Query (React Query), delivering caching, optimistic updates, and infinite queries out of the box. There are also clients for Vue, Svelte, Solid, and vanilla TypeScript.

tRPC has zero runtime dependencies and adds minimal bundle size to client applications. The project has accumulated massive adoption in the TypeScript ecosystem, is MIT-licensed, and is actively maintained with regular releases. It is widely used in production by teams building full-stack TypeScript applications where type safety across the network boundary is critical.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill trpc-end-to-end-typesafe-api-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill trpc-end-to-end-typesafe-api-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill trpc-end-to-end-typesafe-api-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill trpc-end-to-end-typesafe-api-framework -a codex
```

### OpenClaw

```bash
clawhub install trpc-end-to-end-typesafe-api-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trpc-end-to-end-typesafe-api-framework/)
