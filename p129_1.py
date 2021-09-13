#フォルダを指定して保存
import os
import sys
import p122 as mylib #mylibという名前でp122.pyをインポート
path=os.getcwd() #現在の作業フォルダ位置を取得
#元データと出力データのパスとファイル名を指定
excelFile=os.path.join(path,"元データ","売上リスト(pg22_01用).xlsx")
pdfFile=os.path.join(path,"出力データ","売上リストPDF.pdf")
mylib.excelToPdf(excelFile,pdfFile) 