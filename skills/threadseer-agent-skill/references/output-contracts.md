# Output contracts

Profiles are composable defaults. Use the exact headings below when running the validator; otherwise adapt headings to the user's requested format while preserving the same semantics.

## Shared writing rules

- Lead with the outcome or changed state.
- Distinguish source-derived claims, inference, and recommendation.
- Prefer concise evidence locators over large quotations.
- Use `None evidenced` rather than manufacturing content for an empty category.
- Use `Unassigned`, `Not specified`, or `No deadline stated` for missing fields.
- Keep internal analysis out of a shareable section.
- End with the most useful next action or requested response.

## `full` profile

Use for end-to-end analysis. Include:

1. `## Executive Brief`
2. `## Decisions & Commitments`
3. `## Ranked Action Plan`
4. `## Open Questions & Gaps`
5. `## Risks, Misalignments & Assumptions`
6. `## Insights & Learnings`
7. `## Opportunities`
8. `## Nonlinear Potential` only when supported
9. `## Institutional Memory`
10. `## Shareable Team Report`
11. `## Follow-up Draft`

If the audience does not need both communication artefacts, omit the irrelevant one and note the choice.

## `team` profile

Use for coordination and sharing. Include:

1. `## Executive Brief`
2. `## Decisions & Commitments`
3. `## Ranked Action Plan`
4. `## Open Questions & Gaps` when material
5. `## Shareable Team Report`

The shareable report must stand alone and must not refer to hidden/private sections.

## `insights` profile

Use for rapid sense-making. Include:

1. `## Insights & Learnings`
2. `## Risks, Misalignments & Assumptions`
3. `## Open Questions & Gaps`
4. `## Opportunities`
5. `## Nonlinear Potential` only when supported

Rank insights by consequence, not novelty of phrasing.

## `next` profile

Use for decision support. Include:

1. `## Recommendation`
2. `## Why This`
3. `## Ranked Action Plan`
4. `## Validation Plan`

The recommendation must state its epistemic label, decisive evidence, strongest alternative, and what could change it. The validation plan should prefer the cheapest test that resolves the most consequential uncertainty.

## `memory` profile

Use for a proposed durable record. Include:

1. `## Decision Register`
2. `## Commitment Register`
3. `## Assumptions & Unknowns`
4. `## Durable Context`

Include canonical source pointers and a review trigger where available. Producing this profile does not authorize writing it into an archive or tracker.

## Action-plan table

Use these columns for formal Markdown artefacts:

| Action | Owner | Priority | Feasibility | Impact | Effort | Dependencies | Risks | Next Step | Evidence |
|---|---|---|---|---|---|---|---|---|---|

Allowed ranking vocabulary:

- Priority: `P0`, `P1`, `P2`.
- Feasibility: `Easy`, `Medium`, `Hard`.
- Impact: `Low`, `Medium`, `High`.
- Effort: `S`, `M`, `L`.

Explain rankings when they are not self-evident. Do not mistake `P0` for “interesting”; reserve it for blocking, urgent, safety-critical, or immediately decisive work.

## Decision and commitment records

A compact decision entry should contain:

- epistemic label and status;
- decision or proposal;
- decision-maker or authority if known;
- rationale and tradeoff;
- conditions;
- evidence locator;
- superseded or rejected alternatives when material.

A commitment entry should contain:

- epistemic label;
- owner;
- action;
- deadline or `No deadline stated`;
- dependency or condition;
- evidence locator;
- current status only when evidenced.

## Private/shareable pair

When the material is sensitive, return two explicitly separated artefacts:

1. `## Private Analysis` — complete evidence, uncertainty, tensions, and sensitive constraints.
2. `## Shareable Report` — audience-safe facts, decisions, actions, and requests.

List meaningful omissions generically, for example: `Sensitive personnel reasoning omitted`. Do not leak the omitted detail through the explanation.

## JSON contract

Use JSON when the user requests machine-readable output or downstream automation. The top-level object should follow this shape, omitting irrelevant arrays rather than populating them with invented content:

```json
{
  "meta": {
    "profile": "full|team|insights|next|memory|custom",
    "purpose": "string",
    "audience": "string",
    "source_hash": "sha256 or null",
    "limitations": ["string"]
  },
  "executive_brief": "string",
  "evidence": [
    {
      "id": "E01",
      "type": "fact|proposal|decision|commitment|concern|hypothesis|disagreement|unknown",
      "claim": "string",
      "speaker": "string or Unknown",
      "locator": "string",
      "status": "explicit|strong_inference|tentative_inference|contested|unknown",
      "conditions": ["string"],
      "sensitivity": "private|internal|shareable|unknown"
    }
  ],
  "decisions": [],
  "commitments": [],
  "recommendations": [
    {
      "recommendation": "string",
      "status": "recommendation",
      "rationale": "string",
      "evidence_ids": ["E01"],
      "strongest_alternative": "string",
      "change_conditions": ["string"]
    }
  ],
  "actions": [
    {
      "action": "string",
      "owner": "string or Unassigned",
      "priority": "P0|P1|P2",
      "feasibility": "Easy|Medium|Hard",
      "impact": "Low|Medium|High",
      "effort": "S|M|L",
      "dependencies": ["string"],
      "risks": ["string"],
      "next_step": "string",
      "evidence_ids": ["E01"]
    }
  ],
  "open_questions": [],
  "validation_plan": [],
  "risks": [],
  "insights": [],
  "opportunities": [],
  "nonlinear_potential": [],
  "institutional_memory": [],
  "shareable_report": "string",
  "follow_up_draft": "string"
}
```

Recommendations not stated by participants must use a distinct `status` or `kind` field with value `recommendation`; do not insert them into the evidence ledger as explicit source evidence.
