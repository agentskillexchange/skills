# Beautiful PDF

An agent skill for turning Markdown or HTML into a designed PDF—and checking the pages a reader will actually see.

A successful export only tells you that a PDF exists. It does not tell you whether a heading was stranded at the foot of a page, a table was clipped, or the most important number disappeared into dense text. Beautiful PDF makes page layout and rendered-page inspection part of the job, not a final optional polish pass.

Use it for reports, proposals, briefs, CVs, invoices, letters, and dossiers where the layout has to carry the content. For example, a proposal can keep its editable Markdown source while gaining consistent headings, readable budget tables, page numbers, and a review of every exported page.

## How it works

1. Choose a [document pattern](references/doc-types.md) and start in Markdown for linear content or static HTML for custom layouts.
2. Adapt the [A4 stylesheet](assets/default.css) and [style guide](references/style-guide.md): typography, margins, restrained colour, tables, callouts, and page breaks.
3. Render with Pandoc and WeasyPrint, or with WeasyPrint directly for HTML.
4. Convert **every page** to a PNG and inspect the actual render. Fix overflow, awkward breaks, weak hierarchy, clipping, contrast, and inconsistent spacing; then render and inspect again.
5. Deliver the PDF with its editable source, final page count, output path, and a short account of what was visually checked.

The package is a workflow, stylesheet, reference patterns, and a PDF-to-PNG helper. It is not a new PDF engine or a standalone design application. Pandoc/WeasyPrint render the document; the helper rasterizes it; your agent's image-reading tools and judgment perform the review. Creating PNGs alone does not mean the pages were reviewed.

## Install

```bash
npx skills add AntreasAntoniou/beautiful-pdf
```

The package contains a portable skill, a production-oriented A4 stylesheet, document patterns, and a PDF-to-PNG review helper. Rendering dependencies are intentionally not installed automatically.

You need Pandoc for the Markdown route, WeasyPrint for rendering, and Python with PyMuPDF for page images. The agent also needs a way to inspect those images. Missing dependencies must be reported rather than silently installed.

## Render and review

Run these commands from the skill checkout, adjusting the input and output paths to your project:

```bash
# Markdown to PDF
pandoc input.md --standalone --pdf-engine=weasyprint --css=assets/default.css -o output.pdf

# Or static HTML with its stylesheet linked or embedded
weasyprint input.html output.pdf

# One image per page for inspection
python3 scripts/pdf-to-png.py output.pdf /tmp/pdf-qa --dpi 200
```

The helper writes `page-1.png`, `page-2.png`, and so on. Use a fresh review directory for each document or revision so old page images cannot be mistaken for current output. Open all the images, correct the source/CSS, and repeat as needed. Preserve the source alongside the PDF and use a user-approved delivery destination.

## Limits and care

The default is an A4 starting point, not a guarantee that every document will fit. Fonts, long tables, images, and page size still need attention. WeasyPrint does not execute JavaScript, so dynamic charts or interactive content must be represented statically. Use absolute or `file://` paths for local images and fonts, and avoid adding Pandoc title metadata when the Markdown already has an H1.

Visual review is not factual verification, accessibility certification, or commercial-print preflight. This package does not sandbox untrusted documents or grant authority to distribute a finished PDF. Read [SECURITY.md](SECURITY.md) before processing sensitive material, and keep source files and page images private when the content is private.

## Test

```bash
python3 -m unittest discover -s tests
```

These are package checks, not an end-to-end rendering or visual-quality test.

## License

MIT. See [LICENSE](LICENSE).
