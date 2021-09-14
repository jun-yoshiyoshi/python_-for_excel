#ログの出力、書式
#参照１ https://qiita.com/knknkn1162/items/87b1153c212b27bd52b4
#参照２　https://docs.python.org/ja/3/library/logging.html

import logging
import sys

from openpyxl import Workbook

logging.basicConfig(filename='create_book.log',
                    lebel=logging.INFO,
                    format='%(asctime)s : [%(levelname)s]　%(message)s')
#level引数でINFOを指定することで、INFO以上のログのみ出力させることができる

logging.info('処理を開始しました')

try:
    count = sys.argv[1]
    for i in range(int(count)):
        wb = Workbook()
        ws = wb.active
        ws.title = '概要'

        file_name = f'資料_{i+1}.xlsx'
        wb.save(file_name)
        logging.info("ブックを作成しました:%s", file_name)
    #ユーザーの入力数だけブックが作成される。

except Exception:
    logging.exception('例外が発生しました')

logging.info('処理が終了しました')