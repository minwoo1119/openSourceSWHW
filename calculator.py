# calculator.py

def add(x, y):
    """두 수를 더합니다."""
    return x + y

def subtract(x, y):
    """두 수를 뺍니다."""
    return x - y

def multiply(x, y):
    """두 수를 곱합니다."""
    return x * y

def divide(x, y):
    """두 수를 나눕니다."""
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y

def calculator():
    """간단한 계산기 프로그램 메인 함수"""
    print("--- 간단 계산기 ---")
    print("지원 연산: +, -, *, /")
    
    try:
        # 사용자로부터 두 수와 연산자를 입력받습니다.
        num1 = float(input("첫 번째 수를 입력하세요: "))
        op = input("연산자(+, -, *, /)를 입력하세요: ")
        num2 = float(input("두 번째 수를 입력하세요: "))
    except ValueError:
        print("오류: 유효한 숫자를 입력하세요.")
        return

    # 연산자에 따라 해당 함수를 호출하여 결과를 계산합니다.
    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    else:
        result = "오류: 지원하지 않는 연산자입니다."
    
    # 결과를 출력합니다.
    print(f"\n{num1} {op} {num2} = {result}")

# 프로그램 실행
if __name__ == "__main__":
    calculator()
