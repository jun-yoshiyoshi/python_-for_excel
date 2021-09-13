# 異なるブックへの自動入力

import openpyxl
# エクセルのブックを操作するライブラリの読み込み

workBook1 = openpyxl.load_workbook("新商品リスト.xlsx")
# エクセルブックを開く
workSheet1 = workBook1["Sheet1"]
# 指定シートを取得する

try:
    workBook2 = openpyxl.load_workbook("商品リスト.xlsx")
    workSheet2 = workBook2["Sheet1"]
    workSheet2["A10"] = workSheet1["A1"].value
    # セルA10にセルA1の値をコピペ
    workBook2.save("商品リスト.xlsx")

except FileNotFoundError:
    print("出力用ブックがありません")
