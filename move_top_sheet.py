#特定の名前のシートを移動する（シートを先頭へ移動）

from openpyxl import load_workbook

wb = load_workbook("チェックリスト.xlsx")
#対象ファイルの選択

for ws in wb.worksheets:
    ws.sheet_view.tabSelected = None
#default選択のシートをオフにする。オフにしなければアクティブなシートはまとめシートとグループ化される。

ws_matome = wb["まとめ"]
#シートの現在地を基準とした移動しかできないので、"まとめ"シートを変数にする

wb.move_sheet(ws_matome, offset=-wb.index(ws_matome))

wb.active = 0
#先頭のシートを選択

wb.save("チェックリスト_変更後.xlsx")
