"""
파이썬 3.3.의 새로운 구문 : yield from
"""
"""
- 다른 제너레이터에서 생서된 값을 상위 제너레이터 함수가 생성해야 할 때는 전통적으로 중첩된 for 루프를 사용했다
- yield from 은 16장에 자세히 나온다
"""


def chain(*iterables):  # 전통적인 방식
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(
    list(chain(s, t))
)


def chain2(*iterables):
    for i in iterables:
        yield from i


print(
    list(chain2(s, t))
)
