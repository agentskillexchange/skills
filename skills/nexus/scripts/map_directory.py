#!/usr/bin/env python3
"""Map paths and top-level Python symbols without importing repository code."""
import argparse
import ast
import fnmatch
import os
import pathlib
import sys

DEFAULT_IGNORE_DIRS = {
    "__pycache__", "venv", "node_modules", "vendor", "dist", "build", "target",
    "coverage", "credentials", "secrets",
}
DEFAULT_IGNORE_FILES = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx", "id_rsa*", "id_ed25519*",
    "credentials*", "secret*",
}


def _get_signature(node):
    """Return names only: defaults/annotations may contain sensitive values."""
    if isinstance(node, ast.ClassDef):
        return f"class {node.name}:"
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = [a.arg for a in node.args.posonlyargs + node.args.args]
        if node.args.vararg:
            args.append("*" + node.args.vararg.arg)
        elif node.args.kwonlyargs:
            args.append("*")
        args.extend(a.arg for a in node.args.kwonlyargs)
        if node.args.kwarg:
            args.append("**" + node.args.kwarg.arg)
        return f"{node.name}({', '.join(args)})"
    return ""


def _display(name):
    """Keep path control characters from injecting lines into a map."""
    return "".join(c if c.isprintable() else f"\\u{ord(c):04x}" for c in name)


def map_directory_structure(root_dir, output_file, ignore_dirs=None,
                            ignore_files=None, max_source_bytes=1_000_000):
    """Create an exclusive output; exclusions augment defaults, never replace them.

    Traversal does not follow symlinks. This is not a sandbox against another
    process concurrently replacing files. Use a stable authorized checkout.
    """
    root = pathlib.Path(root_dir).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("root must be a directory")
    output = pathlib.Path(output_file).absolute()
    if output.resolve().is_relative_to(root):
        raise ValueError("output must be outside the mapped directory")
    if max_source_bytes < 1:
        raise ValueError("max_source_bytes must be positive")
    ignored_dirs = DEFAULT_IGNORE_DIRS | set(ignore_dirs or ())
    ignored_files = DEFAULT_IGNORE_FILES | set(ignore_files or ())
    lines = [f"# Directory Map of {_display(root.name)}", "",
             "Inventory only; hidden entries, configured exclusions, and symlinks omitted.",
             "Python symbols are static top-level names; source is not executed.", ""]

    def visit(directory, prefix=""):
        try:
            entries = []
            for item in directory.iterdir():
                if item.is_symlink() or item.name.startswith("."):
                    continue
                if item.is_dir() and item.name in ignored_dirs:
                    continue
                if any(fnmatch.fnmatch(item.name.lower(), p.lower()) for p in ignored_files):
                    continue
                if item.is_dir() or item.is_file():
                    entries.append(item)
            entries.sort(key=lambda p: (not p.is_dir(), p.name.casefold(), p.name))
        except OSError as exc:
            lines.append(f"{prefix}[directory unreadable: {type(exc).__name__}]")
            return
        for index, item in enumerate(entries):
            last = index == len(entries) - 1
            connector = "└── " if last else "├── "
            child_prefix = prefix + ("    " if last else "│   ")
            is_dir = item.is_dir()
            lines.append(f"{prefix}{connector}{_display(item.name)}{'/' if is_dir else ''}")
            if is_dir:
                visit(item, child_prefix)
            elif item.suffix == ".py":
                try:
                    if item.stat().st_size > max_source_bytes:
                        lines.append(f"{child_prefix}  - [source exceeds byte limit]")
                        continue
                    with item.open("rb") as stream:
                        content = stream.read(max_source_bytes + 1)
                    if len(content) > max_source_bytes:
                        lines.append(f"{child_prefix}  - [source exceeds byte limit]")
                        continue
                    # ast.parse(bytes) honors Python encoding declarations.
                    tree = ast.parse(content, filename=item.name)
                    for node in tree.body:
                        signature = _get_signature(node)
                        if signature:
                            lines.append(f"{child_prefix}  - {signature}")
                except (OSError, SyntaxError, UnicodeError, ValueError, RecursionError) as exc:
                    # Exception messages can echo private source lines and paths.
                    lines.append(f"{child_prefix}  - [source not parsed: {type(exc).__name__}]")

    visit(root)
    descriptor = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root_dir")
    parser.add_argument("output_file", help="new output outside root; parent must exist")
    parser.add_argument("--ignore-dir", action="append", default=[], help="additional directory name")
    parser.add_argument("--ignore-file", action="append", default=[], help="additional filename glob")
    parser.add_argument("--max-source-bytes", type=int, default=1_000_000)
    args = parser.parse_args(argv)
    try:
        output = map_directory_structure(args.root_dir, args.output_file,
                                         args.ignore_dir, args.ignore_file,
                                         args.max_source_bytes)
    except (OSError, ValueError) as exc:
        print(f"Mapping failed ({type(exc).__name__}): {exc}", file=sys.stderr)
        return 1
    print(f"Created directory map: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
