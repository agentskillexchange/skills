---
title: "tRPC End-to-End Typesafe API Framework"
description: "tRPC is a TypeScript RPC framework that eliminates the gap between server and client type definitions. Instead of defining API schemas in OpenAPI, GraphQL SDL, or Protocol Buffers and then generating client code, tRPC lets the client import the server’s type definitions directly. When a server-side procedure changes its input or output shape, TypeScript immediately flags type errors on the client before the code even runs.\nThe framework uses a procedure-based model where developers define queries, mutations, and subscriptions as typed functions on the server. Each procedure specifies its input validation using libraries like Zod, Valibot, or ArkType, and tRPC infers the validated types through to the client. This means the client gets full autocompletion on request parameters and response data without any manual type declarations or generated client code.\ntRPC includes built-in request batching: multiple procedure calls made in the same event loop tick are automatically combined into a single HTTP request and split back apart on the server. This reduces network overhead without requiring developers to think about batching logic. The framework also supports real-time subscriptions via WebSockets or Server-Sent Events, enabling push-based data flows with the same type safety as regular queries.\nOfficial adapters exist for Next.js (both App Router and Pages Router), Express, Fastify, and standalone HTTP servers. Community adapters cover SvelteKit, Nuxt, Remix, Astro, AWS Lambda, Cloudflare Workers, and more. The React integration provides hooks built on TanStack Query (React Query), delivering caching, optimistic updates, and infinite queries out of the box. There are also clients for Vue, Svelte, Solid, and vanilla TypeScript.\ntRPC has zero runtime dependencies and adds minimal bundle size to client applications. The project has accumulated massive adoption in the TypeScript ecosystem, is MIT-licensed, and is actively maintained with regular releases. It is widely used in production by teams building full-stack TypeScript applications where type safety across the network boundary is critical."
verification: security_reviewed
source: "https://github.com/trpc/trpc"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "trpc/trpc"
  github_stars: 39862
---

# tRPC End-to-End Typesafe API Framework

tRPC is a TypeScript RPC framework that eliminates the gap between server and client type definitions. Instead of defining API schemas in OpenAPI, GraphQL SDL, or Protocol Buffers and then generating client code, tRPC lets the client import the server’s type definitions directly. When a server-side procedure changes its input or output shape, TypeScript immediately flags type errors on the client before the code even runs.
The framework uses a procedure-based model where developers define queries, mutations, and subscriptions as typed functions on the server. Each procedure specifies its input validation using libraries like Zod, Valibot, or ArkType, and tRPC infers the validated types through to the client. This means the client gets full autocompletion on request parameters and response data without any manual type declarations or generated client code.
tRPC includes built-in request batching: multiple procedure calls made in the same event loop tick are automatically combined into a single HTTP request and split back apart on the server. This reduces network overhead without requiring developers to think about batching logic. The framework also supports real-time subscriptions via WebSockets or Server-Sent Events, enabling push-based data flows with the same type safety as regular queries.
Official adapters exist for Next.js (both App Router and Pages Router), Express, Fastify, and standalone HTTP servers. Community adapters cover SvelteKit, Nuxt, Remix, Astro, AWS Lambda, Cloudflare Workers, and more. The React integration provides hooks built on TanStack Query (React Query), delivering caching, optimistic updates, and infinite queries out of the box. There are also clients for Vue, Svelte, Solid, and vanilla TypeScript.
tRPC has zero runtime dependencies and adds minimal bundle size to client applications. The project has accumulated massive adoption in the TypeScript ecosystem, is MIT-licensed, and is actively maintained with regular releases. It is widely used in production by teams building full-stack TypeScript applications where type safety across the network boundary is critical.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trpc-end-to-end-typesafe-api-framework
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/trpc-end-to-end-typesafe-api-framework` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trpc-end-to-end-typesafe-api-framework/)
