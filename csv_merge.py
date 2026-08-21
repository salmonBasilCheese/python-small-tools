import csv
from pathlib import Path

file_path_a = input("1つ目のCSVファイルのパスを入力してください: ").strip()
file_path_b = input("2つ目のCSVファイルのパスを入力してください: ").strip()

file_a = Path(file_path_a)
file_b = Path(file_path_b)

if not file_a.exists():
    print("1つ目のファイルが存在しません。")
    exit()

if not file_a.is_file():
    print("1つ目はファイルではありません。")
    exit()

if not file_b.exists():
    print("2つ目のファイルが存在しません。")
    exit()

if not file_b.is_file():
    print("2つ目はファイルではありません。")
    exit()

with open(file_a, "r", encoding="utf-8", newline="") as f:
    reader_a = csv.DictReader(f)
    rows_a = list(reader_a)

with open(file_b, "r", encoding="utf-8", newline="") as f:
    reader_b = csv.DictReader(f)
    rows_b = list(reader_b)

rows = rows_a + rows_b

output_file = Path("merged.csv")

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader_a.fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print(f"保存しました: {output_file}")
