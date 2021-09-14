# アクティブセル、表示倍率を調整
from openpyxl import load_workbook

cell_no = "A1"

zoom_scale = 100

wb = load_workbook("チェックリスト.xlsx")

for ws in wb.worksheets:
    sv = ws.sheet_view
    sv.selection[0].activeCell = cell_no
    sv.selection[0].sqref = cell_no
    sv.selection[0].activeCellId = None
    sv.zoomScale = zoom_scale

wb.save("チェックリスト_変更後.xlsx")
