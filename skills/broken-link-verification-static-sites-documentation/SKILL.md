---
title: "Broken Link Verification for Static Sites and Documentation"
description: "Uses htmltest to crawl generated documentation or static site output, detect broken internal and external links, and return a link-focused validation report before deploy. This is a narrow docs QA skill for agents validating already-built HTML, not a generic site generator or crawler listing."
verification: security_reviewed
source: "https://github.com/wjdp/htmltest"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# Broken Link Verification for Static Sites and Documentation

This entry turns htmltest into a documentation QA skill with a clear operator job: inspect a built static site or generated docs directory, crawl its HTML output, and report broken links, missing anchors, and other navigation failures before the content ships. htmltest is a Go-based tool that works on generated HTML rather than source markdown, which makes it valuable after docs are rendered by MkDocs, Hugo, Docusaurus, Jekyll, or custom publishing pipelines. An agent can run it as the final gate that checks whether the output users will actually click through still holds together.

The best time to invoke this skill is after a documentation build, before a site deploy, or during a repository cleanup where stale pages and renamed anchors may have left behind dead references. It is also useful in migration projects, versioned docs updates, and nightly validation jobs for sites that pull content from multiple sources. The agent behavior is concrete: run the scan, summarize the broken routes, distinguish internal anchor failures from outbound URL failures, and point maintainers to the exact generated pages that need correction.

The scope boundary is tight. This is not a generic crawler, not a static site generator listing, and not a broad web testing framework card. The job-to-be-done is specifically broken link verification on generated HTML documentation or static sites. Integration points include CI jobs, docs preview pipelines, release gates, and local build verification. Upstream evidence is sufficient: the official GitHub repository exists, the Go package docs are live, tagged releases exist, the MIT license is present, and the project has meaningful adoption even though maintenance is slower than the other two accepted entries.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broken-link-verification-static-sites-documentation/)
