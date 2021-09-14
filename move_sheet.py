#特定の名前のシートを移動する（シートを現在位置から１つ後ろに）

from openpyxl import load_workbook

wb = load_workbook("チェックリスト.xlsx")

wb.move_sheet("まとめ", offset=1)
#"まとめ"シートを現在位置から１つ後ろに移動

wb.save("チェックリスト_変更後.xlsx")
