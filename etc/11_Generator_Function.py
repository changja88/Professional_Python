"""
제너리이터 함수의 작동 방식
- 본체 안에 yeld키워드를 가진 함수는 모두 제너리이터 함수다
- 제너레이터 함수는 호출되면 제너레이터 객체를 반환한다
- 즉, 제너레이터 함수는 제너레이터 팩토리라고 할 수 있다
"""


def gen_123():
    yield 1
    yield 2
    yield 3


for i in gen_123():
    print(i)

g = gen_123()
print(next(g))

"""
- 제너레이터 함수는 함수 본체를 포함하는 제너레이터 객체를 생성한다
- next()를 제너레이터 객체에 호출하면 함수 본체에 있는 다음 yeild로 진행하며, next()는 함수 본체가
  중단된 곳에서 생성된 값을 평가한다
- 마지막으로, 함수 본체가 반환될 때 이 함수를 포함하고 있는 제너레이터 객체는 Iterator프로토콜에 따라
  StopIteration 예외를 발생시킨다
"""
"""
- 제너레이터에서 가져온 결과에 대해 이야기할 때 좀더 명확히 할 필요가 있다
- 제너레이터는 값을 '생성'하는 것이지 값을 '반환'한다고 하지는 않는다
- 함수는 값을 반환한다. 제너레이터 함수를 호출 하면 제너레이터가 반환된다 -> 제너레이터 객체는 값을 생성한다
- 제너레이터는 일반적인 방식으로 값을 '반환'하지 않는다 
  제너레이터 함수 안에 있는 return 문은 제너레이터 객체가 StopIteration예외를 발생하게 만든다
"""


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


for c in gen_AB():
    print('-->', c)

"""
제너레이터 표현식
"""
"""
- 제너레이터 표현식은 지능형 리스트의 느긋한 버전이라고 생각할 수 있다
- 조급하게 리스트를 생성하는 대신, 필요에 따라 항목을 느긋하게 생성하는 제너레잍를 반환하기 때문이다
- 즉, 지능형 리스트가 리스트 팩토리라면, 제너레이터 표현식은 제너레이터 팩토리라고 생각할 수 있다 
"""


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


res1 = [x * 3 for x in gen_AB()]  # -> 조급한 계산

for i in res1:
    print('-->', i)

print()
res2 = (x * 3 for x in gen_AB())  # -> 느긋한 계
for i in res2:
    print('-->', i)

"""
제너레이터 표현식 언제 사용 할까?
- 제너레이터 표현식이 여러 줄에 걸쳐 있을 때는 가독성을 위해 제너레이터 함수를 사용한다
- 저너레이터 함수는 이름이 있기 때문에 재사용도 가능하다
"""
