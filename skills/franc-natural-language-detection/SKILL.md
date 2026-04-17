---
title: "franc Natural Language Detection Library and CLI"
description: "franc is an open-source natural language detection library for JavaScript, available as both an npm package and a CLI tool. It analyzes text input and returns the most likely language as an ISO 639-3 three-letter code. franc supports more languages than any comparable library, with packages available for 82, 187, or all 419 detectable languages depending on the precision needed.\nHow It Works\nfranc uses trigram-based statistical analysis derived from the Universal Declaration of Human Rights (UDHR), the most widely translated copyright-free document. The franc() function returns the single most likely language code, while francAll() returns a ranked array of all candidate languages with confidence scores. You can filter results using only and ignore options to constrain detection to specific language sets.\nPackage Variants\nThree npm packages are available: franc-min (82 languages, speakers of 8M+), franc (187 languages, speakers of 1M+), and franc-all (all 414 detectable languages). The CLI is available as franc-cli. All packages are ESM-only and work in Node.js 14.14+, Deno, and modern browsers.\nAgent Integration\nAI agents can use franc to detect the language of incoming text before routing it to language-specific processing pipelines. The CLI (franc \"text to detect\") returns a language code directly, making it easy to integrate into shell scripts and automation workflows. In Node.js, agents can import franc programmatically to classify multilingual content, filter datasets by language, or validate that generated text matches the target language. The francAll() function provides confidence-ranked results useful for ambiguous text where multiple languages may be present.\nInstallation\nInstall the library: npm install franc. Install the CLI globally: npm install franc-cli --global. The project is licensed under MIT. Documentation and source code are on GitHub."
verification: security_reviewed
source: "https://github.com/wooorm/franc"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wooorm/franc"
  github_stars: 4386
---

# franc Natural Language Detection Library and CLI

franc is an open-source natural language detection library for JavaScript, available as both an npm package and a CLI tool. It analyzes text input and returns the most likely language as an ISO 639-3 three-letter code. franc supports more languages than any comparable library, with packages available for 82, 187, or all 419 detectable languages depending on the precision needed.
How It Works
franc uses trigram-based statistical analysis derived from the Universal Declaration of Human Rights (UDHR), the most widely translated copyright-free document. The franc() function returns the single most likely language code, while francAll() returns a ranked array of all candidate languages with confidence scores. You can filter results using only and ignore options to constrain detection to specific language sets.
Package Variants
Three npm packages are available: franc-min (82 languages, speakers of 8M+), franc (187 languages, speakers of 1M+), and franc-all (all 414 detectable languages). The CLI is available as franc-cli. All packages are ESM-only and work in Node.js 14.14+, Deno, and modern browsers.
Agent Integration
AI agents can use franc to detect the language of incoming text before routing it to language-specific processing pipelines. The CLI (franc "text to detect") returns a language code directly, making it easy to integrate into shell scripts and automation workflows. In Node.js, agents can import franc programmatically to classify multilingual content, filter datasets by language, or validate that generated text matches the target language. The francAll() function provides confidence-ranked results useful for ambiguous text where multiple languages may be present.
Installation
Install the library: npm install franc. Install the CLI globally: npm install franc-cli --global. The project is licensed under MIT. Documentation and source code are on GitHub.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/franc-natural-language-detection
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/franc-natural-language-detection` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/franc-natural-language-detection/)
