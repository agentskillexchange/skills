---
name: "Katana Next-Generation Web Crawling and Spidering Framework"
description: "Katana by ProjectDiscovery is a fast, configurable web crawling and spidering framework written in Go. It supports standard and headless browser modes, JavaScript parsing, automatic form filling, and structured output for feeding into security and data pipelines."
category: "Research &amp; Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/projectdiscovery/katana"
tool_ecosystem:
  github_repo: "projectdiscovery/katana"
  github_stars: 16388
---
# Katana Next-Generation Web Crawling and Spidering Framework

Katana by ProjectDiscovery is a fast, configurable web crawling and spidering framework written in Go. It supports standard and headless browser modes, JavaScript parsing, automatic form filling, and structured output for feeding into security and data pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill katana-web-crawling-spidering-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill katana-web-crawling-spidering-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill katana-web-crawling-spidering-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill katana-web-crawling-spidering-framework -a codex
```

### OpenClaw

```bash
clawhub install katana-web-crawling-spidering-framework
```

## Details

Katana is a next-generation web crawling and spidering framework built by ProjectDiscovery, the team behind Nuclei, httpx, and other widely-used security tools. Written in Go for high performance, Katana is designed to systematically discover URLs, endpoints, JavaScript files, and API routes across web applications with both standard HTTP and headless browser crawling modes.

With over 16,000 GitHub stars, Katana has quickly become a standard tool in the security researcher and bug bounty toolkit. It bridges the gap between simple URL crawlers and full browser automation frameworks by offering JavaScript rendering without the overhead of maintaining browser state.

Crawling Modes
Katana operates in two modes. Standard mode uses Go HTTP clients for fast, lightweight crawling that follows links and parses HTML without executing JavaScript. Headless mode launches a Chrome/Chromium instance to render pages fully, executing JavaScript and capturing dynamically generated URLs. Users can connect to an existing browser session via WebSocket URL, enabling crawling of authenticated pages where the user has already logged in.

Scope and Configuration
The framework provides fine-grained scope control through preconfigured field filters and regex patterns. Crawl depth, concurrency, rate limiting, and delay between requests are all configurable. Katana supports automatic form filling with customizable field values, allowing it to traverse multi-step flows and discover endpoints behind form submissions.

Output and Integration
Output modes include STDOUT for piping into other tools, file output, and structured JSON. Custom output fields let users select exactly what data to capture: URLs, response codes, content types, technologies detected, and more. This makes Katana ideal for chaining with other ProjectDiscovery tools like Nuclei for vulnerability scanning or httpx for HTTP probing.

Agent Skill Use Cases
As an agent skill, Katana enables automated web reconnaissance. An AI agent can use it to map the complete URL surface of a web application, discover hidden API endpoints, find JavaScript files containing secrets or configuration data, and feed discovered URLs into downstream security scanning tools. The tool is distributed as a Go binary, Docker image, and available via package managers. It is MIT-licensed and receives frequent updates from the ProjectDiscovery team.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/katana-web-crawling-spidering-framework/)
