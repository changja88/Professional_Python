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
    for line_no, line in enumerate(fp, 1):  # enumerate 는 순서가 있는 자료형(리스트, 튜플 문자열)을 입력으로 받아 인덱스 값을
        # 포함하는 enumerate 객체를 리턴 한다
        for match in WORDE_RE.finditer(line):  # finditer는 findall가 비슷하지 반복 가능한 객체를 리턴한
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
#       - defaultdict는 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리값의 초깃값으로 지정할수 있다 (숫자, 리스트, 셋등이 가능)
#       - 인자로 주어진 객체에 따라서 기본값이 결정된다 (int 는 0)
#       - default_factory가 설정되어 있지 않으면, 키가 없을 때 흔히 볼수 있는 KeyError 가 발생한다
#       - default_factory는 __getitem()__호출에 대한 기본값을 제공하기 위해 호출되며 다른 메서드는 호출 되지 않는다
#       - 따라서 defaultdict[k] 는 기본 값을 리턴 하지만 defaultdict.get(k)는 None을 반환하다(k값이 저장되어 있지 않은 경우)

index = collections.defaultdict(list)  # default_factory에 list 생성자를 갖고 있는 defaultdict를 생성한다
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORDE_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


#   - __missing__() 메서드
#       - 이 메서드를 이용해서 존재하지 않는 키를 처리한다
#       - 이 특수 메서드는 기본 클래스인 dict에는 정의되어 있지 않지만 dict는 이메서드를 알고 있다
#       - 따라서 dict클래스를 상속하고 __missing__ 메소드를 정의하면, dict.__getitem__()표준 메서드가 키를 발견 할수 없을때
#         KeyError를 발생시키지 않고 __missing__ 메서드를 호출한다
#       - missing()은 dict[k] 를 사용하는 경우 즉, getitem() 메서드를 사용할 때만 호출 된다
#         따라서, in 연산자를 구현하는 get() 이나 __contains__()메서드 등 키를 검생하는 메서드에는 영향을 주지 않는다
#         다시 말해서 getitem()메서드를 사용할 때만 defaultdict의 default_factory가 작동한다


# 조회할때 키를 문자열로 변환하는 StrKeyDict
#   - 사용자 정의 매핑형을 만들 떄는 dict보다 collections.UserDict 클래스를 상속하는 것이 더 낫다
#   - 여기에서는 dict.__getitem__() 내장 메서드가 __missing__() 메서드를 지원 하는것을 보여주기 위해서 dict를 상속했다
#
#   - 파이썬3 에서는 아주 큰 매핑의 경우에도 k in
class StrKeyDict0(dict):
    def __missing__(self, key):
        print('__missing__')
        if isinstance(key, str):  # 키가 문자열인지 확인한다
            raise KeyError(key)
        return self[str(key)]  # 키에서 문자열을 만들고 조회한다

    def get(self, key, default=None):
        print('__get__')
        # get()메서드는 self[key]표기법을 이용해서 __getitem__()메서드에 위힘한다
        # 이렇게 함으로써 __missing__()메서드가 작동할 수 있는 기회를 준다
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('__contains__')

        # 수정하지 않은(문자열이 아닐수 있는)키를 검색하고 나서, 키에서 만든 문자열로 검색한다
        return key in self.keys() or str(key) in self.keys()




d = StrKeyDict0(
    [('2', 'two'), ('4', 'four')]
)
print(d)
print(d['2'])  # 'two'
# print(d[4])  # 'four'
# print(d[1]) # KeyError
#
# print(d.get('2')) #'two'
print(d.get(4)) #'four' , get을 재정의 해주지 않으면 missing을 사용 하지 않음으로 None이 나온다
#
# print(d.get(1, 'N/A')) #'N/A'
#
# print(2 in d) # Ture
# print(1 in d) # False
