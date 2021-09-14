import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

df = pd.read_csv('uriage.csv', encoding='utf-8')

ws['A1'] = df['当期売上'].sum()

wb.save('売上高xlsx')
