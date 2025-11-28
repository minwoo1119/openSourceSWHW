def average_calculate():
	sum = 0
	point = 0
	while True:
		score = float(input("점수를 하나씩 입력(다 입력시 음수 입력):"))
		if (score < 0):
			average = sum / point
<<<<<<< HEAD
			print("당신의 평균 점수:", average)
=======
			print("당신의 평균 점수:", average)
>>>>>>> main
			break
		sum = sum + score
		point = point + 1
			
