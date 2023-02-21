import random
x = random.randint(1, 100)
n = 0
while True:
	n += 1 # n = n + 1
	y = input('請輸入1~100任意數: ')
	y = int(y)
	if y == x:
		print('終於猜對了!')
		print('這是你猜的第', n, '次')
		break
	elif y > x:
		print('比答案大')
	elif y < x:
		print('比答案小')
	print('這是你猜的第', n, '次')