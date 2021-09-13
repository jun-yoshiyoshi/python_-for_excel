# 異なるシートへの自動入力

import openpyxl
# エクセルのブックを操作するライブラリの読み込み

workBook = openpyxl.load_workbook("商品リスト.xlsx")
# エクセルブックを開く
workSheet = workBook["Sheet1"]
# 指定シートを取得する

workSheet["A10"] = workSheet["A1"].value
# セルA10にセルA1の値をコピペ

workBook.save("商品リスト.xlsx")
