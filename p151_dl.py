#データを元に棒グラフを作成をする
import openpyxl
from openpyxl.chart import BarChart, Reference,Series
workBook = openpyxl.load_workbook("日別店舗別クロス集計表.xlsx") #エクセルブックを開く
sheet = workBook.active#アクティブなワークシートを選択
#グラフの描画対象になるセル範囲を設定
values = Reference(sheet, min_col=2, min_row=1,max_col=4, max_row=32)
chart = BarChart() #棒グラフを作成
#先頭行をグラフのラベルにしてデータを追加
chart.add_data(values,titles_from_data=True) 
sheet.add_chart(chart, "G1") #セルG1にグラフを描画
workBook.save("日別店舗別クロス集計表(グラフ).xlsx") #ファイルの保存