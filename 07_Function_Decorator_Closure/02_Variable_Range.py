# 변수 범위 규칙
def f1(a):
    print(a)
    print(b)


# f1(3) # 당연히 에러 발생
b = 6
f1(3)  # 에러 발생하지 않음 (전역 변수 b에 값을 할당 하였기 때문)

b = 6


def f2(a):
    print(a)  # 출력 된다
    print(b)  # 에러 발생 : 전역 변수 b의 값이 출력 되지 않는다(아래 주석을 풀고 실행)
    # b = 9


print()
f2(3)


def f3(a):
    global b  # 함수 안에 할당하는 문장이 있지만 인터프리터가 b를 전역 변수로 다루기 원하는 경우 global 키워드 사용
    print(a)
    print(b)
    b = 9
    print(b)


print()
f3(3)
