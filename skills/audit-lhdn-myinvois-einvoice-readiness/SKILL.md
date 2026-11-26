---
name: "Audit LHDN MyInvois e-invoice readiness and build UBL 2.1 drafts"
slug: "audit-lhdn-myinvois-einvoice-readiness"
description: "Audit a Malaysian invoice ledger for LHDN MyInvois e-invoice readiness and build UBL 2.1 draft payloads. Covers TIN shape validation, per-item MSIC classification, SST tax category codes, the seven readiness gates, and the UBL field mapping MyInvois rejects."

category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/nusabyte-my/agent-skills"
author: "nusabyte-my"
publisher_type: "individual"
---

# Audit LHDN MyInvois e-invoice readiness and build UBL 2.1 drafts

Malaysia mandates business-to-business e-invoicing through LHDN's MyInvois portal on a
phased schedule. An organisation with an existing invoice ledger needs two things before
its first submission: a per-document audit of what is missing, and a correct UBL 2.1
payload for the documents that are ready. This skill covers both, and the failure mode
that makes the first one dangerous.

## What it does

Runs seven readiness gates over every non-void document and reports per-document, not as
one aggregate pass/fail. The gates are: seller TIN present, buyer TIN present, per-item
MSIC classification, filing currency, zero or negative totals, totals arithmetic, and
duplicate issue detection on supplier TIN plus invoice number.

The output that matters is which specific document is blocked and which specific field is
empty. "3 of 12 documents blocked: 2 missing buyer TIN, 1 missing MSIC on line 4" is the
deliverable. "Not ready" is not.

## Why the per-item MSIC column matters

Each gate is annotated with whether an agent can legitimately fix it. MSIC codes are
classifications of a described service, so they can be inferred from the line description.
Tax identification numbers cannot be inferred at all — they are registrations held by a
counterparty. A red gate that names the missing input is the correct output; inventing a
TIN to make the check green produces a filing that LHDN rejects weeks later, plus an audit
trail that says the number was fabricated.

## UBL 2.1 mapping

The fields that actually cause rejection: `InvoicedQuantity` needs its `unitCode`
(UN/ECE Recommendation 20 — `C62` each, `HUR` hour, `MON` month), a bare number fails.
`ItemClassificationCode` carries the five-digit MSIC with `listID="CLASS"`. Both parties
need a `PartyTaxScheme` with `CompanyID` set to the TIN and a `PostalAddress` with
`CountryID = MY`. `LegalMonetaryTotal` needs all four of `LineExtensionAmount`,
`TaxExclusiveAmount`, `TaxInclusiveAmount` and `PayableAmount`, even when they are equal.
`InvoiceTypeCode` is `01` invoice, `02` credit note, `03` debit note, `04` refund note.

The document signature is a `UBLExtensions` block and must be built last, because signing
freezes the payload — any amount change afterwards invalidates it.

## Draft-only by design

Nothing in this skill submits to LHDN, emails a counterparty, marks a document sent, or
deletes a record. Every gate exits non-zero when blocked, so a scheduler can branch on the
exit code. A fetched ledger snapshot is gitignored because it contains counterparty PII.

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/nusabyte-my/agent-skills.git
cp -R agent-skills/skills/myinvois-einvoice-readiness ~/.agent-skills/myinvois-einvoice-readiness
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add nusabyte-my/agent-skills --skill myinvois-einvoice-readiness
```

## Caveats

Rollout thresholds have been amended repeatedly, and at one point the RM1M turnover band
was cancelled. Treat the gate as a signal about data quality, never as a deadline asserted
to the user, and never let e-invoice readiness block accounts-receivable work, which has no
TIN dependency. There is no offline TIN registry — validate the format
(letter prefix, digits, branch code), never the registration.
