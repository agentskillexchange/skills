---
name: "WorkOS AuthKit Next.js Authentication Toolkit"
slug: "workos-authkit-nextjs-authentication-toolkit"
description: "WorkOS AuthKit is a real authentication toolkit for Next.js applications. It gives agents a concrete integration target for login, sessions, RBAC, SSO, MFA, and user management backed by WorkOS docs and package releases."
github_stars: 146
verification: "listed"
source: "https://github.com/workos/authkit-nextjs"
author: "workos"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "workos/authkit-nextjs"
  github_stars: 146
  npm_package: "@workos-inc/authkit-nextjs"
  npm_weekly_downloads: 227207
---

# WorkOS AuthKit Next.js Authentication Toolkit

WorkOS AuthKit is a real authentication toolkit for Next.js applications. It gives agents a concrete integration target for login, sessions, RBAC, SSO, MFA, and user management backed by WorkOS docs and package releases.

## Prerequisites

npm, pnpm, yarn, docker, go, rust, java

## Installation

Use the upstream install or setup path that matches your environment:
- pnpm i @workos-inc/authkit-nextjs
- yarn add @workos-inc/authkit-nextjs
- Make sure the following values are present in your .env.local environment variables file. The client ID and API key can be found in the [WorkOS dashboard](https://dashboard.workos.com), and the redirect URI can also b...
- Make sure this route matches the WORKOS_REDIRECT_URI variable and the configured redirect URI in your WorkOS dashboard. For instance if your redirect URI is http://localhost:3000/auth/callback then you'd put the above...

Requirements and caveats from upstream:
- WorkOS requires that you have a callback URL to redirect users back to after they've authenticated. In your Next.js app, [expose an API route](https://nextjs.org/docs/app/building-your-application/routing/route-handle...
- When running in environments like Docker, set the baseURL explicitly to ensure the redirects point to the correct location.
- | baseURL | undefined | The base URL to use for the redirect URI instead of the one in the request. **Required** if the app is being run in a container like docker where the hostname can be different from the one in t...

Basic usage or getting-started notes:
- or
- ## Video tutorial
- <a href="https://youtu.be/W8TmptLkEvA?feature=shared" target="_blank">

- Source: https://github.com/workos/authkit-nextjs
- Extracted from upstream docs: https://raw.githubusercontent.com/workos/authkit-nextjs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/workos-authkit-nextjs-authentication-toolkit/)
