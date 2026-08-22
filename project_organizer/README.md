# project_organizer

`python-small-tools` のルートフォルダにあるファイルやフォルダを、種類ごとに整理するプログラムです。

## 整理ルール

| 対象 | 移動先 |
|---|---|
| `.py` ファイル | `python/` |
| `.csv` ファイル | `csv/` |
| `_test` で終わるフォルダ | `tests/` |
| その他 | 移動しない |

## 実行方法

`project_organizer` フォルダから実行します。

```powershell
python .\project_organizer.py