import os
import glob
from smb.SMBConnection import SMBConnection
path=os.getcwd()#現在の作業フォルダ位置を取得
sendFileFolder=os.path.join(path,"送信データ")
reciveFileFolder=os.path.join(path,"受信データ")
user="例"#サーバー接続ユーザー名(例)
password="例"#サーバー接続パスワード（例）
ipAdress="例"#サーバーIPアドレス（例）
serverFolder="例"#サーバーフォルダ（例）
connection=SMBConection(user,password,"myClient","HostServer")
connection.connect(ipAdress,139)
#サーバーにデータを送信
os.chdir(sendFileFolder)#送信データフォルダに移動
for sendFile in glob.glob("*.xlsx"):
	with open(sendFile,"rb")as file:
		connection.storeFile(serberFolder,sendFile,file)
#サーバーのデータを受信
os.chdir(reciveFileFolder)#受信データフォルダに移動
for reciveFile in connection.listPath(serverFolder,'/'):
	if reciveFile.filename=="."or reciveFile.filename=="..":
		continue#不要な要素を読み飛ばす
	with open(reciveFile.filename,'wb')as file:
		connection.retrieveFile(sereverFolder,reciveFile.filename,file)
connection.close()