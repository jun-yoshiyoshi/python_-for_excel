# 表をテーブルに設定する

from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

wb = load_workbook("売上実績.xlsx")
ws = wb.active

table = Table(displayName="Table1", ref="B2:F12")
# テーブルを生成.displayNameはブック内で重複させることはできない。
table_style = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
# nemeには"TableStyleLight9","TableStyleDark9"などもある。

table.tableStyleInfo = table_style
#Ｔable.tableＳtyleＩnfo属性に作成したオブジェクトを代入。
ws.add_table(table)
#新しいワークシートにテーブルを追加。
wb.save("売上実績テーブル.xlsx")