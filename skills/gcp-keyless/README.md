# GCP Keyless

GCP Keyless gives an AI agent a repeatable route to Google Cloud without making
browser login or a downloaded service-account key part of everyday operation.
Inside GCP, use the workload's attached service account. From a local machine,
dispatch a reviewed GitHub Actions workflow that obtains short-lived credentials
through Workload Identity Federation (WIF).

This is useful when an agent repeatedly needs to inspect instances, disks, or
regional quotas, but local `gcloud` credentials keep expiring. The durable setup
is an identity policy and a small set of approved operations, not a reusable
private key passed between agent sessions.

## What this repository provides

[SKILL.md](SKILL.md) teaches the agent how to choose and verify an access route.
The accompanying Python tools diagnose available routes and check the supplied
workflow template. The template exposes exactly three read-only operations:
`instances`, `disks`, and `regional-quotas`.

This is not a hosted proxy, credential broker, or automatic IAM installer.
Installing the skill does not grant cloud access.

## Get started

```bash
npx skills add AntreasAntoniou/gcp-keyless
```

Run the bundled commands from the installed skill directory or a repository
checkout:

```bash
python3 scripts/doctor.py --repo OWNER/REPO
python3 scripts/validate_workflow.py assets/gcp-keyless-observe.yml
```

The diagnostic recommends attached metadata identity, GitHub dispatch, a
temporary human-OAuth fallback, or administrator bootstrap. A reachable GitHub
workflow is not proof that WIF or its GCP permissions work: verify an authorized
read-only run and its cloud audit-log principal.

For GitHub dispatch, an administrator must first follow the
[one-time bootstrap checklist](references/bootstrap.md), configure the protected
environment and repository variables, and copy
[the observer template](assets/gcp-keyless-observe.yml) to
`.github/workflows/gcp-keyless-observe.yml`. The complete dispatch and verification
procedure is in [the skill](SKILL.md).

## Trust and authority

GitHub authentication permits dispatch; the WIF provider's identity conditions
and IAM bindings determine GCP authority. Bind to immutable numeric repository
and owner IDs, verify the expected service-account identity, and keep observer
and launcher accounts separate and least-privileged.

The observer accepts typed operations, not arbitrary shell input, and pins its
third-party actions to commit SHAs. Never create a service-account JSON key or
print tokens. The auth action's temporary external-account credentials file is
not a private key, but it is still sensitive and must not be archived.

Dispatch requires authorization for that operation and scope. Paid or mutating
work needs a separately reviewed workflow, appropriate approval and budget
authority; it is not supplied here. The validator checks workflow text, not live
IAM policy or the full security of a deployment.

## Test

```bash
python3 -m unittest discover -s tests
python3 scripts/validate_workflow.py assets/gcp-keyless-observe.yml
```

With pytest available, also run
`python3 -m pytest scripts/test_gcp_keyless.py` for the four workflow regression
checks. Executing that file directly only defines its tests; it does not run them.

Released under the [MIT License](LICENSE).
