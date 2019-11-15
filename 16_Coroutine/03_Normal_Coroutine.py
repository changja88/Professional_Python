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
