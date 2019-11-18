"""
코루틴으로 사용되는 제너레이터의 기본 동작
"""


def simple_coroutine():  # 코루틴은 자신의 본체 안에 yield문을 가진 일종의 제너레이터 함수로 정의된다
    print('-> coroutine started')
    x = yield
    # yield를 표현식에 사용한다(오른쪽에 위치) 단지 호출자에서 데이터를 받도록 설계하면 yield는 값을 생성하지 않는다
    # yield키워드 뒤에 아무런 표현식이 없을 때 값을 생성하지 않으려는 의도를 암묵적으로 표현한다
    print('-> coroutine received:', x)


# my_coro = simple_coroutine()
# print(my_coro)
# next(my_coro)
# 제너레이터가 아직 실행되지 않았으므로 yield문에서 대기하지 않는다. 따라서 먼제 next를 호출해서
# 제너레이터를 yield문 까지 실행함으로써 데이터를 전송할 수 있는 상태를 만든다
# my_coro.send(42)
# 제너레이터의 send()메서드를 호출해서 코루틴 본체 안의 yield문의 값을 42로 만든다
# 이제 코루틴이 실행을 재개해서 다음 yield문이 나오거나 종료될 때까지 실행한다

# 여기에서 제어 흐름이 코루틴 본체의 끝에 도달하므로, 일반적인 제너레이터와 마찬가지로 StopIteration예외를 발생시킨다

"""
코루틴은 네가지 상태를 가진다 
inspect.getgeneratorstate()함수를 이용해서 현재 상태를 알 수 있다. 이 함수느 ㄴ아래 네가지중 하나를 리턴한다
- GEN_CREATED -> 실행을 시작하기 위해 대기하고 있는 상태
- GEN_RUNNING -> 현재 인터프리터가 실행하고 있는 상태
- GEN_SUSPENDED -> 현재 yield문에서 대기하고 있는 상태
- GEN_CLOSED -> 실행이 완료된 상태

- 코루틴이 아직 기동되지 않은 상태(GEN_CREATED)인 경우에는 send()메서드를 호출할수 없다 -> 호출하면 오류 발생
"""


def simple_coro2(a):
    print('-> started: a=', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate

print(getgeneratorstate(my_coro2))
next(my_coro2)

print(getgeneratorstate(my_coro2))
my_coro2.send(28)

# my_coro2.send(99)

getgeneratorstate(my_coro2)
