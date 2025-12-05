# calculator.py (수정된 내용)

def simple_calculator():
    """
    두 숫자와 연산자를 입력받아 사칙연산을 수행하고 결과를 출력
    """
    
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        operator = input("연산자 (+, -, *, /)를 입력하세요: ")
        num2 = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print("오류: 유효한 숫자를 입력해 주세요.")
        return

    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2 
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "0으로 나눌 수 없습니다."
    else:
        result = "사용할 수 없는 연산자입니다."

    print("결과:", result)