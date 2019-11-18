"""
예제: 이동 평균을 계산하는 코루틴
"""


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        # 코루틴을 중단하고, 지금까지의 평균을 생성하기 위해 사용된다. 나중에 호출자가 이 코루틴에 값을 보내면 루프를 다시 실행한다
        total += term
        count += 1
        average = total / count


"""
클로져와 비교 했을 때 장점
- total과 count를 지역 변수로 사용할 수 있다
- 객체 속성이나 별도의 클로저 없이 평균을 구하는데 필요한 값들을 유지 할 수 있다
"""

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))


def test2(i):
    print('start test2 coroutine')
    while True:
        value = yield i
        i += value


b = test2(5)
print(next(b))
# start test1 coroutine 출력 후 5출력, yield i 부분에서 멈춰있다.
print(b.send(3))
# yield를 통해 3을 전달하여 value가 3이 된다. 이후 i += value 줄을 거쳐 i=8이되고 한바퀴 돌아 8을출력, yield에서 멈춘다.
print(b.send(5))
