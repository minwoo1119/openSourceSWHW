<<<<<<< HEAD
# 메인 파이썬 코드입니다.
# 개별적으로 파일을 생성해서 작업해주세요.
git confilt test
=======
# from converters import unit_converter      # 단위 변환기 함수 (예시)
# from calculators import simple_calculator  # 간단 계산기 함수 (예시)
# from score_analysis import calculate_average # 점수 평균 계산 함수 (예시)
# from string_utils import string_processor   # 문자열 처리 함수 (예시)
# from random_generator import generate_password # 랜덤 비밀번호 생성기 함수 (예시)

def main_menu():
    print("기능 선택 메뉴 🛠️")
    print("1. 단위 변환기 (cm ↔ m, kg ↔ g 등)")
    print("2. 간단 계산기 (사칙연산)")
    print("3. 점수 평균 계산")
    print("4. 문자열 처리 (대문자/소문자 변환 등)")
    print("5. 랜덤 비밀번호 생성기")
    print("0. 프로그램 종료")
    print("--------------------------")

    while True:
        try:
            choice = input("실행할 기능의 번호를 입력하세요 (0-5): ").strip()
            
            if choice == '0':
                print("\n👋 프로그램을 종료합니다. 감사합니다!")
                break
            
            elif choice == '1':
                print("\n[1. 단위 변환기]를 실행합니다...")
                # unit_converter()  # 여기에 단위 변환기 함수 호출
                pass

            elif choice == '2':
                print("\n[2. 간단 계산기]를 실행합니다...")
                # simple_calculator() # 여기에 간단 계산기 함수 호출
                pass

            elif choice == '3':
                print("\n[3. 점수 평균 계산]을 실행합니다...")
                # calculate_average() # 여기에 점수 평균 계산 함수 호출
                pass

            elif choice == '4':
                print("\n[4. 문자열 처리]를 실행합니다...")
                # string_processor() # 여기에 문자열 처리 함수 호출
                pass

            elif choice == '5':
                print("\n[5. 랜덤 비밀번호 생성기]를 실행합니다...")
                # generate_password() # 여기에 랜덤 비밀번호 생성기 함수 호출
                pass
            
            else:
                print("오류: 유효하지 않은 번호입니다. 0부터 5 사이의 숫자를 입력해주세요.")
            
            if choice in ['1', '2', '3', '4', '5']:
                print("\n" + "="*40)
                main_menu() 
                break

        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")
            
if __name__ == "__main__":
    main_menu()
>>>>>>> b08ea49 (edit main.py by minwoo)
