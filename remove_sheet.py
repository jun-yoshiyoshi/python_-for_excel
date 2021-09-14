#作業用シートの一括削除

from openpyxl import load_workbook

wb = load_workbook("チェックリスト.xlsx")

for ws in wb.worksheets:
    if ws.title.startswith("作業用_"):
        wb.remove(ws)

wb.save("チェックリスト_変更後.xlsx")
