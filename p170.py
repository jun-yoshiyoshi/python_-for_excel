import os
import glob
from smb.SMBConnection import SMBconnection
path=os.getcwd()#現在の作業フォルダ位置を取得
sendFileFolder=os.path.join(path,"送信データ")
recieveFileFolder=os.path.join(path,"送信データ")
reciveFileFolder=os.path.join(path,"送信データ")
user=""#サーバー接続ユーザー名
password=""#サーバー接続パスワード
ipAdress="192.168.130.100"#サーバーIPアドレス(例)
serverFolder="test"#サーバーフォルダ(例)
connection=SMBConnection(user,password,"myClient","HostServer")
connection.connect(ipAdress,139)
#送信データフォルダの情報を削除
os.chdir(sendFileFolder)#受信データフォルダに移動
for reciveFile in connection.listPath(serverFolder,'/'):
	if reciveFile.filename=="." or reciveFile.filename=="..":
		connection.deleteFile(serverFolder,reciveFile,filename)
connection.close()
