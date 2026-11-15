---
name: "mkcert Zero-Config Local Development TLS Certificate Generator"
slug: "mkcert-local-dev-tls-certificate-generator"
description: "mkcert is a zero-configuration CLI tool by Filippo Valsorda that creates locally-trusted development certificates. It automatically installs a local CA in the system root store and generates TLS certificates for localhost, custom domains, and IP addresses without manual PKI management."
github_stars: 58399
verification: "security_reviewed"
source: "https://github.com/FiloSottile/mkcert"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "FiloSottile/mkcert"
  github_stars: 58399
---

# mkcert Zero-Config Local Development TLS Certificate Generator

mkcert is a zero-configuration CLI tool by Filippo Valsorda that creates locally-trusted development certificates. It automatically installs a local CA in the system root store and generates TLS certificates for localhost, custom domains, and IP addresses without manual PKI management.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install mkcert
- brew install nss # if you use Firefox
- git clone https://github.com/FiloSottile/mkcert && cd mkcert

Requirements and caveats from upstream:
- mkcert is a simple tool for making locally-trusted development certificates. It requires no configuration.
- The local CA is now installed in the Firefox trust store (requires browser restart)! 🦊
- or build from source (requires Go 1.13+)

Basic usage or getting-started notes:
- $ mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1
- "example.com"
- "*.example.com"

- Source: https://github.com/FiloSottile/mkcert
- Extracted from upstream docs: https://raw.githubusercontent.com/FiloSottile/mkcert/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mkcert-local-dev-tls-certificate-generator/)
