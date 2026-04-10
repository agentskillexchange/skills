---
name: Nock HTTP Server Mocking and Expectations Library for Node.js
description: Nock is an HTTP server mocking and expectations library for Node.js that
  intercepts outgoing HTTP requests and provides programmable responses. With over
  13,000 GitHub stars and 5.5 million weekly npm downloads, it is one of the most
  widely used testing utilities in the JavaScript ecosystem.
verification: security_reviewed
source: https://github.com/nock/nock
category:
- Code Quality &amp; Review
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: nock/nock
  github_stars: 13101
---
# Nock HTTP Server Mocking and Expectations Library for Node.js

Nock is a battle-tested HTTP server mocking library for Node.js that works by overriding Node's http.request and http.ClientRequest functions. It allows developers to test modules that perform HTTP requests in complete isolation, without hitting real external services. This makes test suites faster, more reliable, and deterministic.
The library provides a fluent API for defining interceptors that match specific URLs, HTTP methods, request headers, query parameters, and request bodies. Developers can specify exact responses including status codes, headers, and response bodies (as strings, JSON objects, or streams). Nock supports all HTTP verbs, HTTPS, non-standard ports, and can handle complex scenarios like delayed responses, connection timeouts, and network errors.
Key capabilities include scope-based request matching with regex and function filters, request body matching with multiple strategies (string, buffer, regex, JSON, function), response chaining for multi-step API interactions, and a recording mode that captures real HTTP traffic for replay in tests. The .persist() method keeps interceptors active across multiple requests, while .times(n) allows precise control over how many times an interceptor responds.
For AI coding agents, Nock is essential when building or testing any Node.js code that calls external APIs. Agents can use it to mock third-party service responses (GitHub API, Stripe, AWS, etc.) during test generation, ensuring tests run offline and consistently. Integration with popular test frameworks like Jest, Mocha, and Vitest is seamless since Nock operates at the HTTP level.
Install via npm install --save-dev nock. The package requires Node.js and works with both CommonJS and ESM imports. Documentation is available at the GitHub repository with comprehensive examples covering every feature.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nock-http-server-mocking-nodejs/)
