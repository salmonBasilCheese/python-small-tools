from pathlib import Path

folder_path = input("調べるフォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

file_count = 0
folder_count = 0
total_size = 0
files = []
extension_counts = {}

for item in folder.iterdir():
    if item.is_file():
        file_count += 1

        size = item.stat().st_size
        total_size += size

        files.append((item.name, size))

        extension = item.suffix.lower()

        if extension == "":
            extension = "[拡張子なし]"

        extension_counts[extension] = extension_counts.get(extension, 0) + 1

    elif item.is_dir():
        folder_count += 1

print("\n===== フォルダレポート =====")

print(f"ファイル数: {file_count}")
print(f"フォルダ数: {folder_count}")
print(f"合計サイズ: {total_size / 1024:.2f} KB")

if files:
    largest_file = max(files, key=lambda x: x[1])
    smallest_file = min(files, key=lambda x: x[1])

    print(f"最大ファイル: {largest_file[0]} " f"({largest_file[1] / 1024:.2f} KB)")
    print(f"最小ファイル: {smallest_file[0]} " f"({smallest_file[1] / 1024:.2f} KB)")

else:
    print("ファイルがありません。")

print("\n===== 拡張子別ファイル数 =====")

for extension, count in extension_counts.items():
    print(f"{extension}: {count}")
