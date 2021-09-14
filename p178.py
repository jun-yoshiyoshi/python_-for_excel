#googleドライブからファイルを取得する
from urlib.parase import urlparse
import urllib.request
import request
import requests
#Googleドライブのファイル共有URL
url=""
path=urlparse(url).path
path=path.lstrip("/file/d/")
path=path.rstrip("/view")
url=workUrl.replace("<file_id>",path)
response=requests.get(url)
file_name="店別売上表.xlsx"
with open(file_name,'wb')as sf:
	sf.write(response.content)