<<<<<<< HEAD
import csv
from pathlib import Path

# ==========================================
# CSVを名前順に並べ替えるプログラム
# Python 3.13 対応
# ==========================================

# CSVファイルのパスを入力
csv_path = input("CSVファイルのパスを入力してください: ").strip()

file_path = Path(csv_path)

# ファイルの存在確認
if not file_path.exists():
    print("ファイルが存在しません。")
    exit()

# CSVを読み込む
with open(file_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # 全行をリストにする
    rows = list(reader)

# データが空なら終了
if len(rows) == 0:
    print("CSVが空です。")
    exit()

# ヘッダーとデータを分ける
header = rows[0]
data = rows[1:]

# Name列（2列目）で並べ替え
data = sorted(data, key=lambda row: row[1])

# 保存先
output_file = file_path.with_name("sorted_output.csv")

# CSVを書き込む
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerows(data)

print(f"保存しました: {output_file}")
=======
import csv
from pathlib import Path

# ==========================================
# CSVを名前順に並べ替えるプログラム
# Python 3.13 対応
# ==========================================

# CSVファイルのパスを入力
csv_path = input("CSVファイルのパスを入力してください: ").strip()

file_path = Path(csv_path)

# ファイルの存在確認
if not file_path.exists():
    print("ファイルが存在しません。")
    exit()

# CSVを読み込む
with open(file_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # 全行をリストにする
    rows = list(reader)

# データが空なら終了
if len(rows) == 0:
    print("CSVが空です。")
    exit()

# ヘッダーとデータを分ける
header = rows[0]
data = rows[1:]

# Name列（2列目）で並べ替え
data = sorted(data, key=lambda row: row[1])

# 保存先
output_file = file_path.with_name("sorted_output.csv")

# CSVを書き込む
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerows(data)

print(f"保存しました: {output_file}")
>>>>>>> 2e6bc5a (Add Python utility tools)
