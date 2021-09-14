# ブック作成者・最終更新者

from openpyxl import load_workbook

wb = load_workbook("資料.xlsx")

name = "鈴木"
properties = wb.properties
properties.creator = nameproperties.lastModifiedBy = name

wb.save("資料_変更.xlsx")
