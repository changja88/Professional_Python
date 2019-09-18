# 고위함수
# - 함수를 인수로 받거나, 함수를 결과로 반환하는 함수를 고위 함수 라고 한다
# - map, sorted 등등

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
a = sorted(fruits, key=len)  # len 함수를 key의 인자로 전달한다
print(a)


def reverse(word):
    return word[::-1]


# 단어 처라를 거꾸로 해서 정
a = sorted(fruits, key=reverse)
print(a)


# - map(), reduce(), filter(), apply() 등의 고위 함수가 널리 알려져 있다
#       - apply()는 파이썬 2.3.에서 중단 3에서는 제거
#       - map, reduce, filter는 여전히 존재하지만 대부분의 경우 더 나은 다른 방법이 있다


# Map, Filter, Reduce의 대안
# - 지능형 리스트와 제너레이터 표현식이 소개된 후에는 이 함수들의 중요성이 떨어졌다
# - 지능형 리스트나 제너레이터 표현식이 map과 filter의 조합이 처리하는 작업을 표현할 수 있을 뿐만 아니라 가독성이 더 좋기 때문

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


list(map(factorial, range(6)))  # 함수형
[factorial(n) for n in range(6)]  # 제너레이터 표현식

list(map(factorial, filter(lambda n: n % 2, range(6))))  # 함수형
[factorial(n) for n in range(6) if n % 2]  # 제너레이터 표현식

# - 파이썬3에서 map, filter는 제너레이터(일종의 반복 가능 객체)를 반환하므로, 제너레이터 표현식이 이 함수들을 직접 대체한다
# - 내장 되어 있던 reduce는 functools 모듈로 떨어져 나왔다. reduce는 주로 합계를 구할때 사용 하는데 내장 함수 sum()이 더 좋다

from functools import reduce
from operator import add

reduce(add, range(100))
sum(range(100)) # 함수를 임포트하거나 추가할 필요 없다
# - sum과 reduce는 연속된 항목에 어떤 연산을 적용해서, 이전 결과를 나주거시키면서 일련의 값을 하나의 값으로 리덕션 한다는 공통점이 있다

# - 내장된 reduction 함수
#   - all(iterable)
#   - any(iterable)