# 파이썬에서는 메서를 데커레이트 하기 위해 property(), classmethod(), staticmethod() 등
# 총 3개의 내장 함수를 제공한다. (나중에 설명이 나옴 이번 장 말고)

# 그리고 자주 볼 수 있는 데커레이터 중에는 functools.wraps()가 있다.
# 이 함수는 제대로 작동하는 데커레이터를 만들기 위한 헬퍼로, 표준 라이브러리가 제공하는 데커레이터들 중
# lru_cache와 3.4에서 추가된 singledispatch()가 가장 흥미롭다

# functools.lru_cache()를 이용한 메모이제이션
# - 실제로 쓸모가 많은 데커레이터로서, 메모이제이션을 구현한다
# - 메모이제이션은 이전에 실행항 값비싼 함수의 결과를 저장함으로써 이전에 사용된 인수에 대해 다시 계산할 필요가 없게 해준다
# - lru -> Least Recently Used (사용한지 가장 오래된)으로써,
#   오랫동안 사용하지 않은 항목을 버림으로써 캐시가 무한정 커지지 않음을 의미한다

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)  # clocked()에 대한 클로저에 자유변수 func가 들어가야 이 코드가 작동한다
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args, result))
        return result

    return clocked


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
# -> 계산 낭비가 엄청 나다, fibonacci(1)만 8번이 호출되었다

# lru_cache()로 성능 개선 버젼
import functools


@functools.lru_cache()  # 이거 하나만 해주면 된다
@clock
def fibonacci(n):
    if n < 2:
        return 2
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print()
    print(fibonacci(6))

# - 어리석은 재귀 알고리즘을 쓸 만하게 만드는 것 외에 웹에서 정보를 가져와야 하는 애플리케이션에서도 진가를 발휘한다
functools.lru_cache(maxsize=128, typed=False)
# - maxsize = 는 얼마나 많은 호출을 저장할지 결정한다 -> 캐시가 가득차면 가장 오래된 결과를 버리고 공간을 확보한다
#   최적의 성능을 내기 위해 maxsize는 2의 제곱이 되어야 한다
# - typed 인수는 True로 설정되는 경우 인수의 자료형이 다르면 결과를 따로 저장한다
#   예를 들어 일반적으로 1과 1.0은 동일하다고 가정하지만 실수형 인수와 정수형 인수를 구분해야 하는 경우가 있을 것이다
# - lru_cache가 결과를 저장하기 위해 딕셔너리를 사용하고, 호출할 때 사용한 위치 인수와 키워드 인수를 키를 사용 하므로,
#   데커레이트된 함수가 받는 인수는 모두 '해시 가능' 해야 한다
