import csv
from pathlib import Path

file_path = input("CSVファイルのパスを入力してください: ").strip()
file = Path(file_path)

if not file.exists():
    print("指定したファイルが存在しません。")
    exit()

if not file.is_file():
    print("ファイルではありません。")
    exit()

with open(file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"利用可能な列: {', '.join(reader.fieldnames)}")

columns_input = input("残したい列をカンマ区切りで入力してください: ").strip()
selected_columns = [column.strip() for column in columns_input.split(",")]

for column in selected_columns:
    if column not in reader.fieldnames:
        print(f"指定した列が存在しません: {column}")
        exit()

selected_rows = []

for row in rows:
    selected_row = {}

    for column in selected_columns:
        selected_row[column] = row[column]

    selected_rows.append(selected_row)

output_file = Path("selected_columns.csv")

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=selected_columns)

    writer.writeheader()
    writer.writerows(selected_rows)

print(f"保存しました: {output_file}")
