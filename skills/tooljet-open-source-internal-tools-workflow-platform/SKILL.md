---
name: ToolJet Open Source Internal Tools and Workflow Platform
description: ToolJet is an open-source platform for internal tools, dashboards, workflows,
  and AI-assisted business apps. It connects visual app building with databases, APIs,
  object storage, and self-hosted deployment patterns that agents can reuse across
  teams.
category: Developer Tools
framework: Multi-Framework
verification: listed
source: "https://github.com/ToolJet/ToolJet"
---
# ToolJet Open Source Internal Tools and Workflow Platform

ToolJet is an open-source platform for internal tools, dashboards, workflows, and AI-assisted business apps. It connects visual app building with databases, APIs, object storage, and self-hosted deployment patterns that agents can reuse across teams.

ToolJet is an open-source platform from the ToolJet team for building internal tools, dashboards, workflows, and business applications with a visual builder. The upstream project combines drag-and-drop UI construction with integrations for databases, APIs, object storage, and SaaS systems, which makes it practical when an agent needs to help a team create operational software instead of public-facing marketing pages. The repository describes support for dozens of components, multiple data sources, and both JavaScript and Python execution inside apps, giving agents room to move from simple CRUD screens to more customized internal workflows.

For agent use, ToolJet is especially relevant when the job is to assemble admin consoles, workflow apps, support dashboards, or database-backed interfaces without committing to a from-scratch frontend build. Its official deployment documentation covers Docker Compose setups with either an in-built or external PostgreSQL database, so an agent can reason about local evaluation, self-hosted pilots, and more durable installations using the same product. The project also exposes an ecosystem around plugins and connectors through the ToolJet CLI, which broadens how agents can extend integrations over time. With a large GitHub footprint, active maintenance, formal releases, and clear setup docs, ToolJet passes the real-source and adoption checks needed for ASE intake and fits well in the developer-tools lane for multi-framework agent work.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tooljet-open-source-internal-tools-workflow-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tooljet-open-source-internal-tools-workflow-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tooljet-open-source-internal-tools-workflow-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tooljet-open-source-internal-tools-workflow-platform -a codex
```

### OpenClaw

```bash
clawhub install tooljet-open-source-internal-tools-workflow-platform
```


## Source

- [GitHub](https://github.com/ToolJet/ToolJet)
