from pathlib import Path

from organizer.sorter import sort_by_extension


def test_sort_by_extension(tmp_path: Path) -> None:
    """Test sorting files by extension."""

    # Create sample files
    (tmp_path / "photo.jpg").write_text("image")
    (tmp_path / "notes.txt").write_text("notes")
    (tmp_path / "report.pdf").write_text("report")

    sort_by_extension(tmp_path)

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Documents" / "notes.txt").exists()
    assert (tmp_path / "Documents" / "report.pdf").exists()