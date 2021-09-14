# ブックの末尾に連番を追加する
from pathlib import Path

path = Path('./books')
for i, file in enumerate(path.glob('*.xlsx')):
    file.rename(path/f'{file.stem}_{i+1:04d}.xlsx')
