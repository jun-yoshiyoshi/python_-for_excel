#売上リストから店舗別の売上を集計し、別のブックに出力
import pandas as pd#pandas #pandasをインポート
df=pd.read_excel("店舗別売上リスト.xlsx",sheet_name="統合表")
shopDictionary={}#店舗と売り上げを保存する辞書
total=0#全店舗の売り上げを保存する変数
for index,rows in df.iterrows():#行ループ
	if rows["店名"]not in shopDictionary:
		shopDictionary[rows["店名"]]=rows["売上金額"]
	else:
		shopDictionary[rows["店名"]]=shopDictionary[rows["店名"]] + rows["売上金額"]
	total=total+rows["売上金額"]
shopDictionary["全店合計"]=total#全店合計を辞書に格納
shopDictionary["売上平均"]=total/3#全店平均を辞書に格納
df2=pd.DataFrame(list(shopDictionary.items()),columns=["店名","売上合計"])#集計表に店舗別の売上データを追加
#新しいエクセルブックに書き出し
with pd.ExcelWriter("店舗別売上集計リスト.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD')as writer:
	df2.to_excel(writer,sheet_name="集計表",index=False)