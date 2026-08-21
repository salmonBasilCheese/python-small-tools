# File Organizer

フォルダ内のファイルを拡張子ごとに自動分類するPythonツール。

## 対応しているファイル

- JPG / JPEG / PNG → images
- PDF → pdf
- CSV → csv
- TXT → text

## 動作

- 分類先フォルダがなければ自動作成
- 対応していない拡張子は移動しない
- フォルダは処理しない
- 移動先に同名ファイルがある場合は上書きしない

## 実行方法

```powershell
python file_organizer.py