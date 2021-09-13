#複数シートの情報を1つのシートにまとめる
import pandas as pd#pandasをインポート
#指定するbookの全てのシートを読み込む
df=pd.read_excel("店舗別売上リスト.xlsx",sheet_name=None)
dataList=[]#集計表へ書き出すデータを保存するリスト
sheetsList=list(df.keys())
for sheet in df:#シートループ
	for index,rows in df[sheet].iterrows():#行ループ
		work=[]#作業用リスト
		for row in rows:#列ループ
			work.append(row)
		dataList.append(work)
columns=list(df[sheetsList[0]].columns)#列名をリストで取得
df["統合表"]=pd.DataFrame(dataList,columns=columns)#集計表に全店舗の売り上げデータを追加
with pd.ExcelWriter("店舗別売上リスト.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD',engine="openpyxl",mode = "a") as writer:
	df["統合表"].to_excel(writer,sheet_name="統合表",index=False)
