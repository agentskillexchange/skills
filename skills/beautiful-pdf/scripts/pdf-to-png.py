#!/usr/bin/env python3
"""Convert PDF pages to PNG images for visual QA review.

Usage:
    python3 pdf-to-png.py input.pdf output_dir/ [--dpi 200]

Outputs one PNG per page: output_dir/page-1.png, page-2.png, etc.
Requires: PyMuPDF (fitz)
"""

import argparse
import sys
from pathlib import Path


def ensure_pymupdf() -> None:
    """Fail with a clear message when PyMuPDF is unavailable."""
    try:
        import fitz  # noqa: F401
    except ImportError:
        raise SystemExit(
            "PyMuPDF is required. Install it in the active environment with: "
            "python -m pip install PyMuPDF"
        )


def pdf_to_png(pdf_path: str, output_dir: str, dpi: int = 200) -> list[str]:
    """Convert each page of a PDF to a PNG image.

    Args:
        pdf_path: Path to the input PDF file.
        output_dir: Directory to write PNG files to.
        dpi: Resolution for rendering (default 200 for good quality without huge files).

    Returns:
        List of output PNG file paths.
    """
    ensure_pymupdf()
    import fitz

    pdf = Path(pdf_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    if not pdf.exists():
        print(f"Error: PDF not found: {pdf}", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(str(pdf))
    output_files: list[str] = []
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=matrix)
        out_path = out / f"page-{i + 1}.png"
        pix.save(str(out_path))
        output_files.append(str(out_path))
        print(f"  ✓ {out_path} ({pix.width}x{pix.height})")

    doc.close()
    print(f"\nConverted {len(output_files)} pages to {out}")
    return output_files


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG for visual QA")
    parser.add_argument("pdf", help="Input PDF file")
    parser.add_argument("output_dir", help="Output directory for PNG files")
    parser.add_argument("--dpi", type=int, default=200, help="Render DPI (default: 200)")
    args = parser.parse_args()

    pdf_to_png(args.pdf, args.output_dir, args.dpi)


if __name__ == "__main__":
    main()
