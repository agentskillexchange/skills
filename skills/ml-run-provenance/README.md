# ML Run Provenance

An agent skill by [Antreas Antoniou](https://github.com/AntreasAntoniou). Version 1.0.0; MIT licensed.

## Problem

Run names and dashboards rarely explain why a run exists, which code/config/data produced it, or whether historical metadata was reconstructed later.

## Mechanism

Define birth-time metadata, a project-local pure classifier and idempotent attachment pattern, separate resume attempts from birth facts, and preview scope-limited backfills. Validate local JSON structure with the bundled helper.

## Why useful

Campaign intent and artifact identity become inspectable without pretending that inferred historical facts were captured at execution time. The protocol survives tracker changes because the core contract is provider-neutral.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/ml-run-provenance --skill ml-run-provenance
```

Use a compatible agent's skill installer with `AntreasAntoniou/ml-run-provenance`, or clone this repository into that host's configured skills directory under the folder name `ml-run-provenance`:

```sh
git clone https://github.com/AntreasAntoniou/ml-run-provenance.git <your-skills-directory>/ml-run-provenance
```

Replace the destination placeholder first. The repository root is the single discoverable skill, with [SKILL.md](SKILL.md) as its entry point. Installation location and reload/discovery steps vary by host. Installing the skill grants no extra permissions. The host must support Markdown skills; only packages with helpers require Python.

## Example

> Use $ml-run-provenance to design provenance for this trainer. Identify what is already recorded, propose the missing initialization and resume fields, and validate a local metadata record. Do not start training or change remote tracking records.

### Local validator

Requires Python 3.10+. See [the metadata contract](references/metadata-contract.md) for every required field, unknown-value handling, and strict-mode rules.

```sh
python3 scripts/validate_metadata.py /path/to/record.json
python3 scripts/validate_metadata.py /path/to/record.json --strict
```

Replace the illustrative path with an authorized local record. Exit codes: `0` structurally valid; `1` schema/consistency failure; `2` unreadable or invalid JSON/CLI arguments. Normal mode accepts explicitly declared gaps with warnings. Strict mode rejects missing core facts and dirty-code records without a snapshot identity. Unknown keys allow project extensions; their semantics are not validated. Success is not evidence that metadata is true or persisted in a tracker.

## Trust boundary

The helper only reads local JSON. It does not collect facts, verify hashes/URLs, contact trackers, attach metadata, classify run names, backfill records, or reproduce training. Classifier/adapter/resume integration remains project work; uploads and provider mutations require explicit scope and authorization.

## Validation

From this repository root:

```sh
python3 -m unittest discover -s tests -v
```

Tests use clearly synthetic temporary fixtures, not user data or claimed experimental results. If the official skill-creator validator is installed in your environment, run its `quick_validate.py` against this directory. That checks skill packaging, not the truth of a review or the effectiveness of the workflow.

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [CHANGELOG.md](CHANGELOG.md).
