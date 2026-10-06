# Visual QA expert roster

Each expert reviews independently through one lens and must obey the negative constraint. Use the smallest tier that covers the release risk.

## Quick tier

### `visual-hierarchy`

- **Lens:** reading order, grouping, spacing rhythm, salience, and whether the primary task is visually obvious.
- **May not:** argue from copy quality, accessibility standards, or brand taste.

### `contrast-and-color`

- **Lens:** legibility across themes, state distinctions that rely on color, and obvious contrast risks visible in the pixels.
- **May not:** claim a numerical contrast ratio without measurement or critique composition.

### `control-affordance`

- **Lens:** whether controls look interactive, states look distinct, destructive actions are separated, and targets appear usable.
- **May not:** infer keyboard or screen-reader behavior from a screenshot.

### `responsive-layout`

- **Lens:** clipping, overflow, reflow, density, touch reach, and continuity across declared breakpoints.
- **May not:** critique desktop-only aesthetics or invent breakpoints absent from the manifest.

### `state-coverage`

- **Lens:** missing or broken empty, loading, error, disabled, first-run, and long-content states.
- **May not:** critique a populated happy path unless it demonstrates a boundary failure.

## Full tier additions

### `content-clarity`

- **Lens:** visible labels, action verbs, errors, confirmations, terminology consistency, and literal-reader clarity.
- **May not:** argue from typography, color, or product strategy.

### `wcag-structure`

- **Lens:** visible focus indicators, target sizing, zoom/reflow evidence, headings, labels, and error identification.
- **May not:** claim DOM semantics or assistive-technology behavior without non-visual evidence.

### `typography`

- **Lens:** type scale, weight contrast, measure, leading, alignment, wrapping, punctuation, and numeric alignment.
- **May not:** appeal to color, motion, or wording.

### `token-consistency`

- **Lens:** cross-screen drift in spacing, radius, shadows, component states, type tokens, and semantic colors.
- **May not:** declare a single isolated value wrong without comparative evidence.

### `transition-feedback`

- **Lens:** loading, pending, pressed, focus, success/failure, and open/close frames; whether actions visibly receive feedback.
- **May not:** claim measured latency, frame rate, or runtime performance from still images.

### `onscreen-privacy`

- **Lens:** sensitive values unnecessarily exposed in previews, notifications, shared screens, or transient states.
- **May not:** infer hidden data collection or backend security from rendered pixels.

### `temporal-honesty`

- **Lens:** freshness cues, relative-time consistency, stale-versus-live state, and visible “as of” anchors.
- **May not:** critique loading aesthetics or backend cache policy.

## Deep tier additions

### `source-fidelity`

- **Lens:** whether visible generated or transformed content is supported by a co-visible source.
- **May not:** judge unsupported claims when the source evidence is absent; request capture instead.

### `trust-and-consequence`

- **Lens:** whether confidence, provenance, authorization, recipients, costs, and irreversible consequences receive appropriate visual weight.
- **May not:** critique polish unless it manufactures unearned certainty.

### `localization-resilience`

- **Lens:** text expansion, bidirectional layout, locale-sensitive dates/numbers, and culture-bound symbols.
- **May not:** make generic spacing critiques without a named locale or script failure.

### `data-display-honesty`

- **Lens:** proportional encoding, axes, units, legends, aggregation, and whether displayed totals reconcile with visible detail.
- **May not:** comment on screens without quantitative displays.

### `signature-and-brand`

- **Lens:** distinctive identity, emotional peaks, and whether the product has a memorable visual protagonist.
- **May not:** appeal to reduction, efficiency, accessibility compliance, or correctness.

## Selection notes

- Quick is the five-seat smoke test.
- Full is the default twelve-seat audit.
- Deep adds specialists only when the corresponding evidence exists.
- Product-specific experts belong in the project's adapter, not this shared roster.
