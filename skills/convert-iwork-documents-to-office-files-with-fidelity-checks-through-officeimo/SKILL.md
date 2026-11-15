---
name: "Convert iWork documents to Office files with fidelity checks through OfficeIMO"
slug: "convert-iwork-documents-to-office-files-with-fidelity-checks-through-officeimo"
description: "Convert Pages, Numbers, and Keynote files into Office artifacts over MCP, retaining source hashes, strict acceptance results, and fidelity diagnostics."
github_stars: 616
verification: "security_reviewed"
source: "https://github.com/EvotecIT/OfficeIMO"
author: "EvotecIT"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "EvotecIT/OfficeIMO"
  github_stars: 616
---

# Convert iWork documents to Office files with fidelity checks through OfficeIMO

Convert Pages, Numbers, and Keynote files into Office artifacts over MCP, retaining source hashes, strict acceptance results, and fidelity diagnostics.

## Prerequisites

Local MCP client; .NET SDK >=10.0.100 with dotnet dnx; OfficeIMO.Tool 3.5.1 from NuGet; officeimo-document-operator skill; authorized iWork input and output directories

## Installation

Install or set up from the source-backed instructions:

Install .NET SDK 10.0.100 or newer and a local MCP client. Configure the server environment variable OFFICEIMO_MCP_ALLOWED_ROOTS with explicit source and destination directories. In the client STDIO server configuration use command dotnet and args ["dnx", "OfficeIMO.Tool@3.5.1", "mcp", "serve", "--stdio", "--yes"]. Install the OfficeIMO Document Tools plugin through the upstream client-specific instructions to load officeimo-document-operator; configuring MCP alone exposes tools but does not install the skill. Restart the client after environment or plugin changes. Initial launch retrieves the pinned NuGet tool.

- Source: https://github.com/EvotecIT/OfficeIMO

## Documentation

- https://github.com/EvotecIT/OfficeIMO/blob/OfficeIMO-v20261016073836/.agents/plugins/officeimo-document-tools/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-iwork-documents-to-office-files-with-fidelity-checks-through-officeimo/)
