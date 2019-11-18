"""
코루틴을 기동하기 위한 데커레이터
"""
"""
- 코루틴은 기동되기 전에는 할 수 있는 일이 많지 않다.
- @coroutine 데커레이터가 널리 사용된다
"""


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
"""
- @coroutine데커레이터를 사용 하면 코루틴을 가동 하기 위해서 next(coro_avg)를 안해줘도 된다
- yield from 구문은 자동으로 자신을 실행 한 코루틴을 가동시키므로, 같이 사용할 수 없다
"""
