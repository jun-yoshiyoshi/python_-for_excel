#ウインドウ枠（列）の固定

from openpyxl import load_workbook

wb = load_workbook("作業時間.xlsx")
ws = wb.active

ws.freeze_panes = "E1"
# A列以外の列で１行目のセル番地を指定すると、指定列の前列までを固定する

wb.save("作業時間_変更後.xlsx")
