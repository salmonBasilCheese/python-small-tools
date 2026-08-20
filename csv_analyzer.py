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
    columns = reader.fieldnames
    rows = list(reader)

print("\n===== CSV分析 =====")
print(f"行数: {len(rows)}")
print(f"列数: {len(columns)}")
print(f"列名: {', '.join(columns)}")

numeric_columns = {}

for column in columns:
    values = []

    for row in rows:
        try:
            value = float(row[column])
            values.append(value)
        except (ValueError, TypeError):
            pass

    if values:
        numeric_columns[column] = values

print("\n===== 数値列の分析 =====")

for column, values in numeric_columns.items():
    average = sum(values) / len(values)
    maximum = max(values)
    minimum = min(values)

    print(column)
    print(f"  平均: {average:.2f}")
    print(f"  最大: {maximum:.2f}")
    print(f"  最小: {minimum:.2f}")
