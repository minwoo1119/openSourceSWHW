def average_calculate():
        sum = 0
        point = 0
        while True:
                score = float(input("하나씩 점수를 입력하세요.(다 입력했다면 아무 음수나 입력하여 끝내세요.):"))
                if (score < 0):
                        average = sum / point
                        print("평균 점수는 다음과 같습니다.:",average)
                        break
                sum = sum + score
                point = point + 1
