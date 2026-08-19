from pathlib import Path

folder_path = input("調べるフォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

files = []

for item in folder.iterdir():
    if not item.is_file():
        continue

    size = item.stat().st_size
    files.append((item.name, size))

order = input("並び順を選んでください（1: 大きい順 / 2: 小さい順）: ")

if order == "1":
    reverse = True
elif order == "2":
    reverse = False
else:
    print("1または2を入力してください。")
    exit()

files.sort(key=lambda x: x[1], reverse=reverse)

for name, size in files:
    print(f"{name}: {size / 1024:.2f} KB")
