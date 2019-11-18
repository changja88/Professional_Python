"""
코루틴 종료와 예외 처리
"""
"""
- 코루틴 안에서 발생한 예외를 처리하지 않으면, next()나 send()로 코루틴을 호출한 호출자에 예외가 전파된다
- 제너레이터 객체는 호출자가 코루틴에 명시적으로 예외를 전달할 수 있게 해주는 throw()와 close()메서드를 제공한다
    - throw : 제너레이터가 중단한 곳의 yield표현식에 예외를 전달한다. 제너레이터가 예외를 처리하면, 제어흐름이 다음
              yield 문까지 진행하고, 생성된 값은 throw()호출 값이 된다. 제너레이터가 예외를 처리하지 않으면 호출자 
              까지 전파된다
    - close : 제너레이터가 실행을 중단한 yield표현식이 GeneratorExit예외를 발생시키게 만든다. 제너레이터가 예외를 처리하지 
              않거나 StopIteration예외를 발생시키면, 아무런 에러도 호출자에 전달되지 않는다. GeneratorExit예외를 받으면
              제너레이터는 아무런 값도 생성하지 않아야한다. 아니면 RuntimeError에외가 발생한다. 제너레이터에서 발생하는 다른
              예외는 모두 호출자에 전달된다
"""


class DemoException(Exception):
    """설명에 사용할 예외 유형"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoeException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))

    raise RuntimeError('This line should never run')


exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(12)
exc_coro.close()
from inspect import getgeneratorstate

print(getgeneratorstate(exc_coro))

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))  # 예외가 처리되면 GEN_SUSPENDED가 된다

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(ZeroDivisionError)
# print(getgeneratorstate(exc_coro)) # 예외를 처리 할수 없으면 GEN_CLOSED가 된다

"""
- 코루틴이 어떻게 종료되든 어떤 정리 코드를 실행해야 하는 경우 try/finally블록 안에 넣으면 된다
"""


def demo_finally():
    print('-> corotine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoeException handled. Continuing...')

            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')
