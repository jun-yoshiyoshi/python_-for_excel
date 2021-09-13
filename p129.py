#フォルダを指定して保存
import os
import sys
import p122 as mylib #mylibという名前でp122.pyをインポート
path=os.getcwd() #現在の作業フォルダ位置を取得
#元データと出力データのパスとファイル名を指定
excelFilePath=os.path.join(path,"元データ")
files=os.listdir(excelFilePath) #ファイル一覧を取得
for f in files:
    if".xlsx"in f:#excelファイルの場合
        work=f.strip(".xlsx")#PDF用にファイル名だけ取り出す
        excelFile=os.path.join(excelFilePath,f) 
        pdfFile=os.path.join(path,"出力データ",work+".pdf")
        mylib.excelToPdf(excelFile,pdfFile)#Excel->PDF変換 