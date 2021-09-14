# ウインドウ枠（行）の固定

from openpyxl import load_workbook

wb = load_workbook("作業時間.xlsx")
ws = wb.active

ws.freeze_panes = "A4"
# Ａ列のセル番地を指定すると、直前の行までが固定される。
# "A4"の場合は３行目までが常に表示される。

wb.save("作業時間_変更後.xlsx")
