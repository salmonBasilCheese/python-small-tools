import os
from pathlib import Path

# 1. 調査したい対象のフォルダパスを変数に設定する
folder_path = input("検索するフォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

# 2. 拡張子の種類と数を記録するための空の辞書を作る
extension_counts = {}

# 3. os.walk() を使って、対象フォルダ内のすべてのファイルをループで取得する
for root, dirs, files in os.walk(folder):
    for file in files:
        # 4. ファイル名から「拡張子」の部分だけを切り出す
        suffix = Path(file).suffix.lower()

        if not suffix:
            suffix = "(拡張子なし)"

        # 5. 辞書にその拡張子が存在しなければ追加し、カウントを+1する
        if suffix not in extension_counts:
            extension_counts[suffix] = 1
        else:
            extension_counts[suffix] += 1

# 6. ループ終了後、辞書の中身（結果）を画面にわかりやすく表示する
for suffix, count in extension_counts.items():
    print(f"{suffix}: {count}")
