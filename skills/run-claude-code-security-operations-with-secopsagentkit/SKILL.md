---
name: "Run Claude Code security operations with SecOpsAgentKit"
slug: "run-claude-code-security-operations-with-secopsagentkit"
description: "Install SecOpsAgentKit when a Claude Code session needs repeatable security review skills for SAST, DAST, container scanning, secrets checks, policy review, and remediation planning."
github_stars: 157
verification: "security_reviewed"
source: "https://github.com/AgentSecOps/SecOpsAgentKit"
author: "AgentSecOps"
publisher_type: "open_source"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "AgentSecOps/SecOpsAgentKit"
  github_stars: 157
---

# Run Claude Code security operations with SecOpsAgentKit

Use SecOpsAgentKit as a Claude Code security-operations skill pack, not as a generic security product listing. The operator installs the plugin, invokes focused skills for application security or DevSecOps work, and keeps the results inside a reviewable agent workflow before code, container, or infrastructure changes move forward.

## Prerequisites

Claude Code; permission to install Claude Code plugins; repository, API surface, container image, CI/CD change, or infrastructure module to review

## Installation

Install the official SecOpsAgentKit plugin marketplace entry in Claude Code:

```text
/plugin marketplace add https://github.com/AgentSecOps/SecOpsAgentKit.git
```

After installation, choose a focused security skill for the task at hand. The upstream pack includes application security, DevSecOps, secure SDLC, compliance, threat modeling, incident response, and offensive-security skill groups.

Examples of supported review lanes:

- SAST and secure code review
- DAST and API security testing
- Container and dependency scanning
- Secrets detection
- Threat modeling and policy review
- Incident-response evidence gathering

- Source: https://github.com/AgentSecOps/SecOpsAgentKit
- Extracted from upstream docs: https://raw.githubusercontent.com/AgentSecOps/SecOpsAgentKit/HEAD/README.md

## Documentation

- https://github.com/AgentSecOps/SecOpsAgentKit
- https://docs.claude.com/en/docs/claude-code
- https://docs.claude.com/en/docs/claude-code/skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-code-security-operations-with-secopsagentkit/)
