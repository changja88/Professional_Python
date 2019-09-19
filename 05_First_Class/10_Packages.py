# 함수평 프로그래밍을 위한 패키지
# - 귀도는 파이썬이 함수형 프로그래밍 언어를 지향하지 않았다고 공표하고 있지만,
#   operator와 functools 같은 패키지들의 지원 덕분에 파이썬에서도 제법 함수형 코딩 스타일을 사용 할수 있따

# Operator 모듈
# - reduce와 익명 함수로 구현한 팩토리얼
from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


# - lambda a,b : a*b 와 같이 사소한 익명 함수를 작성하는 수고를 덜기 위해 operator 모듈은 수십 개의 연산자에 대응하는
#   함수를 제공한다

from operator import mul


def fact(n):
    return reduce(mul, range(1, n + 1))


# - Operator모듈은 시퀀스에서 항목을 가져오는 람다를 대채하는 itemgetter()함수와ㅓ 객체의 속성을 읽는 람다를 대채하는
#   attrgetter()함수를 제공한다

metro_data = [
    ('Rusia', 'D', 4, (4.1, 4.2)),
    ('Seoul', 'B', 2, (2.1, 2.2)),
    ('Mexico', 'C', 3, (3.1, 3.2)),
    ('Sao Paulo', 'E', 5, (5.1, 5.2)),
    ('Tokyo', 'A', 1, (1.1, 1.2)),
]
from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# - itemgetter()에 여러개의 인덱스를 인수로 전달하면, 생성된 함수는 해당 인덱스의 값들로 구성된 튜플을 반환한다
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# - itemgetter의 형제인 attrgetter은 이름으로 객체 속성을 추출하는 함수를 생성한다
#   attrgetter에 여러 속성명을 인수로 전달하면, 역시 해당 속성값으로 구성된 튜플을 반환한다
#   게다가 속성명에 .이 포함되어 있으면 attrgetter는 내포된 객체를 찾아서 해당 송석을 가져온다

from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropils', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
print(('---------------------------------'))
print(metro_areas)

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')

print(('---------------------------------'))
for city in sorted(metro_areas, key=attrgetter('coord.lat')):  # 스트링인데 coord.lat이 되는게 신기
    print(name_lat(city))

# - methodcaller()
#   - 실행 중 함수를 생성한다는 점에서 attrgetter나 itemgetter메서드와 비슷하다
#   - mehtodcaller가 생성한 함수는 인수로 전달받은 객체의 메서드를 호출한다
#   - 활용 방안을 모르겠다
from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(('---------------------------------'))
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')  # functools.partial() 함수처럼 일부 인수를 고정 할 수 있음을 알수 있
print(hiphenate(s))

# - 이 외에도 52개의 함수들이 있지만 대부분은 이름으로 쉽게 내용을 추측할 수 있다
#       - iadd 와 iand처럼 i로 시작 하는 함수명은 += 및 &=와 같은 복합 할당 연산자다
#         이 함수들은 첫번째 인수가 가변형인 경우에는 첫번째 인수를 변경하며, 불변형인 경우에는 i가 없는 함수와 동일하게
#         단지 연산 결과를 반환한다


# functools.partial()로 인수 고정하기
# - functools 모듈은 몇가지 고위 함수를 통합한다. 그중 가장 널리 알려진 함수가 reduce
# - 하지만 나머지 함수 중 partial()및 이의 변형인 partialmethod()함수가 유용하다
# - 즉, 하나 이상의 인수가 이미 채워진 함수의 새 버젼을 만들기 위해서 사용된다

# - partial은 함수를 부분적으로 실행할 수 있게 해주는 고위 함수다
#   어떤 함수가 있을 때 partial()을 적용하면 원래 함수의 일부 인수를 고정한 콜러블을 생성한다
#   이 기겁은 하나 이상의 인수를 받는 함수를 그보다 적은 인수를 받는 콜백 함수를 사용하는 API에 사용하고자 할때 유용하다
# - partial의 첫번째 인수는 콜러블이며, 그 뒤에 바인딩할 위치 인수와 키워드 인수가 원하는 만큼 나온
from operator import mul
from functools import partial

triple = partial(mul, 3) # mul 함수의 첫번째 위치 인수를 3으로 바인딩해서 triple() 함수를 새로 만든다
print(('---------------------------------'))
print(triple(7)) # 테스트 이미 3이 들어가 있기 때문에 7을 넣어주면 21이 나온다

print(
    list(map(triple, range(1, 10))) # 3이 첫번째 인수로 들어가 있기때문에 3을 1에서 10까지 곱한 값이 나온다
)

# - partialmethod함수는 parial과 동일하지만 메서드에 대해 작동하도록 설게되었다
#   - partial은 사용 준비가 된 callable을 리턴하고
#   - parialmethod는 unbound method 로 사용될 callable을 리턴한다
import functools
def standalone(self, a=1, b=2):
    print(' called standalone with : ', (self, a, b))
    if self is not None:
        print(' self.attr = ', self.attr)


class MyClass:
    "Demostration class for functools"

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()
print('standalone')
standalone(None)
print()

print('method 1 as partialmethod')
o.method1() # partialmethod 에는 self가 들어가 있기 때문에 성공
print()

print('mehtod2 as partial')
try:
    o.method2() # partial 에는 self가 없기 때문에 실패
except TypeError as err:
    print('ERROR:{}'.format(err))


print()
print('method2 as partial to work')
o.method2(o) # partial에 없는 self를 넣어주면 성공