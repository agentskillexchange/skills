---
name: "Hurl Declarative HTTP Request Runner and Tester"
description: "Hurl is a command-line tool for running and testing HTTP requests defined in plain text files. Built on libcurl, it supports chaining multiple requests, capturing values, asserting responses with JSONPath and XPath, and integrating into CI/CD pipelines — making it ideal for API testing, integration testing, and endpoint validation."
verification: security_reviewed
source: "https://github.com/Orange-OpenSource/hurl"
category:
  - "Developer Tools"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hurl-declarative-http-request-runner-tester/)
