import random
start = input('請輸入隨機數字開始值：')
end = input('請輸入隨機數字結束值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count = count + 1 #也可以寫成count += 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('這是你猜的第', count, '次')	 #因為猜中後程式break就不會執行第17行，所以加在這邊
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')	
