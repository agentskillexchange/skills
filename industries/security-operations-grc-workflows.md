# 🛡️ Security Operations & GRC Workflows

Security operations and governance workflows for dependency risk, secrets, CI hardening, agent guardrails, approvals, policy evidence, threat hunting, red-team checks, and audit-ready releases.

- Live page: https://agentskillexchange.com/industry-skills/#security-operations-grc-workflows
- Homepage access: Curated Collections on https://agentskillexchange.com/

## Who this is for

- Security engineers, SOC teams, compliance operators, DevSecOps leads, and AI governance owners.
- Teams that need approval gates, policy evidence, supply-chain checks, agent guardrails, and threat-hunting workflows in one operating map.

## Jobs covered

- Scan dependency, container, CI, and repository surfaces for release-blocking risk.
- Find secrets, unsafe agent configurations, prompt-injection paths, and MCP attack surfaces before adoption.
- Route risky agent or external actions through approval gates with audit evidence.
- Generate SBOM, signature, vulnerability, event-log, and policy artifacts for compliance review.

## Workflow Stacks

- **Release security gate:** Generate SBOM → scan dependencies and images → verify signatures → audit CI permissions → approve or block release
- **Agent governance review:** Preflight prompts and tools → apply runtime guardrails → red-team behavior → route risky actions to approval → store policy evidence
- **SOC investigation packet:** Collect event logs → map Sigma detections → review secrets and repo risk → summarize timeline → handoff remediation

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [Scan project dependencies for supply-chain vulnerabilities with MurphySec](../skills/scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec/) | Scans dependency trees for supply-chain risk before approval or release. | AppSec engineer | Medium | 1.7k |
| [Run Claude Code security operations with SecOpsAgentKit](../skills/run-claude-code-security-operations-with-secopsagentkit/) | Packages Claude Code security workflows for repeatable security operations instead of ad hoc review prompts. | Security engineer | Medium | 157 |
| [Govern agent skills, MCP servers, prompts, and tool calls with DefenseClaw](../skills/govern-agent-skills-mcp-servers-prompts-and-tool-calls-with-defenseclaw/) | Audits agent skills, MCP servers, prompts, and tool calls as governed assets with review boundaries. | AI governance lead | High | 647 |
| [Add runtime guardrails to TypeScript agents with VoltAgent](../skills/add-runtime-guardrails-to-typescript-agents-with-voltagent/) | Adds runtime guardrails around TypeScript agent behavior before unsafe tool calls propagate. | Agent platform engineer | Medium | 8.6k |
| [Pin CI workflow actions and images with Ratchet](../skills/pin-ci-workflow-actions-and-images-with-ratchet/) | Pins workflow actions and images so CI supply-chain inputs stay reviewable and repeatable. | DevSecOps engineer | Low | 928 |
| [Route risky coding-agent work through human approval checkpoints with HumanLayer](../skills/route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer/) | Routes high-risk coding-agent actions through human approval checkpoints before external effects happen. | Security operations lead | Medium | 10.7k |
| [Red-team agent workflows for jailbreaks, prompt injection, and policy failures with DeepTeam](../skills/red-team-agent-workflows-for-jailbreaks-prompt-injection-and-policy-failures-with-deepteam/) | Runs adversarial checks against agent workflows for jailbreaks, prompt injection, and policy failures. | AI red-team operator | Medium | 1.6k |
| [Scan agent repos for repo-poisoning, unsafe AI config files, and MCP attack surfaces with MEDUSA](../skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa/) | Finds repo poisoning and unsafe AI configuration surfaces before agents trust the workspace. | AI security engineer | Medium | 256 |
| [Preflight agent specs for prompt-injection risk across prompt, tool, and architecture layers with Prompt Hardener](../skills/preflight-agent-specs-for-prompt-injection-risk-across-prompt-tool-and-architecture-layers-with-prompt-hardener/) | Checks agent specs for prompt-injection risk across prompts, tools, and architecture before rollout. | AI governance reviewer | Medium | 50 |
| [Turn Windows event logs into Sigma-backed threat-hunting timelines with Hayabusa](../skills/turn-windows-event-logs-into-sigma-backed-threat-hunting-timelines-with-hayabusa/) | Turns Windows event logs into Sigma-backed timelines for SOC triage and investigations. | SOC analyst | Medium | 3.1k |
| [Filter prompts and model outputs for injection, secrets, toxicity, and policy risks with LLM Guard](../skills/filter-prompts-and-model-outputs-for-injection-secrets-toxicity-and-policy-risks-with-llm-guard/) | Screens prompts and model outputs for injection, secrets, toxicity, and policy risks in agent pipelines. | AI safety engineer | Medium | 2.8k |
| [Baseline and Review Repository Secret Findings with detect-secrets](../skills/baseline-and-review-repository-secret-findings-with-detect-secrets/) | Creates a reviewable baseline for repository secret findings instead of burying alerts in noisy scans. | Security reviewer | Low | 4.5k |
| [TruffleHog Credential Leak Scanner](../skills/trufflehog-credential-leak-scanner/) | Scans history and code for leaked credentials that need immediate triage. | SecOps engineer | Low | 25.3k |
| [Audit GitHub Actions for privilege and supply-chain risks with zizmor](../skills/audit-github-actions-for-privilege-and-supply-chain-risks-with-zizmor/) | Audits GitHub Actions workflows for privilege and supply-chain risk before CI becomes an attack path. | DevSecOps engineer | Low | 4.2k |
| [Audit GitHub Actions workflows for insecure permissions and unpinned actions](../skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/) | Reviews workflow permissions and unpinned actions as a pre-merge CI hardening step. | Security reviewer | Low | 4.1k |
| [Catch agent-era CI/CD and permission misconfigurations before shipping with Ship Safe](../skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe/) | Targets agent-era CI/CD and permission misconfigurations that normal lint checks miss. | Platform security engineer | Medium | 521 |
| [Harden-Runner CI/CD Security Agent for GitHub Actions](../skills/harden-runner-cicd-security-agent-github-actions/) | Adds runtime hardening and egress awareness to GitHub Actions jobs. | DevSecOps engineer | Medium | 1.1k |
| [Docker Image Vulnerability Triage](../skills/docker-image-vulnerability-triage/) | Prioritizes container image vulnerabilities for remediation rather than dumping raw scanner output. | Container security analyst | Medium | 71.5k |
| [Trivy Security Scanner for Containers and IaC](../skills/trivy-security-scanner-containers-iac/) | Scans containers and IaC for vulnerabilities and misconfiguration before deploy. | Cloud security engineer | Low | 34.5k |
| [Syft SBOM Generator for Containers and Filesystems](../skills/syft-sbom-generator-containers-filesystems/) | Generates SBOM evidence for containers and filesystems used in release or audit workflows. | Compliance operator | Low | 8.6k |
| [Grype Container and SBOM Vulnerability Scanner](../skills/grype-container-sbom-vulnerability-scanner/) | Maps SBOM and container contents to vulnerabilities for release risk review. | Supply-chain security analyst | Low | 12k |
| [Sigstore Cosign Container Signature Checker](../skills/sigstore-cosign-container-signature-checker/) | Verifies container signatures so release gates can prove artifact origin. | Supply-chain security engineer | Medium | 5.8k |
| [Put approval gates and audit-ready policy checks between agents and external actions with DashClaw](../skills/put-approval-gates-and-audit-ready-policy-checks-between-agents-and-external-actions-with-dashclaw/) | Adds approval gates and policy evidence before agents take external actions. | AI governance operator | Medium | 241 |
| [Verify agent policy coverage and risky-action guardrails before production rollout with Agent Governance Toolkit](../skills/verify-agent-policy-coverage-and-risky-action-guardrails-before-production-rollout-with-agent-governance-toolkit/) | Checks policy coverage and risky-action guardrails before production agent rollout. | AI governance lead | Medium | 1.1k |
| [Stress-test agent defenses with AgentDojo](../skills/stress-test-agent-defenses-with-agentdojo/) | Benchmarks prompt-injection attacks and defenses before agents are trusted with real tools or data. | AI security engineer / red-team operator | Medium | 619 |
| [Run agent-generated code in local microVM sandboxes with Microsandbox](../skills/run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox/) | Runs untrusted agent-generated code and tool calls in local microVM-backed sandboxes for safer review. | AppSec engineer / agent platform operator | High | 6.5k |
| [Evaluate model-generated code execution with SandboxFusion](../skills/evaluate-model-generated-code-execution-with-sandboxfusion/) | Tests model-generated code execution behavior inside a controlled benchmark before teams trust automation outputs. | AI security engineer / evaluation lead | High | 1k |
| [Gate agent inputs and outputs with Superagent safety checks](../skills/gate-agent-inputs-and-outputs-with-superagent-safety-checks/) | Adds a safety gate for agent inputs and outputs before risky actions reach users or downstream systems. | GRC automation owner / AI safety reviewer | Medium | 6.6k |
| [Emit policy receipts for hard-rule agent skills with Pluribus](../skills/emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus/) | Creates reviewable policy receipts for hard-rule workflows where compliance needs evidence, not just logs. | Compliance engineer / policy operations | Medium | — |
| [Record system-level agent activity with AgentSight](../skills/record-system-level-agent-activity-with-agentsight/) | Captures process, file, network, prompt, and report activity from agent runs so SecOps and GRC teams can audit what an agent actually did. | AI security engineer / GRC audit operator | High | 469 |
| [Scan agent dependencies and container inputs with OWASP dep-scan](../skills/scan-agent-dependencies-and-container-inputs-with-owasp-dep-scan/) | Scans dependencies, containers, SBOMs, licenses, and risk signals before agent-generated or agent-adopted code moves toward production. | AppSec engineer / supply-chain risk reviewer | Medium | 1.3k |

## Editorial Notes

- This collection intentionally blends Security, CI/CD, Templates, and Runbooks because security operations span release gates, agent policy, and incident evidence.
- Only one listed SOC seed is included because Hayabusa fills a distinct Windows event-log hunting job; stronger security-reviewed picks dominate the rest.
- Do not frame these as autonomous security fixes; the value is evidence, gates, review, and controlled remediation.
- Keep this workflow/persona based for SecOps, AppSec, SOC, and AI governance; do not make it a renamed Security & Verification category page.

## Adjacent Collections

- [Infrastructure, SRE & Incident Operations](infrastructure-sre-incident-operations.md)
- [Legal Ops & Compliance](legal-ops-compliance.md)
- [AI Agency Operations & FDE Workflows](ai-agency-operations.md)

---

[← Back to industry collections](README.md)
