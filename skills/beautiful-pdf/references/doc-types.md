# Document Type Guide

Type-specific structure and styling guidance for professional PDFs.

## Grant Proposals

**Tone:** Confident, precise, evidence-based. No fluff.
**Layout:** Single column, generous margins, clear section headers.
**Must-haves:**
- Title + PI name + institution on first page
- Clear question numbering matching the funder's form
- Tight word/character counts — measure and enforce
- References formatted consistently
- Team table if required
- Budget table if required

**CSS tweaks:**
```css
body { font-size: 11pt; line-height: 1.45; }  /* slightly larger for readability */
h2 { color: #1d4ed8; }  /* blue section headers for navigation */
.question-header { font-weight: 700; font-size: 12pt; margin-top: 2em; color: #0f172a; }
.word-count { font-size: 8pt; color: #888; text-align: right; }
```

## Business Reports / Briefs

**Tone:** Executive, scannable, data-driven.
**Layout:** Consider two-column for dense reports. Single for briefs.
**Must-haves:**
- Executive summary (first page, standalone)
- Key metrics / KPIs in visual boxes
- Charts as images (pre-rendered)
- Clear recommendations section
- Date + author + version

## Letters / Cover Letters

**Tone:** Personal, professional, direct.
**Layout:** Single column, wide margins, lots of whitespace.
**Must-haves:**
- Sender details top-right or in header
- Date
- Recipient address block
- Salutation + body + sign-off
- Signature (image or typed)

**CSS tweaks:**
```css
@page { margin: 30mm 25mm; }  /* extra margins for letters */
body { font-size: 11pt; max-width: 600px; margin: 0 auto; }
.signature { margin-top: 3em; }
```

## Invoices

**Tone:** Clean, unambiguous, professional.
**Layout:** Structured header + line items table + totals.
**Must-haves:**
- Company logo + details
- Invoice number + date + due date
- Bill-to details
- Line items table (description, qty, rate, amount)
- Subtotal, tax, total prominently displayed
- Payment terms / bank details

## CVs / Résumés

**Tone:** Clean, achievement-focused.
**Layout:** Two-column (sidebar + main) or single column.
**Must-haves:**
- Name + contact prominently
- Professional summary (2-3 lines)
- Experience with quantified achievements
- Education
- Skills (if relevant)
- No photos unless culturally expected

**CSS tweaks:**
```css
@page { margin: 15mm; }  /* tighter margins, maximize space */
body { font-size: 9.5pt; line-height: 1.35; }  /* compact */
h1 { font-size: 20pt; margin-bottom: 2px; }
.section-title { font-size: 11pt; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1.5px solid #333; }
```

## One-Pagers / Briefs

**Tone:** High-impact, scannable, visual.
**Layout:** Dense but not cluttered. Use boxes, icons, colour.
**Must-haves:**
- Title that grabs attention
- The "so what" in the first 3 lines
- 3-5 key points max
- Metrics or proof points
- Clear CTA or next step

**CSS tweaks:**
```css
@page { margin: 15mm; }
body { font-size: 10pt; }
.hero { font-size: 26pt; font-weight: 800; margin-bottom: 8px; }
.key-point { display: flex; gap: 12px; margin: 10px 0; padding: 10px; background: #f9fafb; border-radius: 6px; }
```

## Slide-Style Decks (Landscape PDF)

**Tone:** Visual, minimal text, high-impact.
**Layout:** Landscape, one "slide" per page.
**Must-haves:**
- Consistent header/footer across pages
- One key message per page
- Large fonts, minimal text
- Visual hierarchy through size, not density

**CSS tweaks:**
```css
@page { size: A4 landscape; margin: 15mm; }
body { font-size: 14pt; }
.slide { height: 100vh; display: flex; flex-direction: column; justify-content: center; }
.slide-title { font-size: 32pt; font-weight: 800; }
.slide-body { font-size: 18pt; color: #555; }
```
