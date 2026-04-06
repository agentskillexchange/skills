---
name: "Conftest Structured Configuration Policy Testing with OPA Rego"
description: "Conftest is a CLI tool that tests structured configuration data using the Open Policy Agent Rego language. It validates Kubernetes manifests, Terraform configs, Dockerfiles, CI pipelines, and any other structured format against custom policy rules."
category: "Security & Verification"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/open-policy-agent/conftest"
tool_ecosystem:
  github_repo: "open-policy-agent/conftest"
  github_stars: 3150
---
# Conftest Structured Configuration Policy Testing with OPA Rego

Conftest is a CLI tool that tests structured configuration data using the Open Policy Agent Rego language. It validates Kubernetes manifests, Terraform configs, Dockerfiles, CI pipelines, and any other structured format against custom policy rules.

Conftest is an open-source CLI utility from the Open Policy Agent project that lets you write and run tests against structured configuration data using the Rego query language. With over 3,000 GitHub stars and active development, it has become a standard tool for policy-as-code workflows across Kubernetes, Terraform, CI/CD, and general infrastructure configuration.



How Conftest Works

You write policy rules in Rego (the Open Policy Agent policy language) and store them in a policy/ directory. Each rule defines a deny or warn condition with a human-readable message. Running conftest test your-config.yaml evaluates all policies against the input and reports pass/fail results with clear failure messages. Conftest parses multiple formats natively: YAML, JSON, INI, TOML, HCL, CUE, Dockerfile, and more.



Use Cases

The most common use case is validating Kubernetes manifests: ensuring containers run as non-root, enforcing resource limits, requiring specific labels, or blocking privileged pods. For Terraform, Conftest can validate that security groups restrict access, encryption is enabled, or naming conventions are followed. It works equally well with Dockerfiles (checking base image policies), CI pipeline definitions (enforcing approval gates), and Serverless configurations.



Policy Sharing and Bundles

Conftest supports pulling policies from OCI registries, enabling teams to publish and share policy bundles. You can push policies with conftest push and pull them with conftest pull, making it straightforward to distribute organization-wide compliance rules. Policies can also be tested themselves using conftest verify to ensure rules behave as expected.



CI/CD Integration

Conftest produces structured output (JSON, TAP, table, JUnit) suitable for CI pipeline integration. It returns non-zero exit codes on policy violations, making it a natural fit for pre-merge checks. Teams commonly run Conftest in GitHub Actions, GitLab CI, or Jenkins pipelines to gate deployments on policy compliance.



Agent Integration

AI agents can integrate Conftest into infrastructure workflows: validate generated Kubernetes manifests before applying them, check Terraform plans against security policies, or audit existing configurations for compliance drift. The structured JSON output is easy to parse programmatically, and the Rego policy language lets agents express complex validation logic in a declarative format.



Installation

Install via Homebrew (brew install conftest), Scoop on Windows, or download binaries from the GitHub Releases page. It is also available as a Docker image and can be installed via go install github.com/open-policy-agent/conftest@latest.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill conftest-opa-config-policy-testing
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill conftest-opa-config-policy-testing -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill conftest-opa-config-policy-testing -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill conftest-opa-config-policy-testing -a codex
```

### OpenClaw

```bash
clawhub install conftest-opa-config-policy-testing
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/conftest-opa-config-policy-testing/)
