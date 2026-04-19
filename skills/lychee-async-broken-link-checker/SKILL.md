---
title: "lychee Async Broken Link Checker for Websites and Documentation"
description: "lychee is a command-line link checker written in Rust that scans websites, documentation files, and codebases for broken hyperlinks and invalid email addresses. It operates asynchronously with configurable concurrency, making it dramatically faster than traditional link checkers when validating large documentation sets or crawling multi-page websites. The tool supports checking links in Markdown, HTML, reStructuredText, and plain text files. It handles HTTP/1.1 and HTTP/2 connections, follows redirects, respects robots.txt, and can validate mailto: links by checking MX records. lychee produces output in multiple formats including text, JSON, and Markdown, making it easy to integrate into CI/CD pipelines and automated quality checks. Installation options span virtually every platform: Homebrew and MacPorts on macOS, pacman/zypper/snap/apk on Linux, scoop/winget/chocolatey on Windows, plus cargo install, Docker images, Nix packages, and conda-forge. A dedicated GitHub Action ( lycheeverse/lychee-action ) enables automated link checking on every pull request, catching broken documentation links before they reach production. Key features include regex-based URL filtering to exclude known-flaky endpoints, configurable timeout and retry settings, cookie support for authenticated pages, and caching of results to speed up subsequent runs. The tool can accept base URLs to resolve relative links and supports custom headers for API documentation behind authentication. For SEO and content quality workflows, lychee serves as an essential automated audit tool. An agent skill built around lychee can periodically scan a website&#8217;s sitemap or documentation directory, report broken internal and external links with their source locations, and generate actionable fix lists. With over 2,000 GitHub stars and active maintenance, lychee has become the standard choice for documentation link validation in open-source projects including Rust itself, Kubernetes, and many others."
source: "https://github.com/lycheeverse/lychee"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "lycheeverse/lychee"
  github_stars: 3463
---

# lychee Async Broken Link Checker for Websites and Documentation

lychee is a command-line link checker written in Rust that scans websites, documentation files, and codebases for broken hyperlinks and invalid email addresses. It operates asynchronously with configurable concurrency, making it dramatically faster than traditional link checkers when validating large documentation sets or crawling multi-page websites. The tool supports checking links in Markdown, HTML, reStructuredText, and plain text files. It handles HTTP/1.1 and HTTP/2 connections, follows redirects, respects robots.txt, and can validate mailto: links by checking MX records. lychee produces output in multiple formats including text, JSON, and Markdown, making it easy to integrate into CI/CD pipelines and automated quality checks. Installation options span virtually every platform: Homebrew and MacPorts on macOS, pacman/zypper/snap/apk on Linux, scoop/winget/chocolatey on Windows, plus cargo install, Docker images, Nix packages, and conda-forge. A dedicated GitHub Action ( lycheeverse/lychee-action ) enables automated link checking on every pull request, catching broken documentation links before they reach production. Key features include regex-based URL filtering to exclude known-flaky endpoints, configurable timeout and retry settings, cookie support for authenticated pages, and caching of results to speed up subsequent runs. The tool can accept base URLs to resolve relative links and supports custom headers for API documentation behind authentication. For SEO and content quality workflows, lychee serves as an essential automated audit tool. An agent skill built around lychee can periodically scan a website&#8217;s sitemap or documentation directory, report broken internal and external links with their source locations, and generate actionable fix lists. With over 2,000 GitHub stars and active maintenance, lychee has become the standard choice for documentation link validation in open-source projects including Rust itself, Kubernetes, and many others.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lychee-async-broken-link-checker/)
