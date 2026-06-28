import click
from pathlib import Path

from organizer.sorter import (
    sort_by_extension,
    sort_by_size,
    sort_by_date,
)


from organizer.logger import log_execution
from organizer.undo import undo_last_sort


@click.group()
def cli() -> None:
    """CLI File Organizer."""
    pass


@cli.command()
@click.option(
    "--by",
    type=click.Choice(["extension", "size", "date"], case_sensitive=False),
    required=True,
    help="Sort files by extension, size, or date.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would happen without moving files.",
)
@click.option(
    "--folder",
    default="sample_files",
    help="Folder to organize.",
)
@log_execution
def sort(by: str, dry_run: bool, folder: str) -> None:
    """Sort files."""

    path = Path(folder)

    if not path.exists():
        click.echo("Folder not found.")
        return

    if by == "extension":
        sort_by_extension(path, dry_run)

    elif by == "size":
        sort_by_size(path, dry_run)

    else:
        sort_by_date(path, dry_run)


@cli.command()
@log_execution
def undo() -> None:
    """Undo the last sorting operation."""
    undo_last_sort()


if __name__ == "__main__":
    cli()