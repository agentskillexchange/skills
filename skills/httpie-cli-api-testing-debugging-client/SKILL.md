---
name: HTTPie CLI API Testing and Debugging Client
description: HTTPie is a modern, user-friendly command-line HTTP client designed for
  testing, debugging, and interacting with APIs and HTTP servers. It provides an intuitive
  syntax with formatted and colorized terminal output, built-in JSON support, and
  session persistence.
category: Developer Tools
framework: Claude Code
verification: security_reviewed
source: "https://github.com/httpie/cli"
tool_ecosystem:
  github_repo: "https://github.com/httpie/cli"
  github_stars: 37814
---
# HTTPie CLI API Testing and Debugging Client

HTTPie is a modern, user-friendly command-line HTTP client designed for testing, debugging, and interacting with APIs and HTTP servers. It provides an intuitive syntax with formatted and colorized terminal output, built-in JSON support, and session persistence.

HTTPie (pronounced aitch-tee-tee-pie) is a command-line HTTP client built for developers who spend time working with APIs and web services. Available on PyPI as the httpie package with over 34,000 GitHub stars, it has become one of the most widely-used alternatives to curl for API interaction.

The tool provides a natural, expressive syntax for constructing HTTP requests. Instead of memorizing flag combinations, developers write requests that read almost like plain English. A simple GET request is just http httpie.io/hello, while a POST with JSON data and custom headers uses the format http PUT api.example.com/resource X-API-Token:123 name=John. HTTPie automatically serializes JSON request bodies, sets appropriate content-type headers, and formats response output with syntax highlighting.

Beyond basic request construction, HTTPie supports persistent sessions that remember headers and authentication between requests, wget-like file downloads, form submissions and file uploads, HTTPS with configurable SSL verification, proxy configuration, and multiple authentication methods including Basic, Digest, and Bearer token auth. The plugin architecture allows extending functionality through third-party auth plugins and output formatters.

An agent skill built around HTTPie enables automated API testing workflows, endpoint verification, response validation, and integration testing. The skill can construct complex request chains, parse structured JSON responses, and report on API health. It integrates naturally into CI/CD pipelines and developer toolchains where readable HTTP interactions matter more than raw performance.

HTTPie is MIT-licensed and available via pip, Homebrew, apt, and most package managers. The project is actively maintained with regular releases and comprehensive documentation at httpie.io.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill httpie-cli-api-testing-debugging-client
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill httpie-cli-api-testing-debugging-client -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill httpie-cli-api-testing-debugging-client -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill httpie-cli-api-testing-debugging-client -a codex
```

### OpenClaw

```bash
clawhub install httpie-cli-api-testing-debugging-client
```


## Source

- [GitHub](https://github.com/httpie/cli)
