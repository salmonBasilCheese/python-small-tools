from pathlib import Path
import hashlib

# ==========================================
# 重複ファイルを探すプログラム
# Python 3.13 対応
# ==========================================


def calculate_hash(file_path):
    """
    ファイルのSHA-256ハッシュ値を計算する
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


# フォルダの入力
folder_path = input("フォルダのパスを入力してください: ").strip()

folder = Path(folder_path)

# フォルダの確認
if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()


# ハッシュ値を保存する辞書
hash_dict = {}

# フォルダ内のファイルだけ調べる
for item in folder.iterdir():

    if not item.is_file():
        continue

    file_hash = calculate_hash(item)

    if file_hash not in hash_dict:
        hash_dict[file_hash] = [item.name]
    else:
        hash_dict[file_hash].append(item.name)


print("\n===== 重複ファイル =====")

duplicate_found = False

for files in hash_dict.values():
    if len(files) > 1:
        duplicate_found = True
        print()
        for name in files:
            print(name)

if not duplicate_found:
    print("重複ファイルは見つかりませんでした。")
