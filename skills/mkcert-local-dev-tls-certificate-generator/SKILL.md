---
title: "mkcert Zero-Config Local Development TLS Certificate Generator"
description: "mkcert is a zero-configuration CLI tool by Filippo Valsorda that creates locally-trusted development certificates. It automatically installs a local CA in the system root store and generates TLS certificates for localhost, custom domains, and IP addresses without manual PKI management."
verification: security_reviewed
source: "https://github.com/FiloSottile/mkcert"
category:
  - "Developer Tools"
tool_ecosystem:
  github_repo: "FiloSottile/mkcert"
  github_stars: 58399
---

# mkcert Zero-Config Local Development TLS Certificate Generator

mkcert is a zero-configuration CLI tool by Filippo Valsorda that creates locally-trusted development certificates. It automatically installs a local CA in the system root store and generates TLS certificates for localhost, custom domains, and IP addresses without manual PKI management.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mkcert-local-dev-tls-certificate-generator/)
