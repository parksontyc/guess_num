#產生一個隨機整數
#讓使用都重複輸入數字去猜
#猜對的話，印出終於答對了
#猜錯的話，要告訴使用者，比答案大\小
import random

answer = random.randint(1, 100)

while True:
	user_ans = input('請輸入數字：')
	user_ans = int(user_ans)
	if user_ans == answer:
		print('猜對了！')
		break
	else:
		a = user_ans - answer
		if a > 0:
			print('小於', user_ans)
		else:
			print('大於', user_ans)