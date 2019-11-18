"""
코루틴에서 값 반환하기
"""
"""
코루틴이 활성화 될때마다 의미 있는 값을 생성하지는 않지만 최후에 어떤 의미 있는 값을 반환하는 경우
"""
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(6.5))
# print(coro_avg.send(None))  # StopIteration예외에 값이 들어 있다

coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(6.5))
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value

print(result)
"""
- 예외에서 값을 가져오는 것이 이상하게 느껴질수 있지만 PEP380에 정의되어 있는 방법이다
- 또는 yield from 구문을 사용하면 된다
"""
