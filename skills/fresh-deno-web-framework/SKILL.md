---
name: "Fresh Next-Generation Web Framework for Deno"
description: "Fresh is a next-generation web framework built for Deno that uses island-based client hydration, ships zero JavaScript to the client by default, and provides file-system routing with TypeScript support out of the box."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/denoland/fresh"
tool_ecosystem:
  github_repo: "denoland/fresh"
  github_stars: 13714
---
# Fresh Next-Generation Web Framework for Deno

Fresh is a next-generation web framework built for Deno that uses island-based client hydration, ships zero JavaScript to the client by default, and provides file-system routing with TypeScript support out of the box.

Fresh is a web framework created by the Deno team that takes a fundamentally different approach to client-side JavaScript. By default, Fresh ships zero JavaScript to the client, using island-based architecture to selectively hydrate only the interactive components that need client-side code.



Architecture

Fresh uses an island-based client hydration model where the majority of rendering happens on the server. Only explicitly marked interactive components (islands) receive client-side JavaScript, resulting in dramatically faster page loads and smaller bundle sizes. This approach draws from the islands architecture pattern popularized by frameworks like Astro but is deeply integrated into the framework.



Developer Experience

The framework requires no build step or configuration to get started. It provides file-system routing similar to Next.js, full TypeScript support out of the box via Deno, and uses Preact for the component layer. Scaffolding a new project takes a single command: deno run -Ar jsr:@fresh/init, and the development server starts with deno task dev.



Performance

By eliminating unnecessary client-side JavaScript, Fresh achieves exceptional performance metrics. Pages load faster because the browser has less JavaScript to parse and execute. The server-side rendering ensures content is immediately visible, while islands provide interactivity exactly where needed without bloating the rest of the page.



Deployment

Fresh projects deploy seamlessly to Deno Deploy, requiring only a GitHub push and project creation on the Deno Deploy console. Projects receive public subdomains automatically with no configuration required. The framework also supports standard Deno deployment options for self-hosted scenarios.



Ecosystem

Fresh leverages the Deno ecosystem including JSR (JavaScript Registry) for package management and the Deno standard library. It supports web standard APIs and integrates with the broader Preact plugin ecosystem for UI components and utilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill fresh-deno-web-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill fresh-deno-web-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill fresh-deno-web-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill fresh-deno-web-framework -a codex
```

### OpenClaw

```bash
clawhub install fresh-deno-web-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fresh-deno-web-framework/)
