# PDF Style Guide — Professional Document Patterns

## Typography

### Font Stack (System Fonts — No Installation Required)
```css
/* Primary — clean sans-serif */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;

/* Headings — tighter, bolder */
font-family: 'Helvetica Neue', Arial, sans-serif;

/* Monospace — for code/data */
font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
```

### Font Sizes (A4 optimised)
```css
body { font-size: 10.5pt; line-height: 1.5; }
h1 { font-size: 22pt; font-weight: 700; margin-bottom: 0.3em; }
h2 { font-size: 16pt; font-weight: 600; margin-top: 1.5em; margin-bottom: 0.4em; }
h3 { font-size: 12pt; font-weight: 600; margin-top: 1.2em; margin-bottom: 0.3em; }
.small { font-size: 9pt; }
.caption { font-size: 8.5pt; color: #666; }
```

### Type Scale for Impact Docs (Proposals, Briefs)
```css
.hero-title { font-size: 28pt; font-weight: 800; letter-spacing: -0.5px; }
.subtitle { font-size: 14pt; font-weight: 400; color: #555; }
.section-title { font-size: 18pt; font-weight: 700; border-bottom: 2px solid #333; padding-bottom: 4px; }
```

## Colour Palettes

### Professional Neutral
```css
:root {
  --text: #1a1a1a;
  --text-secondary: #555;
  --text-muted: #888;
  --accent: #2563eb;       /* blue */
  --accent-dark: #1d4ed8;
  --border: #e5e7eb;
  --bg-subtle: #f9fafb;
  --bg-highlight: #eff6ff;
}
```

### Corporate Dark
```css
:root {
  --text: #111827;
  --accent: #0f172a;       /* near-black */
  --accent-secondary: #475569;
  --highlight: #f59e0b;    /* amber */
  --border: #d1d5db;
  --bg-subtle: #f3f4f6;
}
```

### Coral and Navy
```css
:root {
  --text: #1a1a2e;
  --accent: #e94560;       /* coral */
  --accent-dark: #c23152;
  --secondary: #0f3460;    /* deep blue */
  --bg-subtle: #f8f9fa;
  --border: #dee2e6;
}
```

## Page Layout

### A4 Base Layout
```css
@page {
  size: A4;
  margin: 25mm 20mm 25mm 20mm;

  @bottom-center {
    content: counter(page);
    font-size: 9pt;
    color: #888;
  }
}

@page :first {
  margin-top: 15mm;  /* less top margin on first page for title impact */
}
```

### US Letter Layout
```css
@page {
  size: letter;
  margin: 1in 0.85in;
}
```

### Two-Column Layout
```css
.two-col {
  column-count: 2;
  column-gap: 20px;
  column-rule: 1px solid var(--border);
}
```

## Common Components

### Header Bar (Branded)
```css
.header-bar {
  background: var(--accent);
  color: white;
  padding: 15px 20px;
  margin: -25mm -20mm 20px -20mm;  /* bleeds to edges */
  width: calc(100% + 40mm);
}
```

### Metric Box / KPI Card
```css
.metric-box {
  display: inline-block;
  text-align: center;
  padding: 12px 20px;
  border: 1px solid var(--border);
  border-radius: 6px;
  margin: 4px;
}
.metric-box .value { font-size: 24pt; font-weight: 700; color: var(--accent); }
.metric-box .label { font-size: 8.5pt; color: var(--text-secondary); }
```

### Table
```css
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9.5pt;
  margin: 12px 0;
}
th {
  background: var(--bg-subtle);
  font-weight: 600;
  text-align: left;
  padding: 8px 10px;
  border-bottom: 2px solid var(--border);
}
td {
  padding: 6px 10px;
  border-bottom: 1px solid var(--border);
}
tr:hover { background: var(--bg-highlight); }
```

### Callout / Highlight Box
```css
.callout {
  background: var(--bg-highlight);
  border-left: 4px solid var(--accent);
  padding: 12px 16px;
  margin: 16px 0;
  border-radius: 0 4px 4px 0;
}
```

### Blockquote
```css
blockquote {
  border-left: 3px solid var(--accent);
  margin: 16px 0;
  padding: 8px 16px;
  color: var(--text-secondary);
  font-style: italic;
}
```

## Print Considerations

```css
/* Avoid page breaks inside key elements */
h1, h2, h3 { page-break-after: avoid; }
table, figure, .callout { page-break-inside: avoid; }

/* Force page breaks where needed */
.page-break { page-break-before: always; }

/* Hide screen-only elements */
@media print {
  .no-print { display: none; }
}
```

## Complete Starter Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4;
    margin: 25mm 20mm;
    @bottom-center { content: counter(page); font-size: 9pt; color: #888; }
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #1a1a1a;
  }
  h1 { font-size: 22pt; font-weight: 700; margin-bottom: 0.3em; }
  h2 { font-size: 16pt; font-weight: 600; margin-top: 1.5em; margin-bottom: 0.4em; border-bottom: 2px solid #e5e7eb; padding-bottom: 4px; }
  h3 { font-size: 12pt; font-weight: 600; margin-top: 1.2em; margin-bottom: 0.3em; }
  p { margin-bottom: 0.8em; }
  table { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin: 12px 0; }
  th { background: #f9fafb; font-weight: 600; text-align: left; padding: 8px 10px; border-bottom: 2px solid #e5e7eb; }
  td { padding: 6px 10px; border-bottom: 1px solid #e5e7eb; }
  .callout { background: #eff6ff; border-left: 4px solid #2563eb; padding: 12px 16px; margin: 16px 0; border-radius: 0 4px 4px 0; }
  .subtitle { font-size: 14pt; color: #555; margin-bottom: 1.5em; }
  .page-break { page-break-before: always; }
</style>
</head>
<body>
  <!-- Document content here -->
</body>
</html>
```

## WeasyPrint Tips

- Use `@page` rules for margins and page numbers — WeasyPrint supports them natively
- Embedded fonts: use `@font-face` with local file paths (`file:///path/to/font.woff2`)
- Images: use absolute paths or `file://` URLs
- CSS Grid works. Flexbox works. `column-count` works.
- For background colours that bleed to edges, use negative margins matching @page margins
- `page-break-before: always` and `page-break-inside: avoid` both work
- WeasyPrint does NOT support JavaScript — all content must be static HTML/CSS
