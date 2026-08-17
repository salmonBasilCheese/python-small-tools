from pathlib import Path

folder_path = input("検索するフォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

search_word = input("検索する文字列を入力してください: ").strip()

found = False

for item in folder.iterdir():
    if not item.is_file():
        continue

    if item.suffix != ".txt":
        continue

    with open(item, "r", encoding="utf-8") as file:
        text = file.read()

        if search_word in text:
            print(item.name)
            found = True

if not found:
    print("該当するファイルはありません。")
