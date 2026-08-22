from pathlib import Path
import shutil


def get_destination(path):
    if path.suffix == ".py":
        return "python"

    if path.suffix == ".csv":
        return "csv"

    if path.name.endswith("_test"):
        return "tests"

    return None


def organize_file(file, root):
    destination_name = get_destination(file)

    if destination_name is None:
        return

    destination = root / destination_name
    destination.mkdir(exist_ok=True)

    new_path = destination / file.name

    print(file, "->", new_path)

    shutil.move(file, new_path)


def organize_folder(folder, root):
    destination_name = get_destination(folder)

    if destination_name is None:
        return

    destination = root / destination_name
    destination.mkdir(exist_ok=True)

    new_path = destination / folder.name

    print(folder, "->", new_path)

    shutil.move(folder, new_path)


root = Path("..")

python_folder = root / "python"
csv_folder = root / "csv"
tests_folder = root / "tests"

python_folder.mkdir(exist_ok=True)
csv_folder.mkdir(exist_ok=True)
tests_folder.mkdir(exist_ok=True)


for file in root.iterdir():

    if file.is_file():

        if file.suffix == ".py":
            if file.name != "project_organizer.py":
                new_path = python_folder / file.name
                print(file, "->", new_path)
                shutil.move(file, new_path)

        elif file.suffix == ".csv":
            new_path = csv_folder / file.name
            print(file, "->", new_path)
            shutil.move(file, new_path)


for folder in root.iterdir():

    if folder.is_dir():

        if folder.name.endswith("_test"):

            new_path = tests_folder / folder.name
            print(folder, "->", new_path)

            shutil.move(folder, new_path)


def main():
    root = Path("..")

    for item in root.iterdir():
        if item.is_file():
            organize_file(item, root)

        elif item.is_dir():
            organize_folder(item, root)


if __name__ == "__main__":
    main()
