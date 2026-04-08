---
title: Karakeep Self-Hosted Bookmark Manager with AI Tagging
description: Karakeep, previously known as Hoarder, is a self-hosted bookmark management
  application designed for data hoarders who want full control over their saved content.
  With over 24,000 GitHub stars and active development, it provides AI-powered automatic
  tagging, full-text search, and comprehensive content archiving through a modern
  web interface, mobile apps, and browser extensions. Core Features The application
  supports bookmarking links, taking notes, and storing images and PDFs. It automatically
  fetches link titles, descriptions, and preview images. Content can be organized
  into collaborative lists, and a full-text search engine powered by Meilisearch enables
  finding any stored content. OCR extraction pulls text from images, and RSS feed
  integration enables automatic content hoarding from specified sources. AI-Powered
  Organization Karakeep integrates with OpenAI or local Ollama models to provide automatic
  tagging and summarization of bookmarked content. A rule-based engine allows creating
  custom management rules for automated organization. The AI system analyzes content
  and assigns relevant tags without manual intervention, making it possible to organize
  large collections of saved content efficiently. REST API and Integration The application
  exposes a REST API that agents can use to programmatically create bookmarks, manage
  lists, search content, and retrieve tagged items. Browser extensions are available
  for Chrome and Firefox for quick bookmarking, and native iOS and Android apps provide
  mobile access. The platform supports SSO authentication, bookmark importing from
  Chrome, Pocket, Linkwarden, and Omnivore, and automatic sync with browser bookmarks
  via Floccus. Architecture and Deployment Built with Next.js, Drizzle ORM, tRPC,
  and NextAuth, Karakeep is designed as a self-hosting-first application. It uses
  Puppeteer for crawling bookmarked pages and Meilisearch for full-content search.
  Full page archival using Monolith protects against link rot, and automatic video
  archiving via yt-dlp captures video content. Deployment is straightforward via Docker
  Compose. Agent Use Cases Agents can use Karakeep to build and maintain knowledge
  bases from web research, automatically categorize and tag discovered resources,
  search across previously saved content for relevant information, archive important
  pages before they disappear, and manage curated collections of links and notes for
  research workflows.
verification: security_reviewed
source: https://github.com/karakeep-app/karakeep
category:
- Research &amp; Scraping
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: karakeep-app/karakeep
  github_stars: 24456
---

# Karakeep Self-Hosted Bookmark Manager with AI Tagging

Karakeep, previously known as Hoarder, is a self-hosted bookmark management application designed for data hoarders who want full control over their saved content. With over 24,000 GitHub stars and active development, it provides AI-powered automatic tagging, full-text search, and comprehensive content archiving through a modern web interface, mobile apps, and browser extensions. Core Features The application supports bookmarking links, taking notes, and storing images and PDFs. It automatically fetches link titles, descriptions, and preview images. Content can be organized into collaborative lists, and a full-text search engine powered by Meilisearch enables finding any stored content. OCR extraction pulls text from images, and RSS feed integration enables automatic content hoarding from specified sources. AI-Powered Organization Karakeep integrates with OpenAI or local Ollama models to provide automatic tagging and summarization of bookmarked content. A rule-based engine allows creating custom management rules for automated organization. The AI system analyzes content and assigns relevant tags without manual intervention, making it possible to organize large collections of saved content efficiently. REST API and Integration The application exposes a REST API that agents can use to programmatically create bookmarks, manage lists, search content, and retrieve tagged items. Browser extensions are available for Chrome and Firefox for quick bookmarking, and native iOS and Android apps provide mobile access. The platform supports SSO authentication, bookmark importing from Chrome, Pocket, Linkwarden, and Omnivore, and automatic sync with browser bookmarks via Floccus. Architecture and Deployment Built with Next.js, Drizzle ORM, tRPC, and NextAuth, Karakeep is designed as a self-hosting-first application. It uses Puppeteer for crawling bookmarked pages and Meilisearch for full-content search. Full page archival using Monolith protects against link rot, and automatic video archiving via yt-dlp captures video content. Deployment is straightforward via Docker Compose. Agent Use Cases Agents can use Karakeep to build and maintain knowledge bases from web research, automatically categorize and tag discovered resources, search across previously saved content for relevant information, archive important pages before they disappear, and manage curated collections of links and notes for research workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/karakeep-bookmark-manager-ai-tagging/)
