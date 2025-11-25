def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def string_menu():
    while True:
        print("\n=== 문자열 처리 ===")
        print("1. 대문자 변환")
        print("2. 소문자 변환")
        print("0. 돌아가기")
        choice = input("선택: ")
        if choice == "0":
            break
        text = input("문자열 입력: ")
        if choice == "1":
            print("[결과]", to_upper(text))
        elif choice == "2":
            print("[결과]", to_lower(text))
        else:
            print("잘못된 선택")

