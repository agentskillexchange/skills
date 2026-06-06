# 🛠️ Infrastructure, SRE & Incident Operations

Production reliability workflows for Kubernetes, incidents, observability, backups, deploy safety, infrastructure drift, alerts, and runbook-driven debugging.

- Live page: https://agentskillexchange.com/industry-skills/#infrastructure-sre-incident-operations
- Homepage access: Curated Collections on https://agentskillexchange.com/

## Who this is for

- SREs, platform engineers, DevOps leads, and infrastructure operators responsible for production reliability.
- Teams that need Kubernetes, observability, backup, deployment, and incident response workflows joined into one operating shelf.

## Jobs covered

- Investigate production incidents across Kubernetes, logs, cloud signals, and observability backends.
- Review and test infrastructure changes before deploys, Helm releases, Terraform diffs, or cluster manifests cause outages.
- Run backup, restore, retention, and alert routing workflows with operator-visible evidence.
- Keep cluster operations, dashboards, and runbooks close enough for on-call use.

## Workflow Stacks

- **Kubernetes incident triage:** Open cluster context → tail affected pod logs → inspect crash signals → correlate observability → capture runbook notes
- **Safe infrastructure change:** Review Terraform or Helm diff → lint automation → run cluster tests → sync GitOps target → watch rollout health
- **Backup and recovery readiness:** Schedule backups → verify retention → test restore path → route failure alerts → record evidence

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [Deploy Kubernetes-native agents with kagent](../skills/deploy-kubernetes-native-agents-with-kagent/) | Adds a Kubernetes-native agent control plane for cluster automation experiments that still need operator boundaries. | Platform engineer / SRE lead | High | 2.9k |
| [Control Kubernetes infrastructure through natural-language MCP workflows](../skills/control-kubernetes-infrastructure-through-natural-language-mcp-workflows/) | Lets operators inspect and act on Kubernetes resources through MCP instead of brittle one-off kubectl prompts. | SRE / platform operator | High | 898 |
| [Run Kubernetes cluster operations through MCP](../skills/run-kubernetes-cluster-operations-through-mcp/) | Covers cluster-level MCP operations for routine checks, triage, and controlled remediation. | Kubernetes operator | High | 1.4k |
| [Operate Kubernetes and OpenShift clusters through MCP](../skills/operate-kubernetes-and-openshift-clusters-through-mcp/) | Extends the cluster-ops workflow to Kubernetes and OpenShift environments where enterprise platform teams need consistent runbooks. | Platform engineer / OpenShift admin | High | 1.6k |
| [Investigate production incidents across Kubernetes and cloud signals with HolmesGPT](../skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt/) | Pulls Kubernetes and cloud signals into an incident investigation loop instead of leaving responders to correlate dashboards manually. | Incident commander / SRE | Medium | 2.3k |
| [Tail multi-pod Kubernetes logs by label during incidents with Stern](../skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/) | Gives responders a fast multi-pod log tailing step during label-scoped outages. | On-call engineer | Low | 4.6k |
| [Kubernetes Pod Crash Diagnostics](../skills/kubernetes-pod-crash-diagnostics-3/) | Turns CrashLoopBackOff and pod failure evidence into a focused diagnosis packet for responders. | Kubernetes support engineer | Medium | 121.7k |
| [K9s Kubernetes Terminal Dashboard](../skills/k9s-kubernetes-terminal-dashboard/) | Provides a fast terminal cockpit for cluster inspection during normal operations and incidents. | SRE / cluster operator | Low | 33.2k |
| [Polaris Kubernetes Best Practices Validator](../skills/polaris-kubernetes-best-practices-validator/) | Checks Kubernetes workload readiness and policy hygiene before manifest mistakes reach production. | Platform reliability reviewer | Low | 3.4k |
| [Lint Ansible playbooks and roles before automation breaks in prod with ansible-lint](../skills/lint-ansible-playbooks-and-roles-before-automation-breaks-in-prod-with-ansible-lint/) | Prevents configuration automation failures by linting playbooks before they run against infrastructure. | DevOps engineer | Low | 3.9k |
| [ArgoCD GitOps Sync Automator](../skills/argocd-gitops-sync-automator/) | Automates GitOps sync checks and actions for teams running ArgoCD-backed production deploys. | Release engineer / platform operator | Medium | 22.5k |
| [Helm Chart Diff & Upgrade Manager](../skills/helm-chart-diff-upgrade-manager/) | Makes Helm upgrades reviewable by surfacing chart diffs before cluster changes land. | Kubernetes release engineer | Medium | 29.7k |
| [Plan and apply many Helm releases from one declarative state before cluster changes drift out of sync with Helmfile](../skills/plan-and-apply-many-helm-releases-from-one-declarative-state-before-cluster-changes-drift-out-of-sync-with-helmfile/) | Coordinates many Helm releases from a single desired state so platform drift is visible before apply. | Platform engineer | High | 5.1k |
| [Run declarative Kubernetes test suites against clusters before operator or manifest changes merge with KUTTL](../skills/run-declarative-kubernetes-test-suites-against-clusters-before-operator-or-manifest-changes-merge-with-kuttl/) | Runs declarative Kubernetes tests before operator or manifest changes become incident fuel. | Platform QA / SRE | Medium | 804 |
| [Terraform Plan Diff Analyzer](../skills/terraform-plan-diff-analyzer/) | Turns Terraform plan output into an infrastructure-review artifact before risky changes merge. | Infrastructure reviewer | Medium | 48.1k |
| [Terraform Drift Detector](../skills/terraform-drift-detector-2/) | Detects drift between declared Terraform state and real infrastructure before incidents or surprise costs appear. | Cloud platform engineer | Medium | 48.1k |
| [Orchestrate database backup, restore, retention, and failure-notification runbooks through Databasement](../skills/orchestrate-database-backup-restore-retention-and-failure-notification-runbooks-through-databasement/) | Covers backup, restore, retention, and failure notification as an auditable runbook rather than an ad hoc database chore. | Database operator / SRE | Medium | 315 |
| [Schedule and retain cross-database backups from one self-hosted control plane with Databasus](../skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus/) | Centralizes scheduled backups and retention across databases for smaller platform teams. | Infrastructure operator | Medium | 6.6k |
| [Restic Fast Encrypted Backup Program](../skills/restic-encrypted-backup-tool/) | Adds encrypted file and repository backup workflows for production recovery planning. | SRE / backup owner | Low | 32.9k |
| [Netdata Real-Time Infrastructure Monitoring and Alerting](../skills/netdata-real-time-infrastructure-monitoring-and-alerting/) | Gives infrastructure teams immediate host and service telemetry for alerting and triage. | SRE / infra operator | Medium | 78.4k |
| [SigNoz Open-Source Observability Platform](../skills/signoz-open-source-observability-platform/) | Provides logs, metrics, and traces for production reliability investigations without a proprietary-only observability stack. | Observability engineer | High | 26.5k |
| [OpenObserve Cloud-Native Observability Platform for Logs Metrics and Traces](../skills/openobserve-observability-platform-logs-metrics-traces/) | Adds a cloud-native observability backend for logs, metrics, traces, and incident search. | Observability platform owner | High | 18.5k |
| [Convert SMTP-only alerts into routed notification deliveries with Mailrise](../skills/convert-smtp-only-alerts-into-routed-notification-deliveries-with-mailrise/) | Routes legacy SMTP-only alerts into modern notification channels so incidents reach the right responders. | On-call tooling owner | Low | 1.5k |
| [Datadog Integration Connector](../skills/datadog-integration-connector-agent/) | Connects Datadog signals into agent workflows for incident context, monitor review, and dashboard triage. | SRE / observability engineer | Medium | 791 |

## Editorial Notes

- This collection crosses Runbooks, Monitoring, CI/CD, Code Quality, Developer Tools, and Integrations because incident work rarely stays inside one category.
- Listed Kubernetes agent picks are included only where they represent a distinct operator workflow not covered by stronger security-reviewed alternatives.
- Avoid autonomous remediation by default; the collection is built around reviewable signals, controlled runbooks, and operator handoff.
- Keep this persona-based for SRE and platform operations; do not turn it into a generic Monitoring or CI/CD category mirror.

## Adjacent Collections

- [Security Operations & GRC Workflows](security-operations-grc-workflows.md)
- [Data Platform & Analytics Engineering](data-platform-analytics-engineering.md)
- [DevRel & API Documentation Workflows](devrel-api-documentation.md)

---

[← Back to industry collections](README.md)
