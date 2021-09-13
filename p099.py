#列の幅と行の高さを変更する
import openpyxl#openpyxlをインポート
workBook=openpyxl.load_workbook
("新宿店売上リスト.xlsx")#エクセルブックを開く
sheet=workBook.active#アクティブなワークシートを選択
sheet.column_demensions["A"].weidth=12#列の幅を設定(文字数)
workBook.save('新宿店売上リスト(完成).xlsx')
#ファイル名を指定して保存
