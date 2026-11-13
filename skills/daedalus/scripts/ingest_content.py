import pathlib
import fire
from rich.progress import track
from rich.console import Console

console = Console()

def ingest_content(
    root_dir: str,
    output_file: str,
    extensions: list[str] = ['.py', '.md', '.html', '.css', '.js'],
):
    """
    Ingests content from files with specified extensions from a root directory
    into a single text file.

    Args:
        root_dir (str): The root directory to search for files.
        output_file (str): The path to the output text file.
        extensions (list[str]): A list of file extensions to include.
    """
    root_path = pathlib.Path(root_dir)
    output_path = pathlib.Path(output_file)

    console.print(f"🔍 Starting ingestion from [bold cyan]{root_path}[/bold cyan]...")

    # First, find all relevant files
    files_to_ingest = []
    for ext in extensions:
        files_to_ingest.extend(
            p for p in root_path.rglob(f"*{ext}")
            if p.is_file() and not p.is_symlink()
            and p.resolve() != output_path.resolve()
        )

    if not files_to_ingest:
        console.print("[bold red]No files found with the specified extensions.[/bold red]")
        return

    console.print(f"Found [bold green]{len(files_to_ingest)}[/bold green] files to ingest.")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for file_path in track(files_to_ingest, description="Ingesting files..."):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    content = infile.read()
                    outfile.write(f"--- Start of {file_path.relative_to(root_path)} ---\n\n")
                    outfile.write(content)
                    outfile.write(f"\n\n--- End of {file_path.relative_to(root_path)} ---\n\n")
            except Exception as e:
                console.print(f"[bold red]Error reading {file_path}: {e}[/bold red]")

    console.print(f"✅ Successfully ingested content into [bold cyan]{output_path}[/bold cyan].")

if __name__ == '__main__':
    fire.Fire(ingest_content)
