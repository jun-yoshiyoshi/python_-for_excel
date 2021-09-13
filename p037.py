#反復
#1から10までを足し算します。
goukei=0
for i in range(1,11):#iの値を1から11まで増やして11になったらループを抜ける。
	goukei=goukei+i#goukeiの値にiを加算する
print("合計は"+str(goukei)+"です")#goukeiを文字列に変換して表示。
#1から10までを表示します
count=1
while count<=10:#countの値が10以下の間次の行を繰り返す。
	print(count)
	count=count+1