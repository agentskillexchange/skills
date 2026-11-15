---
name: "Read Google Drive files and edit Sheets through MCP"
slug: "read-google-drive-files-and-edit-sheets-through-mcp"
description: "Connect an MCP-capable assistant to Google Drive search, file reads, and Google Sheets cell updates with mcp-gdrive."
github_stars: 280
verification: "security_reviewed"
source: "https://github.com/isaacphi/mcp-gdrive"
author: "Phil Isaac"
publisher_type: "individual"
category: "Calendar, Email & Productivity"
framework: "MCP"
tool_ecosystem:
  github_repo: "isaacphi/mcp-gdrive"
  github_stars: 280
  npm_package: "@isaacphi/mcp-gdrive"
  npm_weekly_downloads: 16102
---

# Read Google Drive files and edit Sheets through MCP

Connect an MCP-capable assistant to Google Drive search, file reads, and Google Sheets cell updates with mcp-gdrive.

## Prerequisites

Node.js, npm, MCP-compatible client, Google Cloud project, OAuth desktop client credentials, Google Drive API, Google Sheets API, Google Docs API

## Installation

Use the upstream install or setup path that matches your environment:
- Make sure to build the server with either npm run build or npm run watch.

Requirements and caveats from upstream:
- Note your OAuth Client ID and Client Secret. They must be provided as environment variables along with your configuration directory.
- Next you will need to run node ./dist/index.js to trigger the authentication step
- You will be prompted to authenticate with your browser. You must authenticate with an account in the same organization as your Google Cloud project.

Basic usage or getting-started notes:
- [Create a new Google Cloud project](https://console.cloud.google.com/projectcreate)
- [Enable the Google Drive API](https://console.cloud.google.com/workspace-api/products)
- [Configure an OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent) ("internal" is fine for testing)

- Source: https://github.com/isaacphi/mcp-gdrive
- Extracted from upstream docs: https://raw.githubusercontent.com/isaacphi/mcp-gdrive/HEAD/README.md

## Documentation

- https://github.com/isaacphi/mcp-gdrive

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/read-google-drive-files-and-edit-sheets-through-mcp/)
