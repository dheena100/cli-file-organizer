from pathlib import Path
import json
import shutil

UNDO_LOG = Path("logs/undo_log.json")

UNDO_LOG.parent.mkdir(exist_ok=True)

if not UNDO_LOG.exists():
    UNDO_LOG.write_text("[]", encoding="utf-8")


def save_move(source: Path, destination: Path) -> None:
    print("save_move() called")
    print(source)
    print(destination)

    moves = []

    if UNDO_LOG.exists():
        try:
            with UNDO_LOG.open("r", encoding="utf-8") as file:
                moves = json.load(file)
        except (json.JSONDecodeError, UnicodeDecodeError):
            moves = []

    moves.append(
        {
            "source": str(source),
            "destination": str(destination),
        }
    )

    with UNDO_LOG.open("w", encoding="utf-8") as file:
        json.dump(moves, file, indent=4)


def undo_last_sort() -> None:
    """Undo all recorded file moves."""

    if not UNDO_LOG.exists():
        print("No undo log found.")
        return

    with UNDO_LOG.open("r", encoding="utf-8") as file:
        moves = json.load(file)

    if not moves:
        print("Nothing to undo.")
        return

    for move in reversed(moves):

        destination = Path(move["destination"])
        source = Path(move["source"])

        if destination.exists():
            source.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destination), str(source))
            print(f"Restored {source.name}")

    UNDO_LOG.write_text("[]", encoding="utf-8")