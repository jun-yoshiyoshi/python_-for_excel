#印刷設定を変更する
import openpyxl#openpyxlをインポート
workBook=openpyxl.load_workbook("売上リスト.xlsx")#エクセルブックを開く
sheet=workBook.active#アクティブなワークシートを選択
sheet.print_options.horizontalCentered=False#水平(横)位置で中央にしない
sheet.print_options.verticalCentered=False#垂直(縦)位置で中央にしない
sheet.print_title_rows="1:1"#1行目を行見出しとして設定
sheet.page_setup.orientation="portrait"#横は"landscape"
sheet.page_setup.fitToWeidth=1#横1ページ
sheet.page_setup.fitToHeidth=0#縦は指定なし
sheet.oddFooter.center.text="&[Page]/&Nページ"#現在のページ、総ページをフッターに設定
workBook.save('売上リスト(完成)1.xlsx')#ファイル名を指定して保存
