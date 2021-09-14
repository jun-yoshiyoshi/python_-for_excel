import pandas as pd

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

wb = Workbook()
ws = wb.active
ws.column_dimensions['C'].width = 40

url = './sample_table.html'
dfs = pd.read_html(url, match='後期')
# '後期'を含むテーブルを読み込む

for df in dfs:
    for row in dataframe_to_rows(df, index=None, header=True):
        ws.append(row)

wb.save('ブックランキング.xlsx')
