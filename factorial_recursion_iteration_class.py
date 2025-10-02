#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 나호정
#  작성일: 2024-10-02
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

user_input = input("정수를 입력하세요 :").strip()
if user_input.lower() in ['q', 'quit']:
    print(f"프로그램을 종료합니다.")
    exit()
if user_input.isdigit():
    n = int(user_input)
    print(f"정수로 변환 : {n} (q/quit 종료):")
    
else:
    try:
        n = int(float(user_input))
        print(f"실수에서 정수로 변환 : {n}")

    except ValueError:
        print("유효하지 않은 입력입니다. 0 이상의 정수를 입력하세요.")

# 입력 2: while 루프
while True:
    user_input = input("숫자를 입력하세요: ")
    if user_input.replace('.', '', 1).isdigit():
        n = int(float(user_input))
        print(f"유효한 숫자입니다. 정수로 변환:{n}")
        break
    else:
        print("유효하지 않은 숫자입니다. 숫자만 입력해주세요.")
        continue

def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    #  재귀적으로 문제 해결 n! -> 재귀함수 정의

    # 1. base case (재귀호출 종료 조건)
    if n == 1:
        return 1
    
    # 2. 재귀 분할 호출
    return n * factorial_rec(n-1)




if __name__ == "__main__":
    n = int(input("\n 정수를 입력하세요: ").strip())
    print(f"반복문 기반: {factorial_iter(n)}")
    try:
        print(f"재귀 기반: {factorial_rec(n)}")
    except RecursionError:
        print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main()
