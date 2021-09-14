# セルと表の移動

from openpyxl import load_workbook

wb = load_workbook("テーブル定義書.xlsx")
ws = wb.active

ws.move_range("A3:F7", rows=2, colus=1, translate=False)

# デフォルト（False）では,数式更新は行われない。
# ws.mobe_range("A6",rows=2,cols=1.translate=True)のとき数式更新される。

wb.save("テーブル定義書_変更後.xlsx")