from pathlib import Path

from file_organizer import get_destination, move_file


def test_jpg_destination():
    folder = Path("test_files")
    result = get_destination(Path("photo.jpg"), folder)
    assert result == folder / "images"


def test_pdf_destination():
    folder = Path("test_files")
    result = get_destination(Path("document.pdf"), folder)
    assert result == folder / "pdf"


def test_csv_destination():
    folder = Path("test_files")
    result = get_destination(Path("data.csv"), folder)
    assert result == folder / "csv"


def test_txt_destination():
    folder = Path("test_files")
    result = get_destination(Path("memo.txt"), folder)
    assert result == folder / "text"


def test_unsupported_extension():
    folder = Path("test_files")
    result = get_destination(Path("program.py"), folder)
    assert result is None


def test_move_file(tmp_path):
    source = tmp_path / "test.txt"
    destination = tmp_path / "text"

    source.write_text("hello", encoding="utf-8")

    move_file(source, destination)

    assert not source.exists()
    assert (destination / "test.txt").exists()


def test_move_file_duplicate(tmp_path):
    source = tmp_path / "test.txt"
    destination = tmp_path / "text"

    source.write_text("new", encoding="utf-8")
    destination.mkdir()
    (destination / "test.txt").write_text("old", encoding="utf-8")

    move_file(source, destination)

    assert source.exists()
    assert (destination / "test.txt").read_text(encoding="utf-8") == "old"
