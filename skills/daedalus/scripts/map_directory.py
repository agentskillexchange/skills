import pathlib
import fire
import ast
from rich.console import Console

console = Console()


def _get_signature(node):
    """Extracts a simplified signature from a function or class AST node."""
    if isinstance(node, ast.FunctionDef) or isinstance(
        node, ast.AsyncFunctionDef
    ):
        args = [arg.arg for arg in node.args.args]
        return f"{node.name}({', '.join(args)})"
    elif isinstance(node, ast.ClassDef):
        return f"class {node.name}:"
    return ""


def map_directory_structure(
    root_dir: str,
    output_file: str,
    ignore_dirs: list[str] = None,
):
    """
    Generates a markdown file representing the directory structure,
    including classes and functions from Python files.

    Args:
        root_dir (str): The root directory to map.
        output_file (str): The path to the output markdown file.
        ignore_dirs (list[str]): A list of directory names to ignore.
    """
    root_path = pathlib.Path(root_dir).resolve()
    output_path = pathlib.Path(output_file)
    if ignore_dirs is None:
        ignore_dirs = ["__pycache__", ".git", ".vscode", "venv", ".idea"]

    console.print(
        f"🗺️  Mapping directory structure of [bold cyan]{root_path}[/bold cyan]..."
    )

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(f"# Directory Map of {root_path.name}\n\n")

        def recurse_path(path, prefix=""):
            # Sort items, directories first
            items = sorted(
                (p for p in path.iterdir() if not p.is_symlink()
                 and p.resolve() != output_path.resolve()
                 and not (p.is_dir() and p.name in ignore_dirs)),
                key=lambda p: (not p.is_dir(), p.name),
            )

            for i, item in enumerate(items):
                is_last = i == len(items) - 1
                connector = "└── " if is_last else "├── "

                if item.is_dir():
                    if item.name in ignore_dirs:
                        continue
                    outfile.write(f"{prefix}{connector}{item.name}/\n")
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    recurse_path(item, new_prefix)
                else:
                    outfile.write(f"{prefix}{connector}{item.name}\n")
                    new_prefix = prefix + (
                        "    " if is_last else "│   "
                    )  # DEFINE new_prefix before try block
                    if item.suffix == ".py":
                        try:
                            with open(item, "r", encoding="utf-8") as py_file:
                                content = py_file.read()
                                tree = ast.parse(content)
                                for node in ast.walk(tree):
                                    if isinstance(
                                        node,
                                        (
                                            ast.FunctionDef,
                                            ast.AsyncFunctionDef,
                                            ast.ClassDef,
                                        ),
                                    ):
                                        # We only want top-level functions/classes
                                        if (
                                            isinstance(node, ast.ClassDef)
                                            and node.col_offset == 0
                                        ):
                                            outfile.write(
                                                f"{new_prefix}  - {_get_signature(node)}\n"
                                            )
                                        elif (
                                            isinstance(
                                                node,
                                                (
                                                    ast.FunctionDef,
                                                    ast.AsyncFunctionDef,
                                                ),
                                            )
                                            and node.col_offset == 0
                                        ):
                                            outfile.write(
                                                f"{new_prefix}  - {_get_signature(node)}\n"
                                            )

                        except Exception as e:
                            outfile.write(
                                f"{new_prefix}  - (Could not parse: {e})\n"
                            )

        recurse_path(root_path)

    console.print(
        f"✅ Successfully created directory map at [bold cyan]{output_path}[/bold cyan]."
    )


if __name__ == "__main__":
    fire.Fire(map_directory_structure)
