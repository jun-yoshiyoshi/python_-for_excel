import pandas as pd

df = pd.read_csv('uriage.csv', encoding='utf-8')

for index, row in df.iterrows():
    print(f'{index+1}行目:{row["当期売上"]}')
