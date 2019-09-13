# Tuple
#   - 튜플은 불변 리스트 이지만, 필드명이 없는 레코드로 사용할 수도 있다

# 1. 레코드로서의 튜플
#   - 튜플을 필드의 집합으로 사용하는 경우에는 항목 수가 고정되어 있고 항목의 순서가 중요하다
import collections

lax_coordinates = (33.9452, -118.12341)
citiy, year, pop, chg, area = ('Tokyo', 200, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'SDA201010')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
    # 튜플 언팩킹 -> 병렬 할당

for country, _ in traveler_ids:
    print(country)

# 2.튜플 언팩킹
#   - 병렬 할당
latitude, logitude = lax_coordinates

#   - 튜플 언팩킹을 이용하면 임시 변수를 사용하지 않고 두 변수의 값을 서로 교환할 수 있다
a = 3
b = 2
b, a = a, b

#   - *를 붙여 튜플을 언패킹할수 있다
divmod(20, 8)  # 이걸
t = (20, 8)
divmod(*t)  # 이렇게 할 수도있다
quotient, remainder = divmod(*t)  # 당연히 이렇게도 된다

#   - 언팩킹의 다른 사용 방법
import os

_, filename = os.path.split('/home/hyun/.ssh/dirsa.pub')  # os.path.split을 하면 파일과 폴더 부분을 잘라준다

#   - 튜플을 언팩킹할때 일부 항목에만 관심이 있는 경우에는 *를 사용할수 있다
a, b, *rest = range(5)  # (0, 1, [2, 3, 4])
a, b, *rest = range(3)  # (0, 1, [2])
a, b, *rest = range(2)  # (0, 1, [])

#   - 병렬 할당의 경우 * 는 단 하나의 변수에만 적용할 수 있다
a, *body, c, d = range(5)  # (0, [1, 2], 3, 4)
*head, b, c, d = range(5)  # ([0, 1], 2, 3, 4)

#   - 내포된 튜플 언패킹 (튜플 안에 튜플 언팩킹)
metro_areas = [
    ('A', 'a', 1.123, (2.123456, 3.123456)),
    ('B', 'b', 2.123, (3.123456, 4.123456)),
    ('C', 'c', 3.123, (4.123456, 5.123456)),
    ('D', 'd', 4.123, (5.123456, 6.123456)),
    ('E', 'e', 5.123, (6.123456, 7.123456)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, logitude) in metro_areas:
    if logitude >= 3:
        print(fmt.format(name, latitude, logitude))

#   - 명명된 튜플
#       - collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팰토리 함수로서, 디벙깅에 유용하다
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
# City = namedtuple('City', ['name', 'country', 'population', 'coordinates']) # 위와 상
tokyo = City('Tokyo', 'JP', 36.933, (35.68922, 139.123123))
print(tokyo)

Card = namedtuple('Card', ['rank', 'suit'])
Card2 = namedtuple('Card', 'rank suit')
a = Card('high', "d")
b = Card2('high', "d")
print(a)
print(b)

#   - 불변 리스트로서의 튜플
#       - 튜플은 항목을 추가하거나 삭제하는 기능 및 __reversed__를 제외하고 리스트가 제공하는 메서드를 모두 지원한다

