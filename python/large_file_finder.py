from pathlib import Path

folder_path = input("検索するフォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

try:
    min_size_kb = float(input("最小サイズ(KB)を入力してください: "))
except ValueError:
    print("サイズは数値で入力してください。")
    exit()

if min_size_kb <= 0:
    print("サイズは0より大きい数値を入力してください。")
    exit()

files = []

for item in folder.iterdir():
    if not item.is_file():
        continue

    size = item.stat().st_size
    size_kb = size / 1024

    if size_kb >= min_size_kb:
        files.append((item.name, size_kb))

files.sort(key=lambda x: x[1], reverse=True)

if not files:
    print("条件に一致するファイルはありません。")
else:
    for name, size_kb in files:
        print(f"{name}: {size_kb:.2f} KB")
