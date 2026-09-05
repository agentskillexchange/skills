---
name: "GCP Keyless"
slug: "gcp-keyless"
description: "Operate Google Cloud without recurring browser OAuth or service-account key files. Use when an agent needs GCP access, local gcloud credentials expire, a project needs GitHub OIDC Workload Identity Federation, or cloud workloads should use attached managed service accounts."
category: "Security & Verification"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/gcp-keyless"
---

# GCP Keyless

Remove human Google OAuth from the steady-state agent path. Prefer short-lived,
auditable identity: attached metadata identity inside GCP, or a typed GitHub Actions
workflow authenticated through Workload Identity Federation (WIF).

## Start with diagnosis

Run:

```bash
python3 scripts/doctor.py --repo OWNER/REPO --workflow gcp-keyless-observe.yml
```

Read its JSON and follow exactly one route:

- `managed-metadata`: run directly with the attached service account. Verify the
  reported email is the intended identity before accessing the project.
- `github-dispatch`: dispatch a reviewed, typed workflow. Local Google credentials are
  neither needed nor consulted.
- `human-oauth-fallback`: credentials currently work, but they are not the durable
  solution. Use them only for the one-time WIF bootstrap or an explicitly approved
  emergency.
- `bootstrap-required`: stop and follow [references/bootstrap.md](references/bootstrap.md).

## Non-negotiable controls

1. Never create, download, accept, or recommend a service-account JSON key.
2. Never print access tokens, OIDC tokens, authorization headers, or credential JSON.
   The official auth action may create an ephemeral WIF external-account file on its
   short-lived runner for `gcloud`; it is not a private key and must never be archived.
3. Never treat a working GitHub login as proof of GCP authority. It only authorizes
   dispatch; the WIF provider and service-account binding authorize GCP.
4. Never expose arbitrary `command`, `script`, or `shell` workflow inputs. Operations
   must be an explicit choice list mapped to reviewed commands.
5. Pin every third-party GitHub Action to a full commit SHA.
6. Restrict the WIF provider with immutable numeric `repository_id` and
   `repository_owner_id` claims plus a protected GitHub environment.
7. Use distinct least-privilege observer and launcher service accounts. Do not let a
   read-only workflow impersonate the launcher.
8. Before paid, mutating, or GPU work, use the project's configured budget and
   approval authority. Preserve durable identity or authority changes in its canonical
   audit record.
9. A workflow dispatch is an external action. Dispatch only when the user authorized
   that exact operation and scope.

## Install the observer workflow

Copy [assets/gcp-keyless-observe.yml](assets/gcp-keyless-observe.yml) to
`.github/workflows/gcp-keyless-observe.yml`. Configure the repository/environment
variables named in the template, then validate it:

```bash
python3 scripts/validate_workflow.py .github/workflows/gcp-keyless-observe.yml
```

The supplied workflow is intentionally read-only. Create mutation workflows separately,
with a narrow typed operation set, protected environment approval, budget receipt, and
project-specific launch grant. Do not turn the observer workflow into a generic executor.

## Dispatch without Google OAuth

```bash
gh workflow run gcp-keyless-observe.yml \
  --repo OWNER/REPO \
  --ref BRANCH \
  -f operation=instances
```

Follow the run with `gh run watch` and download its normal logs or explicit receipts.
Do not echo credentials for debugging. A denied WIF exchange is an identity-policy
failure, not a reason to create a key.

## Inside GCP

Use the VM, Cloud Run, or GKE workload's attached service account through the metadata
server or Application Default Credentials. Do not run `gcloud auth login` on workers.
Refuse startup if the observed service-account email differs from the expected identity.

## One-time boundary

WIF cannot bootstrap itself. A project administrator must perform one authenticated,
audited setup to create the pool/provider, service accounts, attribute condition, IAM
bindings, and GitHub variables. After the verification in
[references/bootstrap.md](references/bootstrap.md), recurring local Google OAuth is no
longer part of ordinary agent operation.

## Installation and upstream provenance

The upstream skill identifier is `gcp-keyless`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/gcp-keyless --skill gcp-keyless --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/gcp-keyless#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`d46213c3e5ef`](https://github.com/AntreasAntoniou/gcp-keyless/tree/d46213c3e5ef84f82c869033fb7719cb1398c4bb). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
