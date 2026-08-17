from pathlib import Path
from PIL import Image

folder_path = input("画像フォルダを入力してください: ").strip()
folder = Path(folder_path)

if not folder.exists():
    print("指定したフォルダが存在しません。")
    exit()

if not folder.is_dir():
    print("フォルダではありません。")
    exit()

suffixes = {".png", ".jpg", ".jpeg", ".webp"}

for item in folder.iterdir():

    if not item.is_file():
        continue

    if item.suffix.lower() not in suffixes:
        continue

    with Image.open(item) as img:
        width, height = img.size
        new_width = 300
        new_height = int(height * new_width / width)
        resized = img.resize((new_width, new_height))
        output_path = folder / f"resized_{item.name}"
        resized.save(output_path)
        print(f"保存しました: {output_path.name}")
