---
title: "Hurl Declarative HTTP Request Runner and Tester"
description: "What is Hurl?\nHurl is an open-source HTTP request runner created by Orange (the telecommunications company). Written in Rust and built on top of libcurl, it uses a simple plain-text file format to define HTTP requests, capture response data, and assert expected outcomes. With over 18,600 GitHub stars and active development (commits daily), Hurl has become one of the most popular tools for declarative API testing.\nHow It Works\nYou write .hurl files that describe HTTP requests in a human-readable format. Each file can contain multiple requests that execute sequentially. Between requests, you can capture values from headers, JSON bodies (using JSONPath), or HTML (using XPath) and reuse them in subsequent requests. Assertions validate status codes, headers, body content, response times, and more. Hurl processes these files from the command line, making it trivial to integrate into CI pipelines, Makefiles, or shell scripts.\nUnlike Postman collections or complex testing frameworks, Hurl files are plain text with no JSON overhead. A typical request-response pair reads almost like documentation. The tool supports all HTTP methods, file uploads, multipart forms, cookies, basic and bearer auth, client certificates, and HTTP/2. Variables can be injected from the command line or environment, enabling parameterized test suites across environments.\nWhat It Produces\nHurl outputs response bodies, test results (pass/fail with detailed error messages), JUnit XML reports for CI integration, and HTML reports for human review. In test mode (--test), it provides a compact summary showing which assertions passed or failed. The --json flag outputs structured results for programmatic consumption.\nIntegration and Installation\nHurl is available via Homebrew, Snap, Chocolatey, Scoop, Arch AUR, Conda, npm (@anthropic-ai/hurl), and as standalone binaries for Linux, macOS, and Windows. It integrates naturally with GitHub Actions, GitLab CI, Jenkins, and any CI system that can run shell commands. The hurlfmt companion tool formats and converts Hurl files to other formats."
verification: security_reviewed
source: "https://github.com/Orange-OpenSource/hurl"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Orange-OpenSource/hurl"
  github_stars: 18696
---

# Hurl Declarative HTTP Request Runner and Tester

What is Hurl?
Hurl is an open-source HTTP request runner created by Orange (the telecommunications company). Written in Rust and built on top of libcurl, it uses a simple plain-text file format to define HTTP requests, capture response data, and assert expected outcomes. With over 18,600 GitHub stars and active development (commits daily), Hurl has become one of the most popular tools for declarative API testing.
How It Works
You write .hurl files that describe HTTP requests in a human-readable format. Each file can contain multiple requests that execute sequentially. Between requests, you can capture values from headers, JSON bodies (using JSONPath), or HTML (using XPath) and reuse them in subsequent requests. Assertions validate status codes, headers, body content, response times, and more. Hurl processes these files from the command line, making it trivial to integrate into CI pipelines, Makefiles, or shell scripts.
Unlike Postman collections or complex testing frameworks, Hurl files are plain text with no JSON overhead. A typical request-response pair reads almost like documentation. The tool supports all HTTP methods, file uploads, multipart forms, cookies, basic and bearer auth, client certificates, and HTTP/2. Variables can be injected from the command line or environment, enabling parameterized test suites across environments.
What It Produces
Hurl outputs response bodies, test results (pass/fail with detailed error messages), JUnit XML reports for CI integration, and HTML reports for human review. In test mode (--test), it provides a compact summary showing which assertions passed or failed. The --json flag outputs structured results for programmatic consumption.
Integration and Installation
Hurl is available via Homebrew, Snap, Chocolatey, Scoop, Arch AUR, Conda, npm (@anthropic-ai/hurl), and as standalone binaries for Linux, macOS, and Windows. It integrates naturally with GitHub Actions, GitLab CI, Jenkins, and any CI system that can run shell commands. The hurlfmt companion tool formats and converts Hurl files to other formats.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hurl-declarative-http-request-runner-tester
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hurl-declarative-http-request-runner-tester` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hurl-declarative-http-request-runner-tester/)
