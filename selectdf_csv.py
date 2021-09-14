import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

wb = Workbook()
ws = wb.active

df = pd.read_csv('uriage.csv', encoding='utf-8')

select_df = df[(df['当期売上'] >= 100) & (df['部門'].isin(['ファブリック', 'キャラクター']))]
# DataFrame.isinメソッド（>=,&,isin）で複数の条件に一致するデータを取得

for row in dataframe_to_rows(select_df, index=None, header=True):
    ws.append(row)

wb.save('売上高.xlsx')
