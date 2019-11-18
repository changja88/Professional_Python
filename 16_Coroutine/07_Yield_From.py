"""
yield_from 사용하기
"""
"""
- yield보다 훨씬 더 많은 일을 하므로 비슷한 키워드를 재사용한 것은 오해의 소지가 있다
- 다른 언어 에서는 await이라고 한다 
"""


def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


print(list(gen()))


def gen2():
    yield from 'AB'
    yield from range(1, 3)


print(list(gen2()))


def chain(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))

"""
- yield from x 표현식이 x에 대해서 첫 번째로 하는 일은 iter(x)를 호출해서 x의 반복자를 가져오는 것이다
  이는 모든 반복형이 x 자리에 올 수 있다는 뜻이다
- 그러나 값을 생성하는 내포된 for 루프를 대체하는 게 yield from이 하는 일의 전부가 아니다
- 진짜는, 가장 바깥쪽 호출자와 가장 안쪽에 있는 하위 제너레이터 사이에 양방향 채널을 열어 준다는 것이다
  따라서 이 둘이 값을 직접 주고받으며, 중간에 있는 코루틴이 판에 박힌 듯한 예외 처리 코드를 구현할 필요 없이 예외를
  직접 던질수 있다. 이전에는 불가능 했던 이 새로운 방식 덕분에 코루틴 위임을 할 수 있게 되었다
"""