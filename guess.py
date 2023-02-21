import random
x = random.randint(1, 100)

while True:
	y = input('請輸入1~100任意數: ')
	y = int(y)
	if y == x:
		print('終於猜對了!')
		break
	elif y > x:
		print('比答案大')
	elif y < x:
		print('比答案小')