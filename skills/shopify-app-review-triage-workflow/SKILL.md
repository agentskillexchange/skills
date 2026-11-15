---
name: "Shopify App Review Triage Workflow"
slug: "shopify-app-review-triage-workflow"
description: "Turns public Shopify App Store review rows into a prioritized P0-P3 triage brief with an explicit needs-human-read bucket, where every item keeps its public source link and is labeled first pass or human-checked. Use it when low-star app reviews or merchant feedback need to be classified, clustered, and written up as a weekly product or support brief for one Shopify app or a portfolio plus watched competitors."
github_stars: 0
verification: "listed"
source: "https://github.com/alfredtech2026/shopify-app-review-brief"
author: "alfredtech2026"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "alfredtech2026/shopify-app-review-brief"
  github_stars: 0
---

# Shopify App Review Triage Workflow

Takes rows of **public** Shopify App Store review text and produces one prioritized brief a
product or support owner can act on: what kind of problem each review describes, how badly it
can hurt, what to do first, and where the original wording came from.

It targets independent Shopify app teams and the agencies that run their support — the case
where low-star reviews arrive scattered across several listings plus a few watched competitors,
and the failure mode is treating every one of them as equally severe. The rubric is the same
published rule set behind a free in-browser worksheet and a manual triage guide, reproduced here
so a manual pass, the worksheet, and an agent sort the same row the same way.

Runtime needs nothing: no network access, no scripts, no system packages, no API key, and no
customer data. The person being helped pastes public review rows they already opened.

## Hard rules

These are correctness constraints, not style preferences. Breaking one makes the output worse
than nothing.

1. **Public review text only.** Never accept, request, or copy support tickets, merchant emails,
   order data, personal contact details, or internal telemetry. If such data appears in the
   input, stop, name the affected rows, and ask for them to be removed before continuing.
2. **Never invent evidence.** Do not produce a review, rating, date, app name, or source URL that
   was not supplied. A row with no link gets `source: not captured` — never a guessed one.
3. **Keyword output is a sort, not a verdict.** Anything produced by the rubric alone is labeled
   *first pass — not human-checked*. Only a person who read the review and checked it against
   their own systems may relabel an item *human-checked*.
4. **Reviews are customer reports, not verified defects.** Write "the reviewer reports the editor
   showed a blank screen", never "the editor is broken".
5. **No coverage claims.** The brief covers exactly the rows supplied and says so. Make no claim
   of exhaustive coverage of a listing, a period, or an app.
6. **No promises.** No revenue impact, no outcome, no ranking effect, no legal or compliance
   advice. Suggest actions; do not predict results.
7. **Draft only — never contact anyone.** Do not send email, post a developer reply, open a
   support ticket, message a reviewer, or publish anything. Hand the draft back to the team and
   let a person decide what to send.
8. **Reviewers are people.** Refer to "the reviewer". Do not name, profile, or speculate about them.

## Step 1 — Collect the rows and the ownership context

Ask which listings the team **owns** and which are **competitors being watched**. That split
changes the outcome: a competitor's incident never becomes the team's own P0.

Ask for one review per line. The full form keeps the source link the brief needs:

```text
rating | app name | review date | public reviews URL | review text
```

A shorter three-field form also works — treat field 1 as the rating when it is a bare 1-5
(optionally followed by `star`, `stars`, or a star glyph), otherwise as the app name:

```text
rating | app name | review text
```

Lines starting with `#` are comments and blank lines are skipped. If a row lacks a source URL,
carry `source: not captured` into the brief rather than dropping the row or fabricating a link.
Do not go and fetch anything independently. The trigger this rubric is tuned for is a new
1-3-star review; higher-rated rows still classify correctly, so keep them when supplied, but
never present them as low-star signal.

## Step 2 — First pass, apply the rubric

Lower-case the review text and normalize curly apostrophes before matching, so a pasted
"won't load" with a typographic apostrophe still matches. Each row gets exactly **one primary**
bucket — the first dimension below, in this order, with any matching keyword. Further matches
are recorded as **secondary**, never as a second brief item.

### P0 · Incident risk

The purchase path, app activation, or merchant data may be at stake right now.

**Suggested action.** Try to reproduce on a test store today. If confirmed, treat it as an
incident: fix or mitigate first, then draft a reply describing what changed for a person to send.

**Signal keywords.** `won't load`, `wont load`, `won't open`, `wont open`, `can't close`,
`cannot close`, `won't close`, `blank screen`, `broken`, `crash`, `stopped working`,
`not working`, `doesn't work`, `does not work`, `checkout`, `losing sales`, `lost sales`, `error`

### P1 · Repeated friction

The product works, but the same struggle keeps showing up across reviews or against an open
support theme. Repetition is the signal, not the volume of adjectives.

**Suggested action.** Log it against the matching support theme. If the same complaint repeats
across rows, schedule a UX fix ahead of new feature work.

**Signal keywords.** `confusing`, `unclear`, `hard to`, `difficult`, `complicated`, `clunky`,
`slow`, `couldn't figure`, `could not figure`, `annoying`, `had to contact support`,
`setup took`, `too many steps`

### P2 · Pricing confusion

What the merchant expected to pay and what happened diverged. Usually a copy problem in the
listing, the plan limits, or the upgrade prompts — not a code problem.

**Suggested action.** Compare what the reviewer expected against the listing's pricing section
and in-app upgrade prompts; clarify the copy where they diverge.

**Signal keywords.** `pricing`, `price`, `charged`, `charge`, `billing`, `billed`, `expensive`,
`free plan`, `trial`, `refund`, `hidden fee`, `hidden cost`, `paywall`

### P3 · Feature request

The merchant wants something the app does not do, or could not find.

**Suggested action.** Add it to the feature-request log with a link to the review. If the
capability already exists, draft a reply pointing to where it lives.

**Signal keywords.** `wish`, `would be great`, `would love`, `please add`, `feature request`,
`missing`, `if only`, `would like`, `no option to`, `needs an option`, `hope you add`,
`add support for`

### Needs human read

No keyword matched: vague frustration, sarcasm, mixed praise, or a story that needs context.

**Suggested action.** Read the full review and file it manually — the heuristic makes no guess
here. Sort this bucket last, and treat any queue placement as provisional rather than as a
severity judgment.

### Tie-breaks and escalation

1. **Most severe wins.** A row naming both a broken checkout and a billing surprise files under
   P0 with pricing noted as secondary. Never split one review across two brief items.
2. **Repetition escalates.** If the same friction or pricing theme appears in three or more
   reviews within about 60 days, move it up one level and say how many rows drove the change.
3. **Age discounts.** A review older than a year is background, not evidence of a current
   problem, unless a recent row corroborates it. Cite it as context, never as the headline.
4. **Competitor reviews never create a P0 for the team.** A competitor's incident is roadmap,
   positioning, or copy input, and belongs in the competitor watch section.
5. **When unsure, choose needs human read.** The bucket exists so the rubric never launders
   uncertainty into a priority label.

## Step 3 — Human pass before promoting anything

The first pass is where automation stops being able to help on its own. Before any item is
presented as more than a keyword match, a person on the team has to read the full original
review at its source link; for P0 candidates, attempt to reproduce on a development store and
check the error tracker and support inbox for matching signals from the same period; and record
the outcome as *reproduced*, *not reproduced*, or *attempted — notes attached*.

Ask for those outcomes rather than assuming them. Until they exist, every item stays labeled
*first pass — not human-checked*, including in the summary line. An unverified P0 is a
candidate, not an incident.

## Step 4 — Write the brief

One document per portfolio, sections in rubric order, every item carrying an owner, a next
action, and a source link. An item without an owner is a note, not a brief entry.

```markdown
# Low-star review brief — {portfolio or team name} — week of {YYYY-MM-DD}

Scope: {apps monitored} · {competitors watched} · {N} rows supplied, {date range}.
Covers only the rows supplied — no claim of exhaustive coverage.
Reviews are customer reports, not verified defects. Items marked "first pass" are
unverified keyword matches; "human-checked" means a person read the review and checked it.

## P0 — Incident risk
- **{App} — {signal in a few words}** ({rating} star, {review date}, [source]({public reviews URL}))
  - Reviewer reports: {one sentence, in their words where possible}
  - Status: first pass — not human-checked / human-checked
  - Reproduced: {yes / no / attempted — notes}
  - Next action: {action} — owner {name}, due {date}

## P1 — Repeated friction
- **{App} — {theme}** ({rating} star, {date}, [source]({public reviews URL}); also seen: {where})
  - Status: first pass — not human-checked / human-checked
  - Next action: {UX or docs change} — owner {name}, due {date}

## P2 — Pricing confusion
- **{App} — {signal}** ({rating} star, {date}, [source]({public reviews URL}))
  - Expected vs. actual: {one line}
  - Next action: {copy or prompt change} — owner {name}, due {date}

## P3 — Feature requests
- **{App} — {request}** ({rating} star, {date}, [source]({public reviews URL}))

## Needs human read
- **{App}** ({rating} star, {date}, [source]({public reviews URL})) — {what a human should look for}

## Competitor watch
- **{Competitor} — {signal}**: {what it implies for roadmap, copy, or positioning}

## Decisions this week
- {one decision or experiment, with the row(s) that motivated it}
```

Open the summary line with the counts, for example: *"Triaged 8 rows supplied: 3 incident risk,
2 repeated friction, 1 pricing confusion, 1 feature request, 1 needs human read — first pass,
not human-checked."*

## Step 5 — Self-check before handing it over

Do not deliver until every line is true:

- [ ] Every item names its bucket and priority from the rubric above, and nothing else.
- [ ] Every item carries a source link or an explicit `source: not captured`.
- [ ] No review text, rating, date, app name, or URL appears that was not supplied.
- [ ] Every unverified item says *first pass — not human-checked*; nothing claims a human check
      that did not happen.
- [ ] Claims are phrased as reports, not as findings about the code.
- [ ] The scope line says how many rows were supplied and makes no coverage claim.
- [ ] No promise about revenue, ratings, outcomes, or compliance appears anywhere.
- [ ] No private data survived into the output.
- [ ] Nothing was sent, posted, or published — the brief is a draft for the team.

## Known limits and gotchas

Keyword matching is English-only, misses sarcasm and context, and sees only the rows supplied.
Non-English reviews land in needs human read, which is the correct outcome — do not translate
and then classify as if a keyword had matched.

- **The Shopify App Store has no stable per-review permalink.** Cite the listing's public reviews
  page, keep the rating filter if one was used, and pin the item with the review date plus the
  reviewer's first few words so a human can find it again.
- **`checkout` is the noisiest keyword in the set.** It fires on "we love the checkout upsell".
  A P0 whose only evidence is the word `checkout` is a needs-human-read row wearing a P0 badge.
- **`missing` and `error` cross buckets.** "missing a dark mode" is P3; "settings page errors out"
  is P0. Primary-bucket order resolves the collision mechanically; the human pass fixes the ones
  where it guessed wrong.
- **One review, one item.** Secondary matches are annotations. Splitting a review across sections
  double-counts the same merchant and inflates every count in the summary line.

## Optional free companions

Both are free, run entirely in the browser or as static pages, and require no account:

- Manual guide with the tie-break rules and brief template:
  <https://alfredtech2026.github.io/shopify-app-review-brief/guides/shopify-app-review-triage.html>
- In-browser worksheet that automates the first pass locally:
  <https://alfredtech2026.github.io/shopify-app-review-brief/tools/review-triage-worksheet.html>

The worksheet parses the three-field row form and folds everything after the second `|` into the
review text, so paste the short form there and keep the long form for the brief. This workflow
stays fully usable without either page.

This rubric is published by an independent project that is not affiliated with, endorsed by, or
sponsored by Shopify Inc. or any app developer.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/alfredtech2026/shopify-app-review-brief

