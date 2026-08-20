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

scores = []

for row in rows:
    try:
        score = float(row["Score"])
        scores.append(score)
    except (ValueError, TypeError):
        pass

if not scores:
    print("有効なScoreデータがありません。")
    exit()

count = len(scores)
total = sum(scores)
average = total / count
maximum = max(scores)
minimum = min(scores)

output_file = Path("summary.csv")

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Metric", "Value"])

    writer.writerow(["Count", count])
    writer.writerow(["Average", f"{average:.2f}"])
    writer.writerow(["Maximum", f"{maximum:.2f}"])
    writer.writerow(["Minimum", f"{minimum:.2f}"])
    writer.writerow(["Total", f"{total:.2f}"])

print(f"保存しました: {output_file}")
