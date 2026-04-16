---
title: "Broken Link Verification for Static Sites and Documentation"
description: "Uses htmltest to crawl generated documentation or static site output, detect broken internal and external links, and return a link-focused validation report before deploy. This is a narrow docs QA skill for agents validating already-built HTML, not a generic site generator or crawler listing."
verification: "security_reviewed"
source: "https://github.com/wjdp/htmltest"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wjdp/htmltest"
  github_stars: 371
---

# Broken Link Verification for Static Sites and Documentation

This entry turns htmltest into a documentation QA skill with a clear operator job: inspect a built static site or generated docs directory, crawl its HTML output, and report broken links, missing anchors, and other navigation failures before the content ships. htmltest is a Go-based tool that works on generated HTML rather than source markdown, which makes it valuable after docs are rendered by MkDocs, Hugo, Docusaurus, Jekyll, or custom publishing pipelines. An agent can run it as the final gate that checks whether the output users will actually click through still holds together.


The best time to invoke this skill is after a documentation build, before a site deploy, or during a repository cleanup where stale pages and renamed anchors may have left behind dead references. It is also useful in migration projects, versioned docs updates, and nightly validation jobs for sites that pull content from multiple sources. The agent behavior is concrete: run the scan, summarize the broken routes, distinguish internal anchor failures from outbound URL failures, and point maintainers to the exact generated pages that need correction.


The scope boundary is tight. This is not a generic crawler, not a static site generator listing, and not a broad web testing framework card. The job-to-be-done is specifically broken link verification on generated HTML documentation or static sites. Integration points include CI jobs, docs preview pipelines, release gates, and local build verification. Upstream evidence is sufficient: the official GitHub repository exists, the Go package docs are live, tagged releases exist, the MIT license is present, and the project has meaningful adoption even though maintenance is slower than the other two accepted entries.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broken-link-verification-static-sites-documentation/)
