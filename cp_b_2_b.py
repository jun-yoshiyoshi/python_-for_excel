# 異なるブックへの自動入力
import openpyxl
# エクセルのブックを操作するライブラリの読み込み


def copy_paste_b2b(Cbook, Pbook, Csheet="Sheet1", Psheet="Sheet1"):
    workBook1 = openpyxl.load_workbook(Cbook)
    workSheet1 = workBook1[Csheet]
    workBook2 = openpyxl.load_workbook(Pbook)
    workSheet2 = workBook2[Psheet]
    workSheet2["A2"] = workSheet1["A1"].value
    workBook2.save(f"確認前+{Pbook}")


copy_paste_b2b("新商品リスト.xlsx", "商品リスト.xlsx")
