from pathlib import Path
import shutil


def get_destination(file, folder):
    extension = file.suffix.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        return folder / "images"

    elif extension == ".pdf":
        return folder / "pdf"

    elif extension == ".csv":
        return folder / "csv"

    elif extension == ".txt":
        return folder / "text"

    return None


def move_file(file, destination):
    destination.mkdir(exist_ok=True)

    new_path = destination / file.name

    if new_path.exists():
        print(f"同名ファイルが存在するためスキップ: {file.name}")
        return

    shutil.move(str(file), str(new_path))

    print(f"{file.name} -> {destination}")


def organize_files(folder):
    for file in folder.iterdir():

        if not file.is_file():
            continue

        destination = get_destination(file, folder)

        if destination is None:
            print(f"対応していないファイル: {file.name}")
            continue

        move_file(file, destination)


def main():
    folder = Path("test_files")
    organize_files(folder)


if __name__ == "__main__":
    main()
