#ケーキ店の売り上げのデータと気温を学習させる
import datetime
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def readTempData(fileName):#気象データを読み込み
    df = pd.read_csv(fileName,encoding="Shift_JIS",skiprows=6)
    df.columns = ["日付","気温","品質情報","均質番号"]
    df['日付'] = pd.to_datetime(df['日付'])#曜日の列を追加　月曜日=0 日曜日=6
    df["曜日"] = df["日付"].dt.dayofweek
    df["月"] = df["日付"].dt.month
    df["日"] = df["日付"].dt.day
    return df
def readSalesData(fileName):#売上データを読み込み
    df = pd.read_excel(fileName)
    df['日付'] = pd.to_datetime(df['日付'])
    return df

#気象データを読み込み
dfTemp = readTempData("気象データ2017.csv")
#売上データを読み込み
dfShop = readSalesData("洋菓子店売上リスト2017.xlsx") #気象データと売上データを統合
df = dfTemp.copy()
df = df.merge(dfShop,how="inner",on="日付")
x = df[["月","日","曜日","気温"]] #与えるデータ
y = df["売上金額"] #求めるデータ
print(x)
print(y)
#重回帰分析
model = LinearRegression()
model.fit(x,y) #訓練の開始 
print(model.coef_) #回帰変数 
print(model.intercept_) #切片 
print(model.predict(x)) #予測値の表示
print(model.score(x,y)) #相関の表示