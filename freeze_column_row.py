#ウインドウ枠（行と列）の固定

from openpyxl import load_workbook

wb = load_workbook("作業時間.xlsx")
ws = wb.active

ws.freeze_panes = "E4"
# A列以外の列で2行目以降のセル番地を指定すると、指定列の前列と前の行までを固定する

wb.save("作業時間_変更後.xlsx")
