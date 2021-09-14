# 行・列のグループ化による表示最適化
from openpyxl import load_workbook

wb = load_workbook("作業時間.xlsx")
ws = wb.active
for row_no in [(5, 20), (22, 27), (29, 30)]:
    ws.row_dimensions.group(*row_no, outline_level=1, hidden=True)
    #行のグループ化。折りたたまない場合はhidden=False

ws.column_dimensions.group("D", outline_level=1, hidden=True)
#列のグループ化。折りたたまない場合はhidden=False
wb.save("作業時間_変更後.xlsx")