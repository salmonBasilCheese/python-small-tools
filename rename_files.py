from pathlib import Path

# ==========================================
# ファイル名の先頭に "new_" を付けるプログラム
# Python 3.13 対応
# ==========================================

# 変更したいフォルダのパスを入力してください
folder_path = input("フォルダのパスを入力してください: ").strip()

folder = Path(folder_path)

# フォルダが存在するか確認
if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

# フォルダ内のファイルを順番に処理
for item in folder.iterdir():

    # サブフォルダは無視する
    if not item.is_file():
        continue

    # 新しいファイル名
    new_name = "new_" + item.name
    new_path = item.with_name(new_name)

    # 同じ名前のファイルが存在する場合は変更しない
    if new_path.exists():
        print(f"スキップ: {new_name} は既に存在します。")
        continue

    # 名前変更
    item.rename(new_path)
    print(f"{item.name} → {new_name}")

print("完了しました。")
