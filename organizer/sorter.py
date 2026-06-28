from pathlib import Path
from datetime import datetime
import shutil

from organizer.undo import save_move
from organizer.models import SortStatistics


EXTENSION_MAP = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".mkv": "Videos",
}


def update_statistics(stats: SortStatistics, category: str) -> None:
    """Update sorting statistics."""

    stats.total_files += 1

    if category == "Images":
        stats.images += 1
    elif category == "Documents":
        stats.documents += 1
    elif category == "Music":
        stats.music += 1
    elif category == "Videos":
        stats.videos += 1
    else:
        stats.others += 1


def move_file(
    file: Path,
    destination_folder: Path,
    dry_run: bool,
    stats: SortStatistics,
) -> None:
    """Move a file safely and update statistics."""

    destination_file = destination_folder / file.name

    if dry_run:
        print(f"[DRY RUN] {file.name} -> {destination_folder.name}/")
        update_statistics(stats, destination_folder.name)
        return

    destination_folder.mkdir(exist_ok=True)

    try:
        shutil.move(str(file), str(destination_file))
        save_move(file, destination_file)

        print(f"Moved {file.name} -> {destination_folder.name}/")

        update_statistics(stats, destination_folder.name)

    except PermissionError:
        print(f"Permission denied: {file.name}")

    except Exception as error:
        print(f"Error moving {file.name}: {error}")


def print_summary(stats: SortStatistics) -> None:
    """Print sorting summary."""

    print("\n========== Summary ==========")
    print(f"Moved Files : {stats.total_files}")
    print(f"Images      : {stats.images}")
    print(f"Documents   : {stats.documents}")
    print(f"Music       : {stats.music}")
    print(f"Videos      : {stats.videos}")
    print(f"Others      : {stats.others}")
    print("=============================")


def sort_by_extension(folder: Path, dry_run: bool = False) -> None:
    """Sort files by extension."""

    stats = SortStatistics()

    for file in folder.iterdir():

        if not file.is_file():
            continue

        if file.name.startswith("."):
            continue

        category = EXTENSION_MAP.get(file.suffix.lower(), "Others")

        destination_folder = folder / category

        move_file(file, destination_folder, dry_run, stats)

    print_summary(stats)


def sort_by_size(folder: Path, dry_run: bool = False) -> None:
    """Sort files by size."""

    stats = SortStatistics()

    for file in folder.iterdir():

        if not file.is_file():
            continue

        if file.name.startswith("."):
            continue

        size = file.stat().st_size

        if size < 1024 * 1024:
            category = "Small"
        elif size < 10 * 1024 * 1024:
            category = "Medium"
        else:
            category = "Large"

        destination_folder = folder / category

        move_file(file, destination_folder, dry_run, stats)

    print_summary(stats)


def sort_by_date(folder: Path, dry_run: bool = False) -> None:
    """Sort files by last modified year."""

    stats = SortStatistics()

    for file in folder.iterdir():

        if not file.is_file():
            continue

        if file.name.startswith("."):
            continue

        modified_date = datetime.fromtimestamp(file.stat().st_mtime)

        category = str(modified_date.year)

        destination_folder = folder / category

        move_file(file, destination_folder, dry_run, stats)

    print_summary(stats)