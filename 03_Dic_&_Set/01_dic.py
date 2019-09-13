# 딕셔너리와 집합

# - 파이썬의 고성능 딕셔너리 뒤에는 해시 테이블이라는 엔진이 있다
# - 집합도 해시 테이블을 이용ㅇ해서 구현하므로, 이장에서는 집합도 다룬다.
# - 해시 테이블이 작동하는 방식을 알아야 딕셔너리와 집합을 최대로 활용할 수 있다

# 1. 일반적인 매핑형
import collections

my_dict = {}
print(
    isinstance(my_dict, collections.Mapping)
)

# - 기본적으로 dict을 생성하는 방
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(
    zip(
        ['one', 'two', 'three'], [1, 2, 3]
    )
)
d = dict(
    [
        ('two', 2), ('one', 1), ('three', 3)
    ]
)
e = dict(
    {'three': 3, 'one': 1, 'two': 2}
)

print(a == b == c == d == e)

# 2. 지능형 딕셔너리
# - 모든 반복형 객체에서 키-값 쌍을 생서함으로써 딕셔너리 객체를 만들 수 있다
#   - 키-값 쌍의 리스트를 바로 사용할 수 있
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, "United States")
]
#   - 쌍을 뒤바꿔서 country는 키, code는 값이 된다
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
#   - 쌍을 한 번 더 뒤바꿔서 값을 대문자로 바꾸고, code가 66보다 작은 항목만 걸러낸다
a = {code: country.upper() for country, code in country_code.items() if code < 66}
print(a)

#   - update 메소드 (duck typing 사례)
a.update(
    {code: country.lower() for country, code in country_code.items()}
)
print(a)

#   - 존재하지 않는 키를 setdefault()로 처리하기
import sys
import re

WORDE_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[0], encoding='utf-8')as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORDE_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

with open(sys.argv[0], encoding='utf-8')as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORDE_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

test = {'a': 1, 'b': 2, 'c': 3}
d = test.setdefault('f', 2)
print(d)

d = test.setdefault('a', [])  # setdefault 는 단순 값만이 아니라 list도 기본값으로 나오게 할 수 있다
print(d)

# 융통성 있게 키를 조회하는 매핑
#   - 검색할때 키가 존재하지 않으면 어떤 특별한 값을 반환하는 매핑을 만들수 있다
#   - 첫번째는 일반 dict 말고 defaultdict를 사용 하는 방법이고
#   - 두번째 방법은 dict등의 매핑형을 상속해서 __missing__() 메서드를 추가하는 방법이다

#   - defaultdict : 존재하지 않는 키에 대한 또 다른 처리
