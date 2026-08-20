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

minimum_score = input("Scoreの最低値を入力してください: ").strip()

try:
    minimum_score = float(minimum_score)
except ValueError:
    print("最低値には数値を入力してください。")
    exit()

with open(file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

filtered_rows = []

for row in rows:
    try:
        score = float(row["Score"])

        if score >= minimum_score:
            filtered_rows.append(row)

    except (ValueError, TypeError):
        pass

output_file = Path("filtered_scores.csv")

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)

    writer.writeheader()
    writer.writerows(filtered_rows)

print(f"保存しました: {output_file}")
