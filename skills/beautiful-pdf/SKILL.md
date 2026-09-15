---
name: "Beautiful PDF"
slug: "beautiful-pdf"
description: "Produce polished, print-ready PDFs from Markdown or HTML with Pandoc, WeasyPrint, reusable CSS, and a mandatory rendered-page review loop. Use for reports, proposals, briefs, CVs, invoices, letters, dossiers, and other documents where layout quality matters."
category: "Image & Creative Automation"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/beautiful-pdf"
---

# Beautiful PDF

Turn structured content into a designed document, then inspect the rendered pages before delivery.

## Workflow

1. Choose the document pattern in [references/doc-types.md](references/doc-types.md).
2. Draft in Markdown for linear documents or HTML for custom layouts.
3. Start from [assets/default.css](assets/default.css) and select a restrained palette from [references/style-guide.md](references/style-guide.md).
4. Render:

   ```bash
   pandoc input.md --standalone --pdf-engine=weasyprint --css=assets/default.css -o output.pdf
   # Or, for hand-authored HTML:
   weasyprint input.html output.pdf
   ```

5. Rasterize every page and inspect it:

   ```bash
   python3 scripts/pdf-to-png.py output.pdf /tmp/pdf-qa --dpi 200
   ```

6. Fix overflow, weak hierarchy, widows/orphans, awkward breaks, clipped tables, low contrast, and inconsistent spacing. Render again until the pages are intentional.

## Guardrails

- Do not pass Pandoc `--metadata title` when Markdown already contains an H1; it duplicates the title.
- Keep source HTML static. WeasyPrint does not execute JavaScript.
- Use absolute or `file://` paths for local images and fonts.
- Preserve the original source alongside the PDF so later edits remain possible.
- Treat page inspection as part of completion, not an optional polish pass.
- Never silently install dependencies. If PyMuPDF, Pandoc, or WeasyPrint is missing, report the exact requirement.

## Output

Use a user-approved destination. When no convention exists, prefer:

```text
outputs/YYYY-MM-DD-descriptor.pdf
```

Before delivery, report the final page count, output path, and the visual issues checked.

## Installation and upstream provenance

The upstream skill identifier is `beautiful-pdf`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/beautiful-pdf --skill beautiful-pdf --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/beautiful-pdf#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`2414b1278f1f`](https://github.com/AntreasAntoniou/beautiful-pdf/tree/2414b1278f1f719a6d7fc24538090fe72741920d). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
