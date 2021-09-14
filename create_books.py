#複数のブックを連番で作成する

from openpyxl import Workbook

count = input("作成するブック数:")
for i in range(int(count)):
    wb = Workbook()
    ws = wb.active
    ws.title = '概要'
    wb.save(f"資料_{i+1}.xlsx")