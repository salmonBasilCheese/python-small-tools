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


filtered_rows = []

with open(file, "r", encoding="utf-8", newline="") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        try:
            score = int(row["Score"])
        except ValueError:
            print(f"Scoreが数値ではないため除外しました: {row}")
            continue

        if score >= 70:
            filtered_rows.append(row)


output_file = Path("filtered_output.csv")

with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["Name", "Score"])

    writer.writeheader()
    writer.writerows(filtered_rows)
