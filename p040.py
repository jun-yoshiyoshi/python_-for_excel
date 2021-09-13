import pandas as pd#エクセルのブックを操作するライブラリの読み込み
item_list=[]#エクセルに出力するデータを格納するリスト
item_no=input("商品番号を入力してください。-1を入力して終了。:")
while(int(item_no)!=-1):#商品番号に-1が入力されるまで次の3行を繰り返す。
	item_name=input("商品名を入力してください:")
	item_price=input("商品の価格を入力してください:")
	item_list.append([item_no,item_name,item_price])
#入力したデータをリスト形式で追加
	item_no=input("商品番号を入力してください。-1で終了。")
df=pd.DataFrame(item_list,columns=['商品番号','商品名','商品価格'])#列名
with pd.ExcelWriter("商品リスト.xlsx")as writer:
	df.to_excel(writer,index=False)
#エクセルファイルに書き出し
print("プログラム終了")