# ML Research Skeptical Audit

An agent skill by [Antreas Antoniou](https://github.com/AntreasAntoniou). Version 1.0.0; MIT licensed.

## Problem

A convincing ML narrative can hide incompatible objectives, leakage, baseline budget differences, or code paths that do not support the claimed result.

## Mechanism

Scope the precise claim, trace a concrete batch through data/model/loss/optimization/evaluation, issue code-cited Solid / Design choice / Questionable verdicts, and propose controlled falsification tests.

## Why useful

The audit separates what the implementation does from whether a scientific conclusion is established. It ranks threats to validity and makes the next check discriminating rather than merely adding more experiments.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/ml-research-skeptical-audit --skill ml-research-skeptical-audit
```

Use a compatible agent's skill installer with `AntreasAntoniou/ml-research-skeptical-audit`, or clone this repository into that host's configured skills directory under the folder name `ml-research-skeptical-audit`:

```sh
git clone https://github.com/AntreasAntoniou/ml-research-skeptical-audit.git <your-skills-directory>/ml-research-skeptical-audit
```

Replace the destination placeholder first. The repository root is the single discoverable skill, with [SKILL.md](SKILL.md) as its entry point. Installation location and reload/discovery steps vary by host. Installing the skill grants no extra permissions. The host must support Markdown skills; only packages with helpers require Python.

## Example

> Use $ml-research-skeptical-audit to review the claim that one training objective outperforms another. Inspect the supplied code and result artifacts, cite the actual evaluation path, and propose the smallest checks that could disprove your conclusions. Do not launch experiments.

The Codex metadata retains explicit invocation for this audit. Other hosts may implement invocation controls differently; the skill's substantive trust boundaries apply regardless.

## Trust boundary

This is an instruction-only review method. It does not run training, reproduce experiments, establish significance, or prove a result. Commands proposed but not run must be labeled. Paid compute, data downloads, tracker writes, and repository modifications need separate authorization.

## Validation

There is no executable runtime in this package. Review its behavior against a scoped hypothetical request: distinguish evidence from inference, preserve authorization boundaries, and state what remains unverified. If the official skill-creator validator is installed in your environment, run its `quick_validate.py` against this directory. That checks skill packaging, not the truth of a review or the effectiveness of the workflow.

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [CHANGELOG.md](CHANGELOG.md).
