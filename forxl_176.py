# 大量の画像を１つのブックにまとめる
from pathlib import Path
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active
ws.column_dimensions['C'].width = 30

path = Path('./image')
for i, file in enumerate(path.glob('*.jpg')):
    row_no = i + 3
    ws.row_dimensions[row_no].height = 130

    image = Image(file)
    image.width = 100
    image.height = 140

    ws.add_image(image, f'C{row_no}')
wb.save('一覧.xlsx')
