import os
import sys
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#メールを送信
def create_message(toAdress,subject,message):
	host="smtp.gmail.com"#送信メールサーバー
	port=465#ポート番号
	fromAdress='adsolutionpartners@gmail.com'#自分のメールアドレス
	password='rwtvcevhgpzfnwpb'#パスワード
	mimeMultiPart=MIMEMultipart()#添付ファイルが送れるメール
	mimeMultiPart['Subject']=subject#件名
	mimeMultiPart['From']=fromAdress#差出人
	mimeMultiPart['To']=toAdress#宛先
	mimeText=MIMEText(message)#メッセージ本文
	mimeMultiPart.attach(mimeText) #本文を追加
	path=os.getcwd()#現在の作業フォルダ位置を取得
	sendFile=os.path.join(path,"出力データ","佐藤　美和様領収書.pdf")
	try:
		attachFile={'name':'佐藤　美和様領収書.pdf','path':sendFile}#送信ファイルを指定
		attachMent=MIMEBase("application",'pdf')
		file=open(attachFile['path'],'rb+')
		attachMent.set_payload(file.read())
		file.close()
	except FileNotFoundError:
		print("添付するファイルが見つかりません")
		sys.exit()
	encoders.encode_base64(attachMent)
	attachMent.add_header("Content-Disposition","attachMent",filename=attachFile['name'])
	mimeMultiPart.attach(attachMent)
	smtpSession=smtplib.SMTP_SSL(host,port)#接続の作成
	smtpSession.login(fromAdress,password)#サーバーにログイン
	smtpSession.send_message(mimeMultiPart)#メッセージの送信
	smtpSession.close()#接続のクローズ＊必ずクローズしてください。
#関数の呼び出し改行は\n
toAdress='adsolutionpartners@gmail.com'#送信先メールアドレス
subject='領収書の件'
message='お世話になります。領収書を送付いたします。\nどうぞ、よろしくお願いいたします。'
create_message(toAdress,subject,message)
