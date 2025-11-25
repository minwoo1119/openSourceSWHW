n = 0
m = 0
x = 0
y = 0
while True:
	x = float(input("점수를 입력하시오.(점수를 다 입력하셨다면 음수를 입력): "))
	if (x < 0):
		y = n / m
		print("평균 점수:", y)
		break
	n = x + n
	m = m + 1
