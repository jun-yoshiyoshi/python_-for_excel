# 異なるシートのセルへの自動入力

import openpyxl
# エクセルのブックを操作するライブラリの読み込み

workBook = openpyxl.load_workbook("商品リスト.xlsx")
# エクセルブックを開く
workSheet1 = workBook["Sheet1"]
# 指定シートを取得する

try:
    workSheet2 = workBook["Sheet2"]

    workSheet2["A10"] = workSheet1["A1"].value
    # セルA10にセルA1の値をコピペ

    workBook.save("商品リスト変更後.xlsx")

except FileNotFoundError:
    print("出力用のシートがありません")
