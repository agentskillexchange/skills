---
title: "Broken Link Verification for Static Sites and Documentation"
description: "This entry turns htmltest into a documentation QA skill with a clear operator job: inspect a built static site or generated docs directory, crawl its HTML output, and report broken links, missing anchors, and other navigation failures before the content ships. htmltest is a Go-based tool that works on generated HTML rather than source markdown, which makes it valuable after docs are rendered by MkDocs, Hugo, Docusaurus, Jekyll, or custom publishing pipelines. An agent can run it as the final gate that checks whether the output users will actually click through still holds together. The best time to invoke this skill is after a documentation build, before a site deploy, or during a repository cleanup where stale pages and renamed anchors may have left behind dead references. It is also useful in migration projects, versioned docs updates, and nightly validation jobs for sites that pull content from multiple sources. The agent behavior is concrete: run the scan, summarize the broken routes, distinguish internal anchor failures from outbound URL failures, and point maintainers to the exact generated pages that need correction. The scope boundary is tight. This is not a generic crawler, not a static site generator listing, and not a broad web testing framework card. The job-to-be-done is specifically broken link verification on generated HTML documentation or static sites . Integration points include CI jobs, docs preview pipelines, release gates, and local build verification. Upstream evidence is sufficient: the official GitHub repository exists, the Go package docs are live, tagged releases exist, the MIT license is present, and the project has meaningful adoption even though maintenance is slower than the other two accepted entries."
source: "https://github.com/wjdp/htmltest"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wjdp/htmltest"
  github_stars: 371
---

# Broken Link Verification for Static Sites and Documentation

This entry turns htmltest into a documentation QA skill with a clear operator job: inspect a built static site or generated docs directory, crawl its HTML output, and report broken links, missing anchors, and other navigation failures before the content ships. htmltest is a Go-based tool that works on generated HTML rather than source markdown, which makes it valuable after docs are rendered by MkDocs, Hugo, Docusaurus, Jekyll, or custom publishing pipelines. An agent can run it as the final gate that checks whether the output users will actually click through still holds together. The best time to invoke this skill is after a documentation build, before a site deploy, or during a repository cleanup where stale pages and renamed anchors may have left behind dead references. It is also useful in migration projects, versioned docs updates, and nightly validation jobs for sites that pull content from multiple sources. The agent behavior is concrete: run the scan, summarize the broken routes, distinguish internal anchor failures from outbound URL failures, and point maintainers to the exact generated pages that need correction. The scope boundary is tight. This is not a generic crawler, not a static site generator listing, and not a broad web testing framework card. The job-to-be-done is specifically broken link verification on generated HTML documentation or static sites . Integration points include CI jobs, docs preview pipelines, release gates, and local build verification. Upstream evidence is sufficient: the official GitHub repository exists, the Go package docs are live, tagged releases exist, the MIT license is present, and the project has meaningful adoption even though maintenance is slower than the other two accepted entries.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broken-link-verification-static-sites-documentation/)
