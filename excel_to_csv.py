import pandas as pd
from openpyxl import load_workbook

wb = load_workbook('売上実績.xlsx', read_only=True)
ws = wb.active

df = pd.DataFrame(ws.values)
df.to_csv('uriage_jisseki.csv', header=False, index=False, encoding='utf-8')
