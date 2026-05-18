---
name: "Generate XML sitemaps and robots.txt from route inventories before SEO launch"
slug: "generate-xml-sitemaps-and-robots-txt-from-route-inventories-before-seo-launch"
description: "Use sitemap when an agent already knows the site routes or content URLs and needs valid sitemap XML, sitemap indexes, or robots.txt references before launch. This is a publishing-artifact skill, not a crawler or SEO platform."
github_stars: 1708
verification: "listed"
source: "https://github.com/ekalinin/sitemap.js"
author: "Eugene Kalinin"
category: "Content Writing & SEO"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ekalinin/sitemap.js"
  github_stars: 1708
---

# Generate XML sitemaps and robots.txt from route inventories before SEO launch

Use sitemap when an agent already knows the site routes or content URLs and needs valid sitemap XML, sitemap indexes, or robots.txt references before launch. This is a publishing-artifact skill, not a crawler or SEO platform.

## Prerequisites

Node.js, npm

## Installation

Use the upstream install or setup path that matches your environment:
- npm install --save sitemap
- npx sitemap < listofurls.txt # npx sitemap -h for more examples and a list of options.

Requirements and caveats from upstream:
- # sitemap ![MIT License](https://img.shields.io/npm/l/sitemap)[![Build Status](https://github.com/ekalinin/sitemap.js/workflows/Node%20CI/badge.svg)](https://github.com/ekalinin/sitemap.js/actions)![Monthly Downloads]...
- const { SitemapStream, streamToPromise } = require('sitemap')
- const { Readable } = require('stream')

Basic usage or getting-started notes:
- [Example of using sitemap.js with](#serve-a-sitemap-from-a-server-and-periodically-update-it) [express](https://expressjs.com/)
- sh
- ## Generate a one time sitemap from a list of urls

- Source: https://github.com/ekalinin/sitemap.js
- Extracted from upstream docs: https://raw.githubusercontent.com/ekalinin/sitemap.js/HEAD/README.md

## Documentation

- https://github.com/ekalinin/sitemap.js#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-xml-sitemaps-and-robots-txt-from-route-inventories-before-seo-launch/)
