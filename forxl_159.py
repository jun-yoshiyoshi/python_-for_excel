# 印刷用調整
from openpyxl import load_workbook

print_area = "A1:D50"
print_title_cols = ""
# シートがページを跨いだときに、常に印刷する列。
print_title_rows = "1:5"
# シートがページを跨いだときに、常に印刷する行。
header_text = "&F"
# ブック名
footer_text = "&P/&Nページ"
# ページ番号/総ページ数
# https://docs.microsoft.com/ja-jp/office/vba/excel/concepts/workbooks-and-worksheets/formatting-and-vba-codes-for-headers-and-footers


wb = load_workbook("印刷調整前.xlsx")
for ws in wb.worksheets:
    ws.print_area = print_area
    # 印刷範囲
    ws.print_title_rows = print_title_rows
    # 常に印刷する行（タイトル行）
    ws.oddHeader.center.text = header_text
    # ヘッダー
    ws.oddFooter.center.text = footer_text
    # フッター
    wps = ws.page_setup
    wps.oroentation = ws.ORIENTATION_LANDSCAPE
    # ORIENTATION_LANDSCAPE（横方向印刷）ORIENTATION_PORTRAIT（縦方向印刷）
    wps.fitToWidth = 1
    # ページ数に合わせて印刷する設定（横）。自動は０．１ページなら１。
    wps.fitToheight = 0
    # ページ数に合わせて印刷する設定（縦）。自動は０．１ページなら１。
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    # fitTOWidthとfitToHeightを有効にする。
    wps.paperSize = ws.PAPERSIZE_A4
    #　用紙サイズ

wb.save("印刷調整済み.xlsx")
