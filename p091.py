#クロス集計表を作成
import pandas as pd#pandasをインポート
df=pd.read_excel("店舗別売上リスト2.xlsx",sheet_name="Sheet1")#ブックを読み込み
df=pd.crosstab(df['日付'],df['店名'],values=df['売上金額'],aggfunc="sum",margins=True,margins_name='合計')
#エクセルブックに書き出し
with pd.ExcelWriter("日別店舗別クロス集計表.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD')as writer:
	df.to_excel(writer,sheet_name="集計表")