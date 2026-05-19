---
name: "Scan sites for accessibility gaps, file GitHub issues, and route fixes through Copilot with Accessibility Scanner"
slug: "scan-sites-for-accessibility-gaps-file-github-issues-and-route-fixes-through-copilot-with-accessibility-scanner"
description: "Run accessibility scans against target URLs, open trackable issues, and optionally hand remediation suggestions to Copilot instead of treating accessibility review as a manual audit chore."
github_stars: 266
verification: "security_reviewed"
source: "https://github.com/github/accessibility-scanner"
author: "GitHub"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "github/accessibility-scanner"
  github_stars: 266
---

# Scan sites for accessibility gaps, file GitHub issues, and route fixes through Copilot with Accessibility Scanner

Run accessibility scans against target URLs, open trackable issues, and optionally hand remediation suggestions to Copilot instead of treating accessibility review as a manual audit chore.

## Prerequisites

GitHub repository with Actions and Issues enabled, repository secret for a fine-grained PAT, list of target URLs, optional GitHub Copilot access for automated fix assignment

## Installation

Requirements and caveats from upstream:
- The a11y scanner requires a Personal Access Token (PAT) as a repository secret:
- | login_url | No | If scanned pages require authentication, the URL of the login page | https://github.com/login |
- | username | No | If scanned pages require authentication, the username to use for login | some-user |

Basic usage or getting-started notes:
- | Input | Required | Description | Example |
- | base_url | No | GitHub API base URL used by Octokit. Set this for GitHub Enterprise Server (format: https://HOSTNAME/api/v3). Defaults to https://api.github.com | https://ghe.example.com/api/v3 |

- Source: https://github.com/github/accessibility-scanner
- Extracted from upstream docs: https://raw.githubusercontent.com/github/accessibility-scanner/HEAD/README.md

## Documentation

- https://github.com/github/accessibility-scanner

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-sites-for-accessibility-gaps-file-github-issues-and-route-fixes-through-copilot-with-accessibility-scanner/)
