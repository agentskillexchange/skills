#!/usr/bin/env python3.14
import fire
from pathlib import Path
import subprocess
import tempfile
from rich.console import Console
from rich.progress import track

console = Console()

DEFAULT_EXTENSIONS = [
    ".md", ".txt", ".py", ".rst", ".yaml", ".yml", ".json",
    ".ini", ".cfg", ".toml", ".sh", ".js", ".ts", ".java",
    ".c", ".cpp", ".h", ".hpp", ".cs", ".go", ".rb", ".php",
    ".html", ".css", ".ipynb"
] # Added more common code/text file types

def ingest_repo(
    repo_url: str,
    output_file: str = "ingested_repo_content.txt",
    extensions: list[str] = None,
    branch: str = None,
):
    """
    Clones a GitHub repository, extracts text content from specified file types,
    and combines it into a single output file, preserving directory structure context.

    Args:
        repo_url: The URL of the GitHub repository to clone (e.g., https://github.com/user/repo.git).
        output_file: The name of the file in the current directory to save the combined content to.
        extensions: A list of file extensions to include (e.g., ['.md', '.py']).
                    Defaults to a comprehensive list of common text-based formats.
        branch: The specific branch to clone. Defaults to the repo's default branch.
    """
    if extensions is None:
        extensions = DEFAULT_EXTENSIONS

    # Ensure extensions are lowercase and start with a dot for consistent matching
    normalized_extensions = []
    for ext in extensions:
        ext_lower = ext.lower()
        if not ext_lower.startswith('.'):
            normalized_extensions.append('.' + ext_lower)
        else:
            normalized_extensions.append(ext_lower)

    root_dir = Path.cwd()
    output_path = root_dir / output_file

    with tempfile.TemporaryDirectory(prefix="daedalus_ingest_") as tmpdir_name:
        clone_dir = Path(tmpdir_name) / "repo_content" # Give a more specific name to the cloned content

        console.print(f"[bold blue]Attempting to clone {repo_url}...[/]")
        git_command = ["git", "clone", "--depth", "1"]
        if branch:
            git_command.extend(["--branch", branch])
        git_command.extend(["--", repo_url, str(clone_dir)])

        try:
            # Using subprocess.run for better control and error handling
            process = subprocess.run(git_command, capture_output=True, text=True, check=False) # check=False to inspect output

            if process.returncode == 0:
                console.print(f"[green]Successfully cloned repository to temporary location: {clone_dir}[/]")
                if process.stdout:
                    console.print(f"[dim]Git clone stdout:\n{process.stdout}[/dim]")
                if process.stderr: # Git often uses stderr for progress, even on success
                    console.print(f"[dim]Git clone stderr:\n{process.stderr}[/dim]")
            else:
                console.print(f"[bold red]Error cloning repository {repo_url}:[/]")
                console.print(f"Return code: {process.returncode}")
                if process.stdout:
                     console.print(f"Stdout:\n{process.stdout}")
                if process.stderr:
                    console.print(f"Stderr:\n{process.stderr}")
                console.print("[yellow]Please check the URL, repository permissions, and that Git is correctly configured.[/yellow]")
                return

        except FileNotFoundError:
            console.print("[bold red]Error: Git command not found. Please ensure Git is installed and in your PATH.[/]")
            return
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred during git clone: {e}[/]")
            return

        all_content_parts = []
        files_processed_count = 0
        files_skipped_binary = 0

        console.print(f"[bold blue]Extracting content from files with extensions: {', '.join(normalized_extensions)}...[/]")

        # Collect all files first to use with track
        files_to_process = [
            f for f in clone_dir.rglob("*")
            if f.is_file() and not f.is_symlink()
            and ".git" not in f.relative_to(clone_dir).parts
            and f.suffix.lower() in normalized_extensions
        ]

        if not files_to_process:
            console.print(f"[yellow]No files found matching the specified extensions in the cloned repository.[/yellow]")
            return

        for file_path in track(files_to_process, description="Processing files"):
            try:
                relative_path = file_path.relative_to(clone_dir)
                header = f"==== START OF {relative_path} ===="
                footer = f"==== END OF {relative_path} ====\n" # Add a newline for better separation

                # Attempt to read as text, skip if it seems like binary
                try:
                    file_content = file_path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    # Try with another common encoding, or skip
                    try:
                        file_content = file_path.read_text(encoding="latin-1")
                    except UnicodeDecodeError:
                        console.print(f"[yellow]Skipping binary or non-text file (UnicodeDecodeError): {relative_path}[/yellow]")
                        files_skipped_binary +=1
                        continue # Skip this file

                all_content_parts.append(header)
                all_content_parts.append(file_content)
                all_content_parts.append(footer)
                files_processed_count += 1
            except Exception as e:
                # Log specific file processing error but continue with other files
                console.print(f"[yellow]Could not read or process file {file_path.relative_to(clone_dir)}: {e}[/yellow]")

        if files_skipped_binary > 0:
            console.print(f"[cyan]Note: Skipped {files_skipped_binary} binary or non-decodable files.[/cyan]")

        if not all_content_parts:
            console.print(f"[yellow]No text content could be extracted from files with the specified extensions in {repo_url}.[/yellow]")
            return

        console.print(f"[bold blue]Writing combined content of {files_processed_count} files to {output_path}...[/]")
        try:
            # Join with double newlines between file blocks for better readability
            output_path.write_text("\n\n".join(all_content_parts), encoding="utf-8")
            console.print(f"[bold green]Successfully wrote content to {output_path}.[/]")
            console.print(f"You can now ask me to read this file for ingestion if it's not too large.")
        except Exception as e:
            console.print(f"[bold red]Error writing to output file {output_path}: {e}[/]")

    console.print(f"[dim]Temporary directory {tmpdir_name} has been cleaned up.[/dim]")

if __name__ == "__main__":
    fire.Fire(ingest_repo)
