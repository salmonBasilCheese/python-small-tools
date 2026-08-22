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

scores_by_department = {}

for row in rows:
    department = row["Department"]

    try:
        score = float(row["Score"])
    except (ValueError, TypeError):
        continue

    if department not in scores_by_department:
        scores_by_department[department] = []

    scores_by_department[department].append(score)

print("\n===== 部署別平均 =====")

for department, scores in scores_by_department.items():
    average = sum(scores) / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print(f"{department}")
    print(f"  平均: {average:.2f}")
    print(f"  最大: {maximum:.2f}")
    print(f"  最小: {minimum:.2f}")

output_file = Path("department_statistics.csv")

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Department", "Average", "Maximum", "Minimum"])

    for department, scores in scores_by_department.items():
        average = sum(scores) / len(scores)
        maximum = max(scores)
        minimum = min(scores)

        writer.writerow(
            [
                department,
                f"{average:.2f}",
                f"{maximum:.2f}",
                f"{minimum:.2f}",
            ]
        )

print(f"保存しました: {output_file}")
