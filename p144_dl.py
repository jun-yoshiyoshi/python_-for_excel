#Excel のデータを Word に書き出す
import os
import sys
import pandas as pd #pandasをインポート 
from docx import Document
#ファイルを開く
path = os.getcwd()#現在の作業フォルダ位置を取得
try:
    df = pd.read_excel("領収書（原本）.xlsx")
except FileNotFoundError:
    print("Wファイルが見つかりません")
    sys.exit()
columns = list(df.columns) #列名を取得
for index,item in df.iterrows(): #行ループ
    try:
        document = Document("領収書原本.docx")
    except FileNotFoundError: 
        print("ファイルが見つかりません")
        sys.exit()
    for par in document.paragraphs: #段落ループ 
        for column in columns: #列ループ
            if str(column) in par.text: #段落に置換対象が含まれているかどうか判定
                if str(column) == "$日付": #日付の場合はyyyy年m月d日にする
                    item[column] = str(item[column]. year)+"年"+str(item[column].month)+"月"+str(item[column].day)+"日"
                if str(column) == "$金額":#日付の場合はyyyy 年m月d日にする
                    item[column] = "¥{:,d}".format(item[column]) 
                par.text = par.text.replace(str(column),str (item[column]))
    outFile = os.path.join(path,"出力データ",item["$お名前"]+"様領収書.docx")
    try:
        document.save(outFile) #Wordのファイルに書き出し 
    except FileNotFoundError:
        print("保存先のフォルダがありません")
        sys.exit()