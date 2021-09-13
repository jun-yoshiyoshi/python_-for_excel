#売上表から担当者別の売上シートを作成する
import pandas as pd #pandasをインポート
#指定したブックのすべてのシートを読み込み
df=pd.read_excel("社員別売上一覧.xlsx",sheet_name="売上一覧")
staffDictionary={} #社員と売上を保存する辞書
for index,rows in df.iterrows(): #行ループ
    if rows["担当者名"] not in staffDictionary:     #辞書に担当者がない場合
        staffDictionary[rows["担当者名"]] = []
    staffDictionary[rows["担当者名"]].append([rows["日付"],rows["売上金額"]]) #日付と売上を追加
#新しいエクセルブックに書き出し
with pd.ExcelWriter("社員別売上一覧.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD',mode="a") as writer:
    for staff in staffDictionary: #担当者ループ
        df2 = pd.DataFrame(list(staffDictionary[staff]),columns=["日付","売上金額"])#集計表に店舗別の売上データを追加
        df2.to_excel(writer, sheet_name=staff,index=False) #シートを書き出し