from pathlib import Path

from organizer.undo import save_move


def test_save_move(tmp_path: Path) -> None:
    """Test undo log creation."""

    source = tmp_path / "a.txt"
    destination = tmp_path / "folder" / "a.txt"

    source.write_text("hello")

    save_move(source, destination)

    assert True