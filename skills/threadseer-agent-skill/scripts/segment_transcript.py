#!/usr/bin/env python3
"""Segment conversational text while preserving original line ranges and hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Block:
    start_line: int
    end_line: int
    text: str


@dataclass(frozen=True)
class Chunk:
    id: str
    start_line: int
    end_line: int
    char_count: int
    sha256: str
    text: str


def read_source(path: str) -> tuple[str, str]:
    if path == "-":
        return sys.stdin.read(), "stdin"
    source_path = Path(path).expanduser()
    return source_path.read_text(encoding="utf-8"), str(source_path.resolve())


def split_long_line(text: str, line_number: int, max_chars: int) -> list[Block]:
    if len(text) <= max_chars:
        return [Block(line_number, line_number, text)]
    return [
        Block(line_number, line_number, text[offset : offset + max_chars])
        for offset in range(0, len(text), max_chars)
    ]


def make_blocks(text: str, max_chars: int) -> list[Block]:
    lines = text.splitlines()
    blocks: list[Block] = []
    current: list[str] = []
    start_line = 1

    def flush(end_line: int) -> None:
        nonlocal current, start_line
        if current:
            block_text = "\n".join(current).strip("\n")
            if block_text:
                if len(block_text) <= max_chars:
                    blocks.append(Block(start_line, end_line, block_text))
                else:
                    for offset, line in enumerate(current):
                        blocks.extend(split_long_line(line, start_line + offset, max_chars))
            current = []

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            flush(line_number - 1)
            start_line = line_number + 1
            continue
        if not current:
            start_line = line_number
        current.append(line)
    flush(len(lines))
    return blocks


def make_chunks(blocks: list[Block], max_chars: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    pending: list[Block] = []
    pending_chars = 0

    def flush() -> None:
        nonlocal pending, pending_chars
        if not pending:
            return
        chunk_text = "\n\n".join(block.text for block in pending)
        chunks.append(
            Chunk(
                id=f"C{len(chunks) + 1:03d}",
                start_line=pending[0].start_line,
                end_line=pending[-1].end_line,
                char_count=len(chunk_text),
                sha256=hashlib.sha256(chunk_text.encode("utf-8")).hexdigest(),
                text=chunk_text,
            )
        )
        pending = []
        pending_chars = 0

    for block in blocks:
        separator_chars = 2 if pending else 0
        if pending and pending_chars + separator_chars + len(block.text) > max_chars:
            flush()
            separator_chars = 0
        pending.append(block)
        pending_chars += separator_chars + len(block.text)
    flush()
    return chunks


def render_markdown(source: str, source_hash: str, chunks: list[Chunk]) -> str:
    output = [
        f"# Segmented transcript: {source}",
        "",
        f"Source SHA-256: `{source_hash}`",
        "",
    ]
    for chunk in chunks:
        output.extend(
            [
                f"## {chunk.id} — lines {chunk.start_line}-{chunk.end_line}",
                "",
                f"Chunk SHA-256: `{chunk.sha256}`",
                "",
                chunk.text,
                "",
            ]
        )
    return "\n".join(output).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default="-", help="UTF-8 text file or - for stdin")
    parser.add_argument("--max-chars", type=int, default=16_000, help="Maximum characters per chunk")
    parser.add_argument("--format", choices=("json", "jsonl", "markdown"), default="json")
    parser.add_argument("--source-label", help="Replace the local path in output with an audience-safe source identifier")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_chars < 500:
        print("error: --max-chars must be at least 500", file=sys.stderr)
        return 2

    try:
        text, source = read_source(args.source)
        if args.source_label:
            source = args.source_label
    except (OSError, UnicodeError) as exc:
        print(f"error: unable to read source: {exc}", file=sys.stderr)
        return 2

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    source_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    chunks = make_chunks(make_blocks(normalized, args.max_chars), args.max_chars)

    if args.format == "markdown":
        sys.stdout.write(render_markdown(source, source_hash, chunks))
    elif args.format == "jsonl":
        for chunk in chunks:
            record = {"source": source, "source_sha256": source_hash, **asdict(chunk)}
            print(json.dumps(record, ensure_ascii=False))
    else:
        payload = {
            "source": source,
            "source_sha256": source_hash,
            "line_count": len(normalized.splitlines()),
            "chunk_count": len(chunks),
            "chunks": [asdict(chunk) for chunk in chunks],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
