# 일급 함수
# - 파이썬의 함수는 일급 객체다 (정수, 문자열, 딕셔너리도)
# - 일급 객체 정의
#   - 런타임에 생성할 수 있다
#   - 데이터 구조체의 변수나 요소에 할당할 수 있다
#   - 함수 인수로 전달할 수 있다
#   - 함수 결과로 반환할 수 있다

# 함수를 객체처럼 다루기
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial.__doc__)  # 객체의 도움말 텍스느를 생성하기 위해 사용된다 -> 대화형에서는 help(factorial)
print(type(factorial))

#   - 일급 객체로 사용 하는 방법

fact = factorial
print(fact(5))

print(
    map(factorial, range(11))
)

print(
    list(map(fact, range(11)))
)

