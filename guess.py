import random
start = input('請決定隨機數字開始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)

x = random.randint(start, end)
n = 0
while True:
	n += 1 # n = n + 1
	y = input('請猜數字: ')
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