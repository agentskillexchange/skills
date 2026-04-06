---
name: Wiki.js Modern Open Source Wiki Platform on Node.js
description: Wiki.js is a powerful open-source wiki app built on Node.js with support
  for Markdown, visual editing, Git-backed storage, and a GraphQL API. It provides
  multi-language content, granular access controls, and integrations with major authentication
  providers.
category: "Calendar, Email &amp; Productivity"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/requarks/wiki"
---
# Wiki.js Modern Open Source Wiki Platform on Node.js

Wiki.js is a powerful open-source wiki app built on Node.js with support for Markdown, visual editing, Git-backed storage, and a GraphQL API. It provides multi-language content, granular access controls, and integrations with major authentication providers.

Wiki.js is a modern, open-source wiki application built on Node.js that provides a fast and extensible platform for team documentation and knowledge management. With over 28,000 GitHub stars and an active development community, Wiki.js has established itself as one of the most popular self-hosted wiki solutions available, offering a clean interface, powerful features, and flexible deployment options.

The platform supports multiple content editors including a full Markdown editor with live preview, a WYSIWYG visual editor, and raw HTML editing. Content is stored in a database (PostgreSQL, MySQL, MariaDB, MS SQL Server, or SQLite) with optional Git-based storage synchronization, allowing teams to version control their documentation alongside their code repositories.

For agent and automation integration, Wiki.js exposes a GraphQL API that covers page creation and updates, asset management, user and group administration, navigation configuration, and system settings. The GraphQL API supports both query and mutation operations with Bearer token authentication, making it well-suited for programmatic content management by AI agents and automated pipelines.

Wiki.js includes a modular architecture with support for multiple storage backends including local filesystem, Git repositories, AWS S3, Azure Blob Storage, Google Cloud Storage, and SFTP. The search engine is configurable with built-in database search, Elasticsearch, Algolia, Azure Search, and PostgreSQL full-text search options, allowing teams to optimize for their specific scale and performance requirements.

Authentication in Wiki.js is highly flexible, supporting local accounts, LDAP, SAML, OAuth2, OpenID Connect, and pre-configured modules for Auth0, Azure AD, Discord, Dropbox, Facebook, GitHub, Google, Keycloak, Okta, Slack, and Twitch. Granular page-level permissions can be configured through a rules-based access control system tied to user groups.

The platform supports multi-language content with built-in localization for the interface, asset management for images and files, page tags and metadata, comments, custom navigation menus, and theming. Deployment is available via Docker, Kubernetes Helm charts, or native installation on Linux, macOS, and Windows with Node.js 18+.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wikijs-wiki-platform-nodejs
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wikijs-wiki-platform-nodejs -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wikijs-wiki-platform-nodejs -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wikijs-wiki-platform-nodejs -a codex
```

### OpenClaw

```bash
clawhub install wikijs-wiki-platform-nodejs
```


## Source

- [GitHub](https://github.com/requarks/wiki)
