---
name: "ML Research Skeptical Audit"
slug: "ml-research-skeptical-audit"
description: "Adversarial, code-cited audit of ML research claims, objectives, leakage, controls, and baseline fairness with ranked risks and explicit falsification tests. Use when asked to challenge a result or assess whether an experimental comparison is trustworthy."
category: "Code Quality & Review"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/ml-research-skeptical-audit"
---

# ML Research Skeptical Audit

Structure a scientific argument grounded in the actual implementation. This is a review method, not an experiment runner: reviewing code does not reproduce a figure, execute training, establish statistical significance, or prove a scientific claim.

## Ground rules

1. **Code or it is unverified.** Cite every structural repository claim to a file, symbol, and line range at the inspected revision. Quote short decisive snippets when useful. If the implementation is unavailable, label the claim unverified; do not invent APIs or infer code behavior from names alone.
2. **Separate units and objectives.** Latent-space MSE, token cross-entropy, and contrastive losses cannot be ranked numerically against each other. Require a shared downstream task/metric with matched data and evaluation protocol before claiming superiority.
3. **Use three verdicts.** Solid: implementation matches the stated intent. Design choice: defensible but sensitive to a named lever such as masking, balancing, tie-breaking, or initialization. Questionable: possibly incorrect, unfair, or misleading, paired with a discriminating counterexample or falsification. “Solid” is not a claim that the method works empirically.
4. Rank validity risks before presentation concerns: leakage and evaluation contamination; incompatible units and unfair controls; train/eval disparity; optimization and regularization; then cosmetic issues. Explain severity and evidence rather than forcing every issue into this order.
5. End with what would prove the audit wrong. Prefer a runnable check grounded in existing scripts; label proposed scripts and unexecuted commands as such.

## Scope and trace

State the exact claim, scope (data/model/loss/training/evaluation/fairness), inspected revision, worktree caveat, and available evidence. Read repository instructions and experiment documentation. Locate the config and entry point for the specific result, not merely the current defaults. Separate executed evidence from logs provided by others and from static inference.

Trace one concrete forward pass: batch dimensions → transformations → model predictions → loss terms and reductions → optimized parameters. Mark unknown dimensions rather than inventing them. Then inspect:

1. **Data contract:** dataset/collate schema, split construction, sampling, augmentation, preprocessing fits, duplicate/entity/time overlap, label-derived features, retrieval contamination, and whether validation/test data affect training or checkpoint choice.
2. **Model:** forward signature, predicted versus reconstructed targets, target visibility, capacity, conditioning, masking, and possible shortcut solutions. For generative or representation-prediction methods, consider intrinsic data complexity versus model capacity without asserting an unmeasured dimension.
3. **Objective:** weights, units, normalization/reduction, masking, modality/task balancing, collapse prevention, stop-gradient, and targets. Check that the implemented optimization matches the claim.
4. **Optimization:** optimizer/schedules, initialization, EMA timing, gradient accumulation, mixed precision, update ordering, effective batch and token budgets, and failed/diverged runs.
5. **Evaluation:** exact checkpoint selection, held-out protocol, metric units/direction/aggregation, shared task, preprocessing, inference budget, paired seeds/examples, uncertainty and multiple comparisons. Inspect the code path producing the figure, not just training metrics.
6. **Reproducibility:** entry point, resolved config, code/data versions, seed handling, hardware/precision, output lineage, and unavailable artifacts. A seed alone is not reproducibility.

## Controls and falsification

Choose tests that distinguish the disputed explanation from alternatives. Do not demand expensive experiments merely to fill a checklist; first use static checks and small counterexamples when sufficient.

| Claim | Discriminating check |
|---|---|
| A beats B on training loss | Identify units; if incompatible, compare on a shared held-out downstream metric, fixed selection rule, and evaluation budget. |
| Fair comparison | Match or explicitly account for data, steps/tokens, parameters, tuning effort, and measured compute; include extra encoders, targets, projectors, and inference cost. State which budget is controlled rather than claiming all are equivalent. |
| Scaling law | Vary size with controlled data/compute and regularizer conventions; check optimization failures, uncertainty, and extrapolation limits. |
| Multitask mechanism helps | Ablate terms or task dropout, include simpler baselines, and use paired seeds with uncertainty. |
| No leakage | Trace split/preprocessing/checkpoint-selection code; check overlap at the meaningful entity/time unit and test-set reuse. |
| Representation is meaningful | Compare shortcut/collapse or shuffled-label controls, fixed probes, and transfer under a declared evaluation protocol. |

For each proposed falsification specify hypothesis, intervention, held-fixed variables, metric, decision criterion, expected discriminating outcome, and estimated resource/permission needs. Do not run training, download restricted data, launch paid compute, or mutate experiment tracking unless separately authorized. Avoid post-hoc threshold invention: state when a criterion is provisional.

## Deliverable

Give the question and evidence limits; one concrete forward/loss trace with citations; Solid / Design choice / Questionable findings; ranked risks with claim impact; and a short falsification list. Cite both supporting and conflicting evidence. Distinguish “reviewed,” “executed,” “reproduced,” and “not checked.” A missing control is a limitation, not proof of misconduct or a failed method.

## Installation and upstream provenance

The upstream skill identifier is `ml-research-skeptical-audit`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/ml-research-skeptical-audit --skill ml-research-skeptical-audit --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/ml-research-skeptical-audit#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`0ea8fa98d155`](https://github.com/AntreasAntoniou/ml-research-skeptical-audit/tree/0ea8fa98d1558852f4f2653bfe03a92526be7d6b). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
