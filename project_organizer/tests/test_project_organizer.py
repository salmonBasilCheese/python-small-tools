from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from project_organizer import get_destination, organize_file, organize_folder


def test_python_file_goes_to_python():
    file = Path("example.py")

    assert get_destination(file) == "python"


def test_csv_file_goes_to_csv():
    file = Path("example.csv")

    assert get_destination(file) == "csv"


def test_test_folder_goes_to_tests():
    folder = Path("example_test")

    assert get_destination(folder) == "tests"


def test_readme_is_ignored():
    file = Path("README.md")

    assert get_destination(file) is None


def test_venv_is_ignored():
    folder = Path(".venv")

    assert get_destination(folder) is None


def test_python_destination_path():
    root = Path("..")

    result = get_destination(Path("example.py"))

    assert root / result == Path("..") / "python"


def test_csv_destination_path():
    root = Path("..")

    result = get_destination(Path("example.csv"))

    assert root / result == Path("..") / "csv"


def test_organize_python_file(tmp_path):
    file = tmp_path / "example.py"
    file.write_text("print('hello')")

    organize_file(file, tmp_path)

    assert (tmp_path / "python" / "example.py").exists()
    assert not file.exists()


def test_organize_csv_file(tmp_path):
    file = tmp_path / "example.csv"
    file.write_text("name,score")

    organize_file(file, tmp_path)

    assert (tmp_path / "csv" / "example.csv").exists()
    assert not file.exists()


def test_organize_test_folder(tmp_path):
    folder = tmp_path / "example_test"
    folder.mkdir()

    organize_folder(folder, tmp_path)

    assert (tmp_path / "tests" / "example_test").exists()
    assert not folder.exists()
